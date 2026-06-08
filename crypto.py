import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("crypto_model.pkl", "rb"))

# Load data for dropdown
df = pd.read_csv('BTC_USD_Price_Prediction_Data.csv')
df.drop("Unnamed: 0", axis=1, inplace=True)

currencies = sorted(df["Currency"].unique())

st.title("📈 Crypto Price Prediction App")

# Inputs
currency = st.selectbox("Currency", currencies)

year = st.number_input(
    "Year",
    min_value=2014,
    max_value=2021,
    value=2021
)
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

selected_month = st.selectbox(
    "Select Month",
    list(months.keys())
)

month = months[selected_month]

open_price = st.number_input("24h Open (USD)", min_value=0.0)
high_price = st.number_input("24h High (USD)", min_value=0.0)
low_price = st.number_input("24h Low (USD)", min_value=0.0)

# Predict
if st.button("Predict Closing Price"):

    input_df = pd.DataFrame([[
        currency,
        year,
        month,
        open_price,
        high_price,
        low_price
    ]], columns=[
        "Currency",
        "Year",
        "Month",
        "24h Open (USD)",
        "24h High (USD)",
        "24h Low (USD)"
    ])

    prediction = model.predict(input_df)

    st.success(f"💰 Predicted Closing Price: ${prediction[0]:.2f}")