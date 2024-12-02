import streamlit as st
import pandas as pd
import numpy as np

# Title and Description
st.title("Welcome to My Streamlit App")
st.write("This is a basic Streamlit application demonstrating its features.")

# Interactive Widgets
st.header("Input Section")
name = st.text_input("What's your name?")
age = st.number_input("What's your age?", min_value=0, max_value=120)

if name:
    st.write(f"Hello, {name}! You are {age} years old.")

# Data Visualization
st.header("Data Visualization Example")
data = np.random.randn(10, 2)
df = pd.DataFrame(data, columns=['Column A', 'Column B'])

st.write("Randomly Generated Data:")
st.write(df)

st.line_chart(df)

# Sidebar
st.sidebar.header("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "About"])

if selection == "About":
    st.sidebar.write("This app was built with Streamlit!")
