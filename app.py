import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Title
st.title("Student Marks Prediction Using Machine Learning")

# Dataset
data = {
    'Hours': [1,2,3,4,5,6,7,8,9,10],
    'Marks': [15,20,35,40,50,60,65,75,85,95]
}

df = pd.DataFrame(data)

# Features and labels
X = df[['Hours']]
y = df['Marks']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Error calculation
error = mean_absolute_error(y_test, y_pred)

st.subheader("Model Performance")
st.write(f"Mean Absolute Error: {error:.2f}")

# User Input
hours = st.slider("Select Study Hours", 1, 12)

# Predict
prediction = model.predict([[hours]])

st.subheader("Predicted Marks")
st.success(f"Expected Marks: {prediction[0]:.2f}")

# Graph
fig, ax = plt.subplots()

ax.scatter(df['Hours'], df['Marks'])
ax.plot(df['Hours'], model.predict(X))

ax.set_xlabel("Study Hours")
ax.set_ylabel("Marks")
ax.set_title("Hours vs Marks")

st.pyplot(fig)
