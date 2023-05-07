from spider import Spider
from data_processor import Data_processor as dp
import numpy as np
import streamlit as st
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')



