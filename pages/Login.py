import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)


# Login page
name, authentication_status, username = authenticator.login('main')
if authentication_status:
   st.write(f'Welcome {name}')
elif authentication_status == False:
   st.error('Username or password is incorrect')
elif authentication_status == None:
   st.warning('Please enter your username and password')


