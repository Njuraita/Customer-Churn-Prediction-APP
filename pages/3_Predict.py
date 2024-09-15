import streamlit as st
import joblib
import pandas as pd
import os
import datetime

st.set_page_config=(
    page_title='Predict',
    page_icon=':machine:',
    layout='wide'
)