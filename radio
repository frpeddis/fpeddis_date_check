import streamlit as st

st.set_page_config(page_title="Challenge Selector")

# Add a title and subtitle
st.title("A date is all you need to answer...")
st.subheader("A little challenge with easy math and memory")

# Add radio button to select between files
selected_file = st.radio("Select a file to execute:", ["date_guess.py", "selected_day.py"])

# Execute the selected file when the "Run" button is clicked
if st.button("Run"):
    if selected_file == "date_guess.py":
        # Execute code from date_guess.py
        exec(open("date_guess.py").read())
    elif selected_file == "selected_day.py":
        # Execute code from selected_day.py
        exec(open("selected_day.py").read())
