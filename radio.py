import streamlit as st
import importlib

st.set_page_config(page_title="File Selector")

# Add a title and subtitle
st.title("A date is all you need to answer...")
st.subheader("A little challenge with easy math and memory")

# Add radio button to select between files
selected_file = st.radio("Select a file to execute:", ["date_guess.py", "selected_day.py"])

# Execute the selected file when the "Run" button is clicked
if st.button("Run"):
    module_name = selected_file.replace(".py", "")
    try:
        module = importlib.import_module(module_name)
        function_name = "generate_news" if module_name == "date_guess" else "calculate_specific_date_magic"
        selected_function = getattr(module, function_name)

        if module_name == "date_guess":
            selected_date = selected_function()
            news_summary = generate_news(selected_date)
            st.header("Please verify, but according to ChatGPT in that period... ")
            st.write(news_summary)
        elif module_name == "selected_day":
            specific_date = st.date_input("Select a specific date:")
            if specific_date:
                selected_function(specific_date)
    except Exception as e:
        st.error(f"Error executing the script: {e}")
