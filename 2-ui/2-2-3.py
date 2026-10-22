import streamlit as st

st.title("File Order Processor")

<<<<<<< HEAD
st.file_uploader("Select Order File", type=["txt"])

total = 0.0
count = 0

st.markdown('''
### File Processing Results
- Total: ${total}
- Count: {count}
''')
=======
# Innit
total = 0.0
count = 0

select_file = st.file_uploader("Select a file to process", type=["txt"])

if select_file is not None:
    content = select_file.read().decode("utf-8") 
    for line in content.splitlines():
        number = float(line.strip()) if line.strip() else 0.0
        total += number
        count += 1

st.markdown(f'''
### File Processing Results
- Total: ${total}
- Count: {count}
''')
>>>>>>> 3675e1bf6f97413e21695e2aadc0947aa4c9d2bb
