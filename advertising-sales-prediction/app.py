import streamlit as st
import pandas as pd
import pickle
import os

# --------------------------------
# Page
# --------------------------------

st.set_page_config(
    page_title="AdSales AI",
    page_icon="📈"
)

st.title("📈 AdSales AI")
st.write("Advertising Sales Prediction using Simple Linear Regression")

st.divider()

# --------------------------------
# Load Model
# --------------------------------

model_path = "model/advertising_model.pkl"

if not os.path.exists(model_path):
    st.error("Model not found. Please create model/advertising_model.pkl")
    st.stop()

with open(r"C:\Users\SHUBHAM\OneDrive\Desktop\machine learning\advertising-sales-prediction\linear_regressor_sales_model.pkl", "rb") as file:
    model = pickle.load(file)

# --------------------------------
# Load Dataset
# --------------------------------

df = pd.read_csv("Advertising.csv")

# --------------------------------
# Prediction
# --------------------------------

st.header("🔮 Sales Prediction")

tv = st.number_input(
    "Enter TV Advertising Budget",
    min_value=0.0,
    value=100.0,
    step=1.0
)

if st.button("Predict Sales"):

    input_data = pd.DataFrame({
        "TV": [tv]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Sales: {prediction[0]:.2f}"
    )

# --------------------------------
# Formula
# --------------------------------

st.header("📐 Mathematical Formula")

st.latex(
    r"Sales = 7.2925 + 0.0460 \times TV"
)

st.write("Where:")
st.write("- TV = TV Advertising Budget")
st.write("- Sales = Predicted Sales")

# --------------------------------
# Model Performance
# --------------------------------

st.header("📊 Model Performance")

col1, col2, col3 = st.columns(3)

col1.metric("R² Score", "0.6763")
col2.metric("MAE", "2.5054")
col3.metric("RMSE", "3.1916")

# --------------------------------
# Dataset
# --------------------------------

st.header("📁 Dataset")

st.write(
    f"Rows: {df.shape[0]} | Columns: {df.shape[1]}"
)

st.dataframe(
    df,
    use_container_width=True
)

# --------------------------------
# Footer
# --------------------------------

st.divider()

st.caption(
    "Built with Python, Pandas, Scikit-learn and Streamlit"
)