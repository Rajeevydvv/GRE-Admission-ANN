import streamlit as st
import tensorflow as tf
import numpy as np
import pickle

# Load Model
model = tf.keras.models.load_model(
    "model.h5",
    compile=False
)
# Load Scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.set_page_config(
    page_title="GRE Admission Predictor",
    page_icon="🎓"
)

st.title("🎓 GRE Admission Prediction using ANN")

st.write(
    "Enter applicant details to estimate admission probability."
)

# Inputs
gre_score = st.slider(
    "GRE Score",
    min_value=260,
    max_value=340,
    value=320
)

toefl_score = st.slider(
    "TOEFL Score",
    min_value=0,
    max_value=120,
    value=100
)

university_rating = st.slider(
    "University Rating",
    min_value=1,
    max_value=5,
    value=3
)

sop = st.slider(
    "SOP Strength",
    min_value=1.0,
    max_value=5.0,
    value=3.0,
    step=0.5
)

lor = st.slider(
    "LOR Strength",
    min_value=1.0,
    max_value=5.0,
    value=3.0,
    step=0.5
)

cgpa = st.slider(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=8.0,
    step=0.1
)

research = st.selectbox(
    "Research Experience",
    [0, 1]
)

if st.button("Predict Admission Chance"):

    input_data = np.array([[
        gre_score,
        toefl_score,
        university_rating,
        sop,
        lor,
        cgpa,
        research
    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(
        input_scaled,
        verbose=0
    )

    chance = float(prediction[0][0])

    chance = max(0, min(1, chance))

    st.success(
        f"Estimated Chance of Admission: {chance * 100:.2f}%"
    )