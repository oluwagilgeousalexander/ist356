import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log"

st.title("Software: Microsoft Internet Information Services 8.5")




data = pd.read_csv(url, sep = " ", skiprows = 3)
st.dataframe(data)