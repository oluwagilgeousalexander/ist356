import streamlit as st
import pandas as pd
import numpy as np
<<<<<<< HEAD
import requests 
=======
import requests
>>>>>>> 3675e1bf6f97413e21695e2aadc0947aa4c9d2bb

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json"

response = requests.get(url)
json_data = response.json()

<<<<<<< HEAD
employees = pd.json_normalize(json_data,
                              record_path=["employees"],
                              meta= ["dept"])

st.dataframe(employees)
=======
employees = pd.json_normalize(json_data, 
                            record_path="employees", 
                              meta=["dept"]
                              ) #<== turn the right nobs

st.dataframe(employees)
>>>>>>> 3675e1bf6f97413e21695e2aadc0947aa4c9d2bb
