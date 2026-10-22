import streamlit as st
import pandas as pd
import numpy as np

import requests
from check_functions import clean_currency

checks = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv")
checks['total_amount_cleaned'] = checks['total amount of check'].apply(clean_currency)
# checks['gratuity_cleaned'] = checks['gratuity'].apply(clean_currency)
checks['gratuity_cleaned'] = checks.apply(lambda row: clean_currency(row['gratuity']), axis=1)

#engineer more columns 
checks['price_per_item'] = checks['total_amount_cleaned'] / checks['total items on check']
checks['price_per_person'] = checks['total_amount_cleaned'] / checks['party size']
checks['item_per_person'] = checks['total items on check'] / checks['party size'] 
# checks['gratuity percentage'] = checks['gratuity_cleaned'] / checks['total_amount_cleaned']

st.dataframe(checks)
