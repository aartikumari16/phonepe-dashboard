# app.py
import streamlit as st
import case_study_1
import case_study_2
import case_study_3
import case_study_4
import case_study_5

st.set_page_config(page_title="📊 PhonePe Dashboard", layout="wide")
st.title("📱 PhonePe Data Analysis – Business Case Studies")

# Define tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Case Study 1: Decoding Transaction Dynamics on PhonePe",
    "🏢 Case Study 2: Device Dominance and User Engagement Analysis",
    "📍 Case Study 3: Insurance Engagement Analysis",
    "💳 Case Study 4: User Engagement and Growth Strategy",
    "📈 Case Study 5: Insurance Transactions Analysis"
])

with tab1:
    case_study_1.run()

with tab2:
    case_study_2.run()

with tab3:
    case_study_3.run()

with tab4:
    case_study_4.run()

with tab5:
    case_study_5.run()
