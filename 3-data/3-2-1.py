import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log"

<<<<<<< HEAD
st.title("Software: Microsoft Internet Information Services 8.5")




data = pd.read_csv(url, sep = " ", skiprows = 3)
=======
data = pd.read_csv(url, sep=" ", skiprows=3) # <===

>>>>>>> 3675e1bf6f97413e21695e2aadc0947aa4c9d2bb
st.dataframe(data)