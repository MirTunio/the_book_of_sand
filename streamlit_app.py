import streamlit as st
import requests
import pandas as pd

def dummy():
    test = "THIS IS A TEST"
    return pd.DataFrame({'A': [test], 'B': [test]})

dum = dummy()
st.table(dum)
