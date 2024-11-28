import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import json

# dataframe #table #metric #json

# DataFrame
df = pd.DataFrame(np.random.randn(50, 20),columns= ["cols" +str(i) for i in range(1,21)])
# st.write(df)

# st.dataframe(df,width=200,height=1000)

# st.dataframe(np.random.randn(50,20))

# table

# st.table(df)

# metric

# st.metric("Temperature", "70 °F", "1.2 °F")
# st.metric("Wind", "9 mph", "-8%")
# st.metric("TCS Stock",value = "322",delta = "19.10")
# st.metric("TCS Stock",value = "322",delta = "19.10",delta_color="inverse")

# json

f = open(r"F:\DA\DATASET\Cricket Data\Total_Session_Run-main\Total_Session_Run-main\columns.json")
dt = json.load(f)
st.json(dt,expanded=False)

