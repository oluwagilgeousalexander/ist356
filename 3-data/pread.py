import streamlit as st
import pandas as pd
import numpy as np

st.title("Pandas Example")
st.write("This is a simple example of using Pandas with Streamlit.")



url = "https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv"
order = pd.read_csv(url, sep=",", skiprows=3)

st.dataframe(order)
st.write("Dataframe shape: ", order.shape)

col1= ['A', 'B', 'C', 'D', 'E', 'F', 'G']
col2 = ['B', 'G', 'A', 'F', 'C', 'D', 'E']
same = set(col1) == set(col2)

'''
processes vs referecence when analyzing data.
a gpa for example is a summary of a process, not a reference to the process itself.
while an examople of a reference to the process is a video of a presentation in a presetation class
'''