import streamlit as st
import pandas as pd
import numpy as np
import requests

base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/bbplayers.csv"
months = ["jan", "feb", "mar", "apr"]
selected = months[3]
monthly_url = f"{base}?purchases={selected}.csv"
orders = pd.read_csv(monthly_url)
st.dataframe(orders)