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

# Set OpenAI API Key
openai.api_key = st.secrets["API_KEY"]

# Function to generate news
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

# Function to choose which code block to execute
def execute_choice(choice):
    if choice == 'First file content':
        execute_first_file_content()
    elif choice == 'Second file content':
        execute_second_file_content()

# Function to execute the first file content
def execute_first_file_content():
    # Your code from the first file goes here
    # ...
    
# Function to execute the second file content
def execute_second_file_content():
    # Your code from the second file goes here
    # ...
    

# Streamlit app title
st.title(":sunglasses: What day is it?")

# Radio buttons to choose which code block to execute
choice = st.radio(
    "Choose which code block to execute:",
    ('First file content', 'Second file content')
)

# Execute the selected code block
execute_choice(choice)
