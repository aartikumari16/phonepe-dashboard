# app.py
import streamlit as st
import case_study_1
import case_study_2

st.set_page_config(page_title="📊 PhonePe Dashboard", layout="wide")
st.title("📱 PhonePe Data Analysis – Business Case Studies")

# Define tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Case Study 1: Decoding Transaction Dynamics on PhonePe",
    "🏢 Case Study 2: Device Dominance and User Engagement Analysis",
    "📍 Case Study 3 – [Title]",
    "💳 Case Study 4 – [Title]",
    "📈 Case Study 5 – [Title]"
])

with tab1:
    case_study_1.run()

with tab2:
    case_study_2.run()

with tab3:
    st.info("📍 Case Study 3 will appear here once prepared.")

with tab4:
    st.info("📍 Case Study 4 will appear here once prepared.")

with tab5:
    st.info("📍 Case Study 5 will appear here once prepared.")
