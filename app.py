import streamlit as st

st.title("Predictive Modeling Using Machine Learning")

hours = st.slider("Study Hours", 1, 10)

marks = hours * 10

st.write("Predicted Marks:", marks)
