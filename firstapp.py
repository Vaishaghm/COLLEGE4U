import streamlit as st

st.title("Welcome to Streamlit")
st.write("This is your first Streamlit App!")

st.markdown("<h1 style='color:red;'>This is Red</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:green;'>This is Green</p>", unsafe_allow_html=True)

st.markdown("""
    <div style='background-color:yellow; padding:10px; border-radius:10px;'>
        This is a yellow box.
    </div>
""", unsafe_allow_html=True)

if st.button("Click Me"):
    st.write("You clicked the button!")

if st.button("Say Hello"):
    st.write("Hello, User!")

if st.button("Say Bye"):
    st.write("Goodbye, User!")

import streamlit as st

name = st.text_input("Enter your name:")
st.write("Your name is", name)

import streamlit as st

age = st.number_input("Enter your age:", 1, 100)
st.write("Your age is", age)

import streamlit as st

s = st.slider("Select one number",-100,100)
st.write("Your number is", s)


r=st.date_input('select date,')
st.write('today:',r)

import streamlit as st
import pandas as pd

data = pd.read_csv("date.csv")
st.write(data)

age_limit = st.number_input("Show records with Age >", 0)
filtered_data = data[data['Age'] > age_limit]
st.write("Filtered Data:")
st.dataframe(filtered_data)