import streamlit as st

nav = st.navigation([st.Page("home.py"), st.Page("planner.py")])
nav.run()