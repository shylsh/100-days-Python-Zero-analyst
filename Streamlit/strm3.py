import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10,2), columns =['Prices','diff'])
# st.write(df)
st.line_chart(df, y = ['diff'])
st.area_chart(df, y =['Prices'])

fig,ax = plt.subplots()
# ax.scatter(np.arange(10),np.arange(10)**2)
# st.pyplot(fig)

ax.hist(np.random.randn(100),bins =10)
st.pyplot(fig)

places = pd.DataFrame({
    'lat':[19.07,28.64],
    'lon':[72.88,77.24]
})
st.map(places)