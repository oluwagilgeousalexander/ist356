import streamlit as st

st.title("Order Amount Accumilator")

# initialize into session state 
if 'total_order' not in st.session_state:
    st.session_state.total_order = 0.0
    st.session_state.order_history = []

amount = st.number_input(
    "Enter an amount", min_value=0.0)
add_to_order = st.button(
    "Add to order", type= "primary")
clear_order = st.button(
    "Clear Order", type = "secondary")

# order accumulation logic
if add_to_order:
    st.session_state.total_order += amount
    st.session_state.order_history.append(amount)

st.text(
    f"Total Order: {st.session_state.total_order}")
    

