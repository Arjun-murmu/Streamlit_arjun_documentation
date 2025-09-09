import streamlit as st
import pandas as pd
import numpy as np
from numpy.random import default_rng as rng
import math


st.sidebar.markdown("### Page 3 ❄️")
st.write("### Create a table.")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df

##data point
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#E30606")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

st.write("### Here's are the generate random table : ")
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.bar_chart(df)

st.write("### Here's are the generate random table : ")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

#line chart
st.write("### Line chart : ")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


#Ploat Map
st.write("## Sambalpur cordinate")
map_data = pd.DataFrame(
    np.random.randn(50, 2) / [50, 50] + [21.4669, 83.9812],
    columns=['lat', 'lon'])

st.map(map_data)

# Sambalpur coordinates
st.write("## VSSUT")
vssut_coords = pd.DataFrame({
    'lat': [21.497299], #Latitude (Y-axis)
    'lon': [83.903999], # Longitude (X-axis)
    'name': ['VSSUT, Burla']
})
st.write("### 📍Location: ", vssut_coords['name'][0])
st.map(vssut_coords, zoom=15)

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option


#STANDARD NORMAL DISTRIBUTION TABLE

# Define Z values
z_rows = np.arange(-3.4, 3.5, 0.1)   # Row index
z_cols = np.arange(0.00, 0.10, 0.01) # Column index

# Function for standard normal CDF
def normal_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

# Create DataFrame for Z-table
table = pd.DataFrame(index=np.round(z_rows, 1),
                     columns=[f"{c:.2f}" for c in z_cols])

# Fill table with cumulative probabilities
for r in table.index:
    for c in table.columns:
        z_value = r + float(c)
        table.loc[r, c] = round(normal_cdf(z_value), 4)

table = table.astype(float)

# Display table
st.write("### Standard Normal Distribution Table")

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
st.dataframe(table)


