import streamlit as st
import pickle

# Load model
with open("exam_score_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page settings
st.set_page_config(
    page_title="Exam Score Predictor",
    page_icon="📚",
    layout="centered"
)

# Title
st.title("📚 Student Exam Score Predictor")
st.write("Predict exam score based on study hours using Simple Linear Regression.")

st.divider()

# Input
study_hours = st.number_input(
    "Enter Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

# Prediction
if st.button("Predict Exam Score", type="primary"):

    prediction = model.predict([[study_hours]])[0]

    st.success(f"Predicted Exam Score: **{prediction:.2f}**")

    st.info(
        f"A student studying **{study_hours:.1f} hours** "
        f"is predicted to score approximately **{prediction:.2f} marks**."
    )

st.divider()

st.caption("Model: Simple Linear Regression | Feature: Study Hours")