#Author: Francesco Peddis with ChatGPT

import streamlit as st
import streamlit.components.v1 as com
import time

st.set_page_config(page_title="🌀 Guess the Weekday!")

st.subheader("↖️ Your Calendar Challenge on the upper left sidebar")

com.iframe("https://lottie.host/?file=5a47a9d0-e7b0-492a-a32c-dd53d0fbfd5b/NaMYqV899B.json")

st.title("Welcome!!!  :sunglasses:")
#st.header("Guess the **weekday** for **any date!**")

text = "Guess the weekday for any date!"


t = st.empty()
for i in range(len(text) + 1):
    t.markdown("## %s" % text[0:i])
    time.sleep(0.1)

st.subheader("With a little practice you can calculate it in your head... ") 


 
st.sidebar.success("Select your challenge ")
