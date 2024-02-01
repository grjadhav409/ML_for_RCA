import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import joblib

# Load label encoder and model
label_encoder = joblib.load('label_encoder.joblib')
model = load_model('model.h5')

# Streamlit app
st.title("Root Cause Prediction App")

# Create tabs
selected_tab = st.sidebar.selectbox("Select a tab", ["Home", "About App"])

# Home 
if selected_tab == "Home":
    st.sidebar.header("Input Parameters")
    cpu_load = st.sidebar.slider("CPU_LOAD", 0, 1, 1)
    memory_load = st.sidebar.slider("MEMORY_LOAD", 0, 1, 0)
    delay = st.sidebar.slider("DELAY", 0, 1, 0)
    error_1000 = st.sidebar.slider("ERROR_1000", 0, 1, 0)
    error_1001 = st.sidebar.slider("ERROR_1001", 0, 1, 0)
    error_1002 = st.sidebar.slider("ERROR_1002", 0, 1, 0)
    error_1003 = st.sidebar.slider("ERROR_1003", 0, 1, 0)

    if st.button("Predict"):
        input_data = np.array([[cpu_load, memory_load, delay, error_1000, error_1001, error_1002, error_1003]])
        prediction = np.argmax(model.predict(input_data), axis=1)
        predicted_root_cause = label_encoder.inverse_transform(prediction)

        st.success(f"Predicted ROOT_CAUSE:")
        st.error(f"{predicted_root_cause[0]}")

# About 
elif selected_tab == "About App":
    st.header("About Root Cause Prediction App")

    st.image("Screenshot 2023-12-28 at 9.41.50 PM.png", caption="Caption for Image 1", use_column_width=True)
    st.image("Screenshot 2023-12-28 at 9.41.50 PM.png", caption="Caption for Image 2", use_column_width=True)

    st.markdown("""
    This is a Streamlit app for predicting root causes based on input parameters. 
    Add more information about the app here.
    """)

    st.sidebar.header("Creators Information")
    st.sidebar.markdown("Created by:")
    st.sidebar.markdown("[Creator 1](your_linkedin_profile_1)")
    st.sidebar.markdown("[Creator 2](your_linkedin_profile_2)")
