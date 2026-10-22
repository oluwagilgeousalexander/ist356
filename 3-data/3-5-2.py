import streamlit as st
import pandas as pd 

exams = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv")


row = "Exam_Version" 
col = "Studied_In_Groups"
measure = "Completion_Time"

st.title("Universal Pivot Table")
pivot_table = exams.pivot_table(index = row,columns = col,values = measure,aggfunc = 'mean')
st.write(f"Pivot Table: {row} x {col} with {measure} as the measure")
st.dataframe(pivot_table)


row_col_values = ['Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Studied_In_Groups']
measure_col_values = exams[measure].unique()
st.title("Interactive Pivot Table")
row = st.selectbox("Select Row", options=exams.columns)
col = st.selectbox("Select Column", options=exams.columns)
measure = st.selectbox("Select Measure", options=exams.columns)

st.write(f"Interactive Pivot Table")
interactive_pivot_table = exams.pivot_table(index = row,columns = col,values = measure,aggfunc = 'mean')
st.dataframe(pivot_table)

# filter mean in measure in order to avoid NaN values in the pivot table
