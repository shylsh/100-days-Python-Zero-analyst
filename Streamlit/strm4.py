import streamlit as st
import pandas as pd
import numpy as np  
import time
import matplotlib.pyplot as plt

# pr = st.button("Click me")

# if pr == True:
#     st.write(time.time())
    
    
# def fn():
#     st.write(time.time())
    
# st.button("Click me",on_click=fn)

df = pd.DataFrame(
    np.random.randn(10,2),
    columns = ['col1','col2']
)
data = df.to_csv().encode('utf-8')
st.download_button(
    label='Download data',
    data=data,
    file_name = 'new_file.csv',
    mime='text/csv'
)


