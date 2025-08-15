import streamlit as st
import joblib
import pandas as pd

# Load the trained car price model
model = joblib.load("model.joblib")

# Load dataset
data = pd.read_csv("Cardetails.csv")

# Extract brands (first word from the name column) and sort them
brands = sorted(data['name'].dropna().apply(lambda x: x.split()[0]).unique())

st.title("🚗 Car Price Prediction App")
st.write("Select the car brand and enter details to predict the selling price.")

# Select brand
brand = st.selectbox("Car Brand", brands)

# Filter available models for the selected brand
models_for_brand = sorted(data[data['name'].str.startswith(brand)]['name'].unique())
car_model = st.selectbox("Car Model", models_for_brand)

# Other input fields from dataset categories
fuel = st.selectbox("Fuel Type", sorted(data['fuel'].dropna().unique()))
seller_type = st.selectbox("Seller Type", sorted(data['seller_type'].dropna().unique()))
transmission = st.selectbox("Transmission", sorted(data['transmission'].dropna().unique()))
owner = st.selectbox("Owner", sorted(data['owner'].dropna().unique()))
year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, value=2015)
km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=1000000, value=50000)
mileage = st.number_input("Mileage (kmpl)", min_value=0.0, max_value=50.0, value=18.0, format="%.1f")
engine = st.number_input("Engine (CC)", min_value=0, max_value=5000, value=1200)
max_power = st.number_input("Max Power (bhp)", min_value=0.0, max_value=500.0, value=80.0, format="%.1f")
seats = st.number_input("Number of Seats", min_value=2, max_value=10, value=5)

# Prediction button
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        'name': car_model,
        'fuel': fuel,
        'seller_type': seller_type,
        'transmission': transmission,
        'owner': owner,
        'year': year,
        'km_driven': km_driven,
        'mileage': mileage,
        'engine': engine,
        'max_power': max_power,
        'seats': seats
    }])

    try:
        prediction = model.predict(input_df)
        st.success(f"💰 Estimated Selling Price: ₹{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error making prediction: {e}")

st.caption("This is a machine learning model prediction and should be used for estimation purposes only.")
