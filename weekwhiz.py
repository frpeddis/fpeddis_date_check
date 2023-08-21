import random
import calendar
import streamlit as st
from datetime import datetime, timedelta
import openai
import time
import streamlit.components.v1 as com
import requests
from PIL import Image
from io import BytesIO
import pandas as pd

openai.api_key = st.secrets["API_KEY"]
st.set_page_config(page_title="🌀 Day Guess - F Peddis")

# Add radio button to select between random date and specific date
date_selection = st.radio("Select a date option:", ["Random Date", "Specific Date"])

if date_selection == "Random Date":
    random_date = calculate_random_date()
else:
    specific_date = st.date_input("Select a specific date:")
    random_date = specific_date if specific_date else datetime.now()

# Rest of the code remains the same

# Checkbox to toggle image display
show_images = st.checkbox("Show me how to calculate !")

# Rest of the code remains the same

# Calculate time taken
if not st.session_state.check_pressed:
    time_taken = (datetime.now() - st.session_state.start_time).total_seconds()
    display_time_taken = False
else:
    time_taken = st.session_state.time_taken
    display_time_taken = True

# Rest of the code remains the same

# Display the date in the format dd-mmm-yyyy
description = "**Selected Date:**"
value = "**" + random_date.strftime("%d-%b-%Y") + "**"
st.markdown(f"{description} {value}")
selected_date = random_date.strftime("%d-%b-%Y")

# Rest of the code remains the same

# Calculate time taken to make the selection
st.session_state.time_taken = (datetime.now() - st.session_state.start_time).total_seconds()
time_taken = st.session_state.time_taken
display_time_taken = True

# Show the amount of seconds taken
if display_time_taken:
    st.write(":hourglass: Time taken to check:", round(time_taken, 2), "seconds")

    if st.button("In that period..."):
        news_summary = generate_news(selected_date)
        st.header("Please verify, but according to ChatGPT in that period... ")
        st.write(news_summary)
