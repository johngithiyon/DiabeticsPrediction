import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("diabetics_model.pkl")

# Page setup
st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# CSS Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f7fa;
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        text-align: center;
        color: #2c3e50;
        font-weight: 700;
    }
    .css-1cpxqw2 {
        color: #34495e;
        font-size: 18px;
    }
    .stButton > button {
        background-color: #2980b9;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-size: 16px;
        transition: all 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background-color: #1abc9c;
        color: white;
    }
    .stNumberInput > div > div > input {
        border: 1px solid #bdc3c7;
        border-radius: 5px;
        padding: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🩺 Diabetes Prediction App")
st.write("Enter patient details below to predict the likelihood of diabetes:")

# Input fields
preg = st.number_input("Pregnancies", min_value=0, step=1)
plas = st.number_input("Plasma Glucose", min_value=0)
pres = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)

# Prediction button
if st.button("Predict"):
    input_data = np.array([[preg, plas, pres, skin]])
    prediction = model.predict(input_data)[0]

    st.markdown("---")
    if prediction == 1:
        st.error("⚠️ The patient is likely to have diabetes.")
    else:
        st.success("✅ The patient is not likely to have diabetes.")
