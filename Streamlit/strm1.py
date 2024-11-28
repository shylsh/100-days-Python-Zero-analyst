import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"F:\Github\100-days-Python-Zero-analyst\day16_emp_data.csv")

dc ={"a":10,"b":20}
# st.write(dc)

fig, ax = plt.subplots()
ax.scatter(np.arange(5),np.arange(5)**2)
# st.write(fig)
# df

# st.title("This is the title")
# st.header("Header")
# st.subheader("subheader")


code = '''def func():
    print('hello')'''
st.code(code,language='python')

