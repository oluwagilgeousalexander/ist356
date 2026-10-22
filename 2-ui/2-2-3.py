import streamlit as st

st.title("File Order Processor")

st.file_uploader("Select Order File", type=["txt"])

total = 0.0
count = 0

st.markdown('''
### File Processing Results
- Total: ${total}
- Count: {count}
''')