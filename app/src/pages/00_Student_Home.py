import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title(f"Wecome to the Student Home Page, {st.session_state['first_name']}!")
st.write('')
st.write('')
st.write('### How can we help you today?')

if st.button('View Question Bank',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/01_Question_Bank.py')


if st.button('View Interview Prep Sessions ',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/02_Interview_Prep.py')

if st.button('View Peer Stories',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/03_Peer_Stories.py')

if st.button('View Companies',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/04_Companies.py')

if st.button('View Analytics',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/05_Analytics.py')