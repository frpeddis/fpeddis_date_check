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

def generate_news(selected_date):
    prompt = f"What happens on {selected_date}?\nGive me a good news simply with an initial 😄, a neutral news simply with an initial 😐, and a bad news simply with an initial 😔. Do not mention if it is good, neutral or bad news, just use the icons. Do not mention any date in your answer. jump a line forevery news. Insert related Wikipedia links."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )

    return response.choices[0].text.strip()

# Function to calculate a random date
def calculate_random_date():
    start_date = datetime(1582, 10, 15)
    end_date = datetime(2099, 12, 31)
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

# Checkbox to toggle image display
show_images = st.checkbox("Show me how to calculate !")

# Streamlit app title
st.title(":sunglasses: What day is it?")
st.session_state.check_pressed = False

# Initialize start_time in session state
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()

# Add radio button to select between random date and specific date
date_selection = st.radio("Select a date option:", ["Random Date", "Specific Date"])

if date_selection == "Random Date":
    random_date = calculate_random_date()
else:
    specific_date = st.date_input("Select a specific date:")
    random_date = specific_date if specific_date else datetime.now()

# Display the date in the format dd-mmm-yyyy
description = "**Selected Date:**"
value = "**" + random_date.strftime("%d-%b-%Y") + "**"
st.markdown(f"{description} {value}")
selected_date = random_date.strftime("%d-%b-%Y")

if date_selection == "Specific Date":
    # Display magic calculation steps for specific date
    
    # Step 1: User selects a date
    selected_date = specific_date
    
    if selected_date:
        st.write("That's why: consider the date ", selected_date.strftime("%d-%b-%Y"))
        
        # Step 2: Take the last 2 digits of the year
        year_last_2_digits = selected_date.year % 100
        st.write(year_last_2_digits, ": Last 2 digits of the year")
        
        # Step 3: Divide the year number by 4 and add it
        year_divided_by_4 = year_last_2_digits // 4
        st.write(year_divided_by_4, ": Integer part of year YY divided by 4")
        subtotal = year_last_2_digits + year_divided_by_4
        
        # Step 4: Add the "Century Correction"
        century_correction_table = {
            "Century": [1500, 1600, 1700, 1800, 1900, 2000],
            "Correction": [0, 6, 4, 2, 0, -1]
        }
        century = (selected_date.year // 100) * 100
        century_correction_value = century_correction_table["Correction"][century_correction_table["Century"].index(century)]
        st.write(century_correction_value, ": Century Correction")
        subtotal += century_correction_value
        
        # Step 5: Add the "Month Coefficient"
        month_coefficients = {
            "January": 1 if not (selected_date.year % 4 == 0 and selected_date.month <= 2) else 0,
            "February": 4 if not (selected_date.year % 4 == 0 and selected_date.month <= 2) else 3,
            "March": 4, "April": 0, "May": 2, "June": 5,
            "July": 0, "August": 3, "September": 6,
            "October": 1, "November": 4, "December": 6
        }
        month = selected_date.strftime("%B")
        month_coefficient = month_coefficients[month]
        st.write(month_coefficient, ": Month Coefficient")
        subtotal += month_coefficient
        
        # Step 6: Add the day of the month
        day_of_month = selected_date.day
        st.write(day_of_month, ": Day of the month")
        subtotal += day_of_month
        
        # Step 7: Divide the subtotal by 7 and find the remainder
        remainder = subtotal % 7
        st.write(":point_right: Remainder after dividing ", subtotal, " by 7:", f"<span style='font-size:18px; font-weight:bold;'>{remainder}</span>", unsafe_allow_html=True)
        
        # Display calculated string
        calculated_string = f"{year_last_2_digits} + {year_divided_by_4} + {century_correction_value} + {month_coefficient} + {day_of_month}"
        st.write(":point_right: Magic Sum: ", calculated_string, " = ", f"<span style='font-size:18px; font-weight:bold;'>{subtotal}</span>", unsafe_allow_html=True)

# Prompt the user to select the day of the week from a dropdown list
selected_day_of_week = st.selectbox("Select the day of the week:", list(calendar.day_name))

# Add a "Check" button to confirm the selection
check_button = st.button("Check")

if check_button:
    st.session_state.check_pressed = True

    # Confirm the day of the week selected by the user
    day_of_week = calendar.day_name[random_date.weekday()]

    if selected_day_of_week == day_of_week:
        st.balloons()
        st.success(day_of_week + " is OK! :thumbsup:")
    else:
        st.error(day_of_week + " is the right day! :coffee: Try again...")
        com.iframe("https://lottie.host/?file=380d3ff9-0c30-4a96-b25b-7eeb8868bfeb/vnvhMZFQ8j.json")
        
# Calculate time taken
if not st.session_state.check_pressed:
    time_taken = (datetime.now() - st.session_state.start_time).total_seconds()
    display_time_taken = False
else:
    time_taken = st.session_state.time_taken
    display_time_taken = True

# Show the amount of seconds taken
if display_time_taken:
    st.write(":hourglass: Time taken to check:", round(time_taken, 2), "seconds")

    if st.button("In that period..."):
        news_summary = generate_news(selected_date)
        st.header("Please verify, but according to ChatGPT in that period... ")
        st.write(news_summary)
