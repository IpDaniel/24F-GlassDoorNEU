import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.title("Question Bank")
st.write('')
st.write('')
st.write('### What would you like to do, Administrator')

# Can reuse this
if st.button('View Question Bank',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/01.1_View_All_Questions.py')

# Can reuse this
if st.button('Find Specific Question',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/01.2_View_Specific_Question.py')

# Can reuse this
if st.button ('Add New Question',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/11.1_Add_New_Question.py')

if st.button ('Delete Question',
              type='primary',
              use_container_width=True):
  st.switch_page('pages/41.1_Delete_Question.py')