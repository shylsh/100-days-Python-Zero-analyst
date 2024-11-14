import streamlit as st 
import pandas as pd
import numpy as np

st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age: ", 0, 100, 25)

options = ['Python','Java','C++','JavaScript']
choice = st.selectbox("Select your favorite programming language: ", options)
st.write(f'Your favorite programming language is {choice}.')

st.write(f'Your age is {age}.')


data = {
    "Name":['John','Jane','Jake','Jill'],
    "Age":[28,24,35,40],
    "City":['New York','Los Angeles','Chicago','Houston']
}

df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader('Choose a csv file:',type ='csv')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)
    st.write(df1)