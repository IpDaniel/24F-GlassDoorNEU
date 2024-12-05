import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.title(f"How would you like to access Interview Prep?")
st.write('')
st.write('')
st.write('### How can we help you today?')

# We might want to unimplement this feature because it does not make sense to view all interview preps
if st.button('View All Interview Preps',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/02.1_View_All_Interview_Prep.py')

# Makes more sense to view your own interview preps
if st.button('View Your Interview Preps',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/02.2_View_Your_Interview_Prep.py')

if st.button('View Interview Prep by ID',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/02.3_View_Specific_Interview_Prep.py')

if st.button('Cancel Interview Prep',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/02.4_Cancel_Interview_Prep.py')

