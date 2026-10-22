import pandas as pd
import streamlit as st
import numpy as np


st.header("Pivot Melt Example")

exams = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv")
# Get average scores by section and exam version:
avg_scores_by_section_and_version = exams.groupby(by=['Class_Section', 'Exam_Version']).agg({'Student_Score': 'mean'})

# add section and exam version back to dataframe
avg_scores_by_section_and_version['Class_Section'] = avg_scores_by_section_and_version.index.get_level_values('Class_Section')
avg_scores_by_section_and_version['Exam_Version'] = avg_scores_by_section_and_version.index.get_level_values('Exam_Version')
# reset the index
avg_scores_by_section_and_version = avg_scores_by_section_and_version.reset_index(drop=True)
#rename the Student_score to average score
avg_scores_by_section_and_version =  avg_scores_by_section_and_version.rename(columns={'Student_Score': 'Average_Score'})
#reorder the columns
avg_scores_by_section_and_version = avg_scores_by_section_and_version[['Class_Section', 'Exam_Version', 'Average_Score']]

#show
avg_scores_by_section_and_version

st.dataframe(avg_scores_by_section_and_version)

# pivot
pivoted = avg_scores_by_section_and_version.pivot(
    index='Class_Section', 
    columns='Exam_Version', 
    values='Average_Score')
st.dataframe(pivoted)

melted = pivoted.reset_index().melt(
    id_vars='Class_Section',
    value_name='Average_Score', 
    var_name='Exam_Version')
st.dataframe(melted)

st.title("Pivot Table Example")
# pivot table exams in row: Class_Section, in columns Exam_Version, values Student_Score, aggfunc mean
pivot_table = exams.pivot_table(
    index = 'Class_Section',
    columns = 'Exam_Version',
    values = 'Student_Score',
    aggfunc = 'mean'
)
st.dataframe(pivot_table)

# use case for pivot/unpivot:

# take values in one column and make them several columns => pivot
# normally you would do this to make the data easier to read and analyze
# done one discreet values rather than a continuous range of values

# take values in columns and represent them in rows => unpivot/melt
