
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("sales_model.pkl")

st.title("Weekly Sales Prediction")
st.write("Enter the details below to predict weekly sales.")

store = st.number_input("Store number", min_value=1, value=1)
year = st.number_input("Year", min_value=2000, max_value=2035, value=2012)
month = st.number_input("Month", min_value=1, max_value=12, value=10)
day = st.number_input("Day", min_value=1, max_value=31, value=26)
week = st.number_input("Week", min_value=1, max_value=53, value=43)
holiday = st.selectbox("Holiday week?", [0, 1])
temperature = st.number_input("Temperature", value=60.0)
fuel_price = st.number_input("Fuel price", min_value=0.0, value=3.5)
cpi = st.number_input("CPI", min_value=0.0, value=220.0)
unemployment = st.number_input("Unemployment", min_value=0.0, value=7.0)

if st.button("Predict Weekly Sales"):
    inputs = pd.DataFrame([{
        "Store": store,
        "Year": year,
        "Month": month,
        "Day": day,
        "Week": week,
        "Holiday_Flag": holiday,
        "Temperature": temperature,
        "Fuel_Price": fuel_price,
        "CPI": cpi,
        "Unemployment": unemployment
    }])

    prediction = model.predict(inputs)[0]
    st.success(f"Predicted Weekly Sales: ${prediction:,.2f}")
