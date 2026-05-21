import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Student Marks Prediction")

# Sample Data
hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
marks = [10, 20, 30, 40, 50, 60, 70, 80]

# Train Model
model = LinearRegression()
model.fit(hours, marks)

# User Input
study_hours = st.slider("Select Study Hours", 1, 10)

# Prediction
prediction = model.predict([[study_hours]])

# Output
st.write(f"Predicted Marks: {prediction[0]:.2f}")
