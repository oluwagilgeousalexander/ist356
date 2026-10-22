import streamlit as st

from figures import *
'''
output = df1.apply(lambda row: row['COLB'] + row['COLC'], 
                   axis=1).sum()
st.write(output)
'''
# math + naan= naan, dont treat naan as zero 

# #output = pd.merge(df1, df2,
#                   how = "inner",
#                   left_on = "COLA",
#                   right_on = "COLE"
#                   )
# st.write(output)

'''cola and cold do not work because they are different data types. cola is a string and cold is an integer.
cola and cole do work because they are both strings.
mergeing data frames require the two dataframes to have the same data type for the columns you are merging on.
unlike SQL, pandas does not automatically convert data types for you. You have to make sure the data types match before merging. 
unlike merge, concat does not require the data types to match. Concat will just stack the dataframes on top of each other, regardless of the data types.
it is important to add a column to the dataframes you are concatenating/appending to keep track of which dataframe the data came from in most cases.
this is because when you concatenate dataframes, the index of the dataframes will be the same, and when you concatenate them, the index will be duplicated. 
This can cause issues when you try to access the data later on.'''

df2['COLX']  = 7
df2['CoLY'] = df2['COLD'] * 7
# better way
df2['COLY'] = df2.apply(lambda x:
                         x['COLD'] * 7, axis=1)

df8.pivot(index = "COLA", columns = "COLB", values = "COLC")