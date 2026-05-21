import streamlit as st

st.title("Predictive Modeling Using Machine Learning")

hours = st.slider("Enter Study Hours", 1, 10)

predicted_marks = hours * 10

st.write("Predicted Marks:", predicted_marks)

st.success("Machine Learning Prediction Successful")
