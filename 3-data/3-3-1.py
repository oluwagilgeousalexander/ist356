# create a data chart using a json file that does not have a header row and has a custom separator
import streamlit as st
import pandas as pd
import numpy as np
import requests

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json"
response = requests.get(url)
json_data = response.json()

# st.write(json_data)

# # loop over each key, create a dataframe and display it 
# for key in json_data.keys():
#     st.write(f"Dataframe for {key}:")
#     df = pd.DataFrame(json_data[key])
#     st.dataframe(df)

# dfs = []
# for key in json_data.keys():
#     df = pd.DataFrame(json_data[key])
#     df["department"] = key
#     dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)
st.write("Combined Dataframe:")
st.dataframe(combined_df)

filename = "3-data/data/combined_employees_data.json"
combined_df.to_json("combined_employees.json", orient="records", lines = True)

    