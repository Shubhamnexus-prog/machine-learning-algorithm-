import streamlit as st
import pandas as pd
import pickle


# Load model
with open("car_price_model.pkl", "rb") as file:
    model = pickle.load(file)


# Page configuration
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗"
)


st.title("🚗 Used Car Price Prediction")
st.write("Enter your car details")


# =========================
# Inputs
# =========================

car_name = st.text_input(
    "Car Name",
    "Maruti Swift"
)

year = st.number_input(
    "Manufacturing Year",
    min_value=1990,
    max_value=2026,
    value=2018
)

km_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=30000
)

fuel = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Individual", "Dealer", "Trustmark Dealer"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Owner",
    [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car"
    ]
)


# =========================
# Prediction
# =========================

if st.button("Predict Price"):

    car_data = pd.DataFrame({
        "name": [car_name],
        "year": [year],
        "km_driven": [km_driven],
        "fuel": [fuel],
        "seller_type": [seller_type],
        "transmission": [transmission],
        "owner": [owner]
    })

    prediction = model.predict(car_data)[0]

    st.success(f"Car: {car_name}")

    st.metric(
        "Predicted Selling Price",
        f"₹ {prediction:,.0f}"
    )