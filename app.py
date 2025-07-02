# app.py

import streamlit as st
from case_study_1 import render_case_study_1

st.set_page_config(page_title="📊 PhonePe Dashboard", layout="wide")
st.title("📱 PhonePe Data Analysis – Business Case Studies")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Case Study 1 – Transaction Dynamics",
    "🏢 Case Study 2 – [Title]",
    "📍 Case Study 3 – [Title]",
    "💳 Case Study 4 – [Title]",
    "📈 Case Study 5 – [Title]"
])

with tab1:
    render_case_study_1()

with tab2:
    st.info("📍 Case Study 2 will appear here once prepared.")

# ... similarly for tab3, tab4, tab5
