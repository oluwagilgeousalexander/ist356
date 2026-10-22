import streamlit as st
import pandas as pd
import datetime

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/"

roster = pd.read_csv(url + "roster.csv")


# concatanate data files. whenever you concatenate data files, make sure to add linear indexing to the dataframes. This is because the index of the dataframes will be the same, and when you concatenate them, the index will be duplicated. This can cause issues when you try to access the data later on.
#import all poles 
start_date = datetime.date(2024, 1, 8)
class_split = datetime.timedelta(days=7)

polls = []
for i in range(4):
    file_date = start_date + i*class_split
    file_date_string = datetime.datetime.strftime(file_date, "%Y-%m-%d")
    filename = f"poll-responses-{file_date_string}.csv"
    poll = pd.read_csv(url + filename)
    poll["poll_date"] = file_date
    poll["poll_filename"] = filename
    polls.append(poll)

polls_concat = pd.concat(polls)

# merge the roster with the polls_concat
polls_merged = pd.merge(roster, polls_concat, how="left", left_on="netid", right_on="student_id")

#use pibot_table so roster data is in the row, and poll_date values are in the columns. 
#values are the count of poll responses
polls_pivot = polls_merged.pivot_table(index=["netid", "name"], columns="poll_date", values="poll_num", aggfunc="count")

# now melt pivot table so that poll_date is in a column
polls_melted = polls_pivot.reset_index().melt(id_vars=["netid", "name"], 
                                              var_name="poll_date", value_name="response_count")

st.dataframe(polls_pivot)
st.dataframe(polls_melted)