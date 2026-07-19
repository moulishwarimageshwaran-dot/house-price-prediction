import streamlit as st
import pandas as pd
import joblib

# 1. Train aana brain-ah (model) load pannuvom
try:
    model = joblib.load('model.pkl')
except FileNotFoundError:
    st.error("❌ Error: 'model.pkl' file-ah kaanom! Terminal-la munaadi 'python train.py' run pannunga.")
    st.stop()

# Page setting title configuration setup layout
st.set_page_config(page_title="Tamil Nadu Real Estate Estimator", layout="centered")

st.title("🏡 Tamil Nadu Smart House Price Prediction App")
st.write("Unga residential features & location-ah select panni property market value-ah instantaneous-ah check pannunga!")

st.markdown("---")

# 2. Interactive Input Fields Configuration System (Sidebar mapping dashboard template layout layout)
col1, col2 = st.columns(2)

with col1:
    sqft = st.number_input("Total Square Feet (Sqft)", min_value=300, max_value=8000, value=1200, step=50)
    bedrooms = st.selectbox("Bedrooms (BHK)", options=[1, 2, 3, 4, 5], index=1)
    bathrooms = st.selectbox("Bathrooms", options=[1, 2, 3, 4], index=1)
    floors = st.selectbox("Total Floors Count", options=[1, 2, 3, 4, 5], index=0)
    age = st.slider("House Age (Years old history)", min_value=0, max_value=40, value=2)

with col2:
    parking = st.selectbox("Car/Bike Parking Spaces", options=[0, 1, 2, 3], index=1)
    balcony = st.selectbox("Available Balconies", options=[0, 1, 2, 3], index=1)
    location_score = st.slider("Location Development Score (1-10 area quality index)", 1, 10, 8)
    furnishing = st.radio("Furnishing Status Type", ["Unfurnished", "Semi-Furnished", "Fully-Furnished"], horizontal=True)

# 3. Real-Time Regional Tracking Dropdown Mapping Elements Setup Matrix fields
location_name = st.selectbox("Select Regional Locality / City", ["Chennai Region Zone", "Coimbatore Regional Cluster", "Salem Smart City Belt"])

# Text data matrix arrays values-ah key indexing mappings format encoding algorithms-ku shift framework mathurom
location_map = {"Chennai Region Zone": 1, "Coimbatore Regional Cluster": 2, "Salem Smart City Belt": 3}
furnish_map = {"Unfurnished": 1, "Semi-Furnished": 2, "Fully-Furnished": 3}

location_value = location_map[location_name]
furnish_value = furnish_map[furnishing]

st.markdown("---")

# 4. Property Price Estimation Processing Trigger Execution Logic Component System
if st.button("💰 Predict Property Valuation Price", use_container_width=True):
    # Mapping configuration input data frames structure arrays
    input_data = pd.DataFrame([[
        sqft, bedrooms, bathrooms, floors, age, parking, location_score, balcony, furnish_value, location_value
    ]], columns=['sqft', 'bedrooms', 'bathrooms', 'floors', 'age', 'parking', 'location_score', 'balcony', 'furnishing', 'location'])
    
    # Mathematical linear inference tracking price estimation execution cycle
    prediction = model.predict(input_data)[0]
    
    # Outcome rendering panel interface alert container logic dashboard parameters
    st.success(f"### 🎉 Estimated Market Valuation:")
    st.metric(label=f"Valuation Quote Around {location_name}", value=f"₹ {prediction:,.2f}")
    st.info("💡 Note: Idhu input trends criteria-vavachhu OpenStreetMap framework trace matrix generate panna live base analytics value pricing thaan.")
