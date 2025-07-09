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


    st.subheader("🛡️ Insurance Transaction Insights & Actionable Recommendations")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔍 **Key Insights from Data Analysis & Visualizations**")

        st.markdown("#### **Top 10 States by Insurance Transaction Amount**")
        st.markdown("- **Karnataka** and **Maharashtra** lead significantly in total insurance transaction amounts.")
        st.markdown("- Other top states include **Uttar Pradesh**, **Tamil Nadu**, and **Kerala**.")
        st.markdown("- Southern states (**Karnataka**, **Tamil Nadu**, **Kerala**, **Telangana**) dominate the insurance market.")
        st.markdown("- States like **West Bengal**, **Rajasthan**, **Haryana**, and **Delhi** also rank in the top 10 but with comparatively lower amounts.")

        st.markdown("#### **Top 10 States by Insurance Transaction Count**")
        st.markdown("- **Karnataka** leads, followed by **Maharashtra** and **Tamil Nadu** in transaction count.")
        st.markdown("- **Uttar Pradesh** shows high transaction counts but slightly lower total amounts, suggesting smaller transaction values per user.")
        st.markdown("- Other key states: **Telangana**, **West Bengal**, **Kerala**, **Andhra Pradesh**, **Delhi**, and **Rajasthan**.")

        st.markdown("#### **Top 10 Districts by Insurance Transaction Amount**")
        st.markdown("- **Bengaluru Urban (Karnataka)** dominates by a wide margin.")
        st.markdown("- Other high-value districts include:")
        st.markdown("  - **Pune, Thane, Mumbai Suburban** (Maharashtra)")
        st.markdown("  - **Chennai** (Tamil Nadu)")
        st.markdown("  - **Medchal Malkajgiri & Rangareddy** (Telangana)")
        st.markdown("  - **Jaipur** (Rajasthan)")
        st.markdown("  - **Ernakulam** (Kerala)")
        st.markdown("  - **Gurugram** (Haryana)")
        st.markdown("- High engagement in metro/urban districts.")

        st.markdown("#### **Yearly Insurance Transaction Trend – Top 5 States**")
        st.markdown("- Strong upward trend from 2020 to 2024 across all top 5 states.")
        st.markdown("- **Karnataka** leads in both growth rate and volume, followed by **Maharashtra** and **Tamil Nadu**.")
        st.markdown("- Consistent growth indicates increasing insurance adoption.")

        st.markdown("#### **District-wise Insurance Transaction Heatmap (Top 25 Districts)**")
        st.markdown("- Metro/urban districts dominate: **Bengaluru Urban, Pune, Thane, Chennai, Medchal Malkajgiri, Rangareddy, Mumbai Suburban, Jaipur, Ernakulam**.")
        st.markdown("- Minimal activity in several districts of **Uttar Pradesh**, **Bihar**, and **Madhya Pradesh**, signaling untapped potential.")

    with col2:
        st.markdown("### 📝 **Actionable Recommendations**")

        st.markdown("#### **Leverage High-Performing States & Districts**")
        st.markdown("- Strengthen partnerships and expand insurance offerings in top-performing states like **Karnataka, Maharashtra, and Tamil Nadu**.")
        st.markdown("- Launch premium insurance products or bundled services targeting high-transaction districts such as **Bengaluru Urban, Pune, and Chennai**.")

        st.markdown("#### **Target Low Adoption Regions**")
        st.markdown("- Focus on under-penetrated yet populous regions like **Uttar Pradesh, Bihar, Rajasthan, and Madhya Pradesh** with:")
        st.markdown("  - Affordable micro-insurance products.")
        st.markdown("  - Simplified onboarding and vernacular language support.")
        st.markdown("  - Awareness campaigns highlighting digital insurance benefits.")

        st.markdown("#### **Optimize for High-Transaction but Low-Amount Regions**")
        st.markdown("- Identify users in states like **Uttar Pradesh** with high transaction counts but lower values.")
        st.markdown("- Offer premium upgrades or bundled plans to increase average transaction amounts.")

        st.markdown("#### **Regional Campaign Customization**")
        st.markdown("- Create hyperlocal marketing strategies focusing on urban vs. rural dynamics:")
        st.markdown("  - **Urban/Metro Users:** Promote advanced plans, quick claim processes, and high-value policies.")
        st.markdown("  - **Rural/Semi-Urban Users:** Focus on low-cost protection plans, government-linked schemes, and simplified purchase journeys.")

        st.markdown("#### **Quarterly Monitoring & Growth Acceleration**")
        st.markdown("- Monitor quarterly insurance trends to spot emerging markets.")
        st.markdown("- Dynamically adjust marketing and operational strategies based on regional data.")

    st.markdown("---")

    st.markdown("### ✅ **Conclusion**")
    st.markdown("""
    This insurance transaction analysis highlights clear regional disparities in adoption.
    While metros such as **Bengaluru Urban** and **Pune** dominate the market, many populous districts remain under-tapped.
    By leveraging targeted marketing, affordable products, and regionalized campaigns, PhonePe can unlock significant growth potential in the insurance segment.
    """)
