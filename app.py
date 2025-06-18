import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("diabetics_model.pkl")

st.title("🩺 Diabetes Prediction App")

st.write("Enter patient details below to predict the likelihood of diabetes:")

# Input fields
plas = st.number_input("Plasma Glucose", min_value=0)
pres = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)

# Prediction button
if st.button("Predict"):
    input_data = np.array([[plas, pres, skin]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ The patient is likely to have diabetes.")
    else:
        st.success("✅ The patient is not likely to have diabetes.")

