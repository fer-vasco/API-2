import streamlit as st
import random

num_aleatorio = random.randint(0,9)

st.title('Hello, World!')
st.write('Welcome to my Streamlit app!')
st.write(num_aleatorio)

