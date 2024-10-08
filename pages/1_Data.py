import streamlit as st
import pandas as pd


st.title("Data page")

#Load data

st.cache_data(persist=True)
def load_data():
    data = pd.read_csv('churn_prime.csv')
    return data

st.dataframe(load_data())
