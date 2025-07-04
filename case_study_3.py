# case_study_3.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.header("🛡️ Case Study 3: Insurance Engagement Analysis")

    st.markdown("PhonePe aims to analyze **insurance transactions** across various states and districts to understand "
                "the uptake of insurance services among users. This helps identify regional behavior and growth opportunities.")

    # Load data
    insurance_by_state = pd.read_csv("insurance_by_state.csv")
    insurance_by_category = pd.read_csv("insurance_by_category.csv")
    insurance_trend_by_state = pd.read_csv("insurance_trend_by_state.csv")
    top_districts_insurance = pd.read_csv("top_districts_insurance.csv")
    #state_insurance_amount = pd.read_csv("top_insurance_state.csv")

    # ------------------ Charts Row 1 ------------------
    col1, col2 = st.columns(2)

    with col1:
        top_states = insurance_by_state.sort_values(by='total_insurance_amount', ascending=False).head(10)
        fig1, ax1 = plt.subplots(figsize=(8,5))
        sns.barplot(data=top_states, y='state', x='total_insurance_amount', palette='viridis', ax=ax1)
        ax1.set_title("Top 10 States by Insurance Transaction Amount")
        ax1.set_xlabel("Total Insurance Amount (₹)")
        st.pyplot(fig1)

    with col2:
        
        top_districts = top_districts_insurance.sort_values(by='total_insurance_amount', ascending=False).head(10)
        fig2, ax2 = plt.subplots(figsize=(8,5))
        sns.barplot(data=top_districts, y='district', x='total_insurance_amount', palette='rocket', ax=ax2)
        ax2.set_title("Top 10 Districts by Insurance Transaction Amount")
        ax2.set_xlabel("Total Insurance Amount (₹)")
        st.pyplot(fig2)

    # ------------------ Charts Row 2 ------------------
    st.markdown("### 📊 Volume vs Value: State Insights")
    col3, col4 = st.columns(2)

    with col3:
        top_states_volume = insurance_by_state.sort_values(by='total_insurance_transactions', ascending=False).head(10)
        fig3, ax3 = plt.subplots(figsize=(8,5))
        sns.barplot(data=top_states_volume, y='state', x='total_insurance_transactions', palette='cubehelix', ax=ax3)
        ax3.set_title("Top 10 States by Insurance Transactions")
        ax3.set_xlabel("Total Transactions")
        st.pyplot(fig3)

    with col4:
        trend_df = insurance_trend_by_state.copy()
        top_trend_states = trend_df.groupby('state')['total_insurance_amount'].sum().nlargest(5).index.tolist()
        filtered_trend = trend_df[trend_df['state'].isin(top_trend_states)]
        filtered_trend['year'] = filtered_trend['year'].astype(str)

        fig4, ax4 = plt.subplots(figsize=(10,5))
        sns.lineplot(data=filtered_trend, x='year', y='total_insurance_amount', hue='state', marker='o', ax=ax4)
        ax4.set_title("📈 Yearly Insurance Transaction Trend – Top 5 States")
        ax4.set_ylabel("Total Insurance Amount (₹)")
        st.pyplot(fig4)

    # ------------------ District Heatmap ------------------
    st.markdown("### 🔥 District-Level Heatmap")

    top_districts = insurance_by_category.nlargest(25, "total_insurance_transactions")
    pivot = top_districts.pivot(index="district", columns="state", values="total_insurance_transactions").fillna(0)
    #pivot = insurance_by_category.pivot(index='district', columns='state', values='total_insurance_transactions').fillna(0)
    fig5, ax5 = plt.subplots(figsize=(14,10))
    sns.heatmap(pivot, cmap='YlGnBu', linewidths=0.3, linecolor='gray', ax=ax5)
    ax5.set_title("District-wise Insurance Transaction Heatmap (Top 25 Districts)")
    st.pyplot(fig5)

    # ------------------ Insights ------------------
    st.markdown("---")
    st.markdown("### 🧠 Key Insights")
    st.markdown("""
    - **Karnataka** and **Maharashtra** are leading both in insurance volume and value.
    - **Bengaluru Urban** district stands out in transaction value.
    - Consistent year-over-year growth reflects increasing insurance awareness.
    - Urban and metro districts dominate insurance adoption, while rural areas show untapped potential.
    """)
