import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("diabetics_model.pkl")

# Page config
st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# Background styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f8ff;
        padding: 20px;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
        color: #333;
        text-align: center;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🩺 Diabetes Prediction App</div>', unsafe_allow_html=True)
st.write("Fill in the following patient health indicators:")

# Input fields
col1, col2 = st.columns(2)
with col1:
    preg = st.number_input("Pregnancies", min_value=0, step=1)
    plas = st.number_input("Plasma Glucose", min_value=0)
    skin = st.number_input("Skin Thickness", min_value=0)
    age = st.number_input("Age", min_value=1)
with col2:
    pres = st.number_input("Blood Pressure", min_value=0)
    insu = st.number_input("Insulin Level", min_value=0)
    mass = st.number_input("BMI", min_value=0.0, format="%.1f")
    pedi = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")

# Prediction
if st.button("Predict"):
    input_data = np.array([[preg, plas, pres, skin, insu, mass, pedi, age]])
    prediction = model.predict(input_data)[0]

    st.markdown("---")
    if prediction == 1:
        st.error("⚠️ **The patient is likely to have diabetes. Please consult a doctor.**")
    else:
        st.success("✅ **The patient is not likely to have diabetes. Keep up the good health!**")
