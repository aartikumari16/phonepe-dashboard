# case_study_1.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.header("📊 Case Study 1: Decoding Transaction Dynamics on PhonePe")

    # Load CSVs (can be moved to main app and passed as arguments too)
    txn_by_state = pd.read_csv("transaction_by_state.csv")
    quarterly_trend = pd.read_csv("quarterly_trend_by_state.csv")
    txn_by_category = pd.read_csv("transactions_by_state_category.csv")

    metric_type = st.radio("📊 Select Metric:", ["Total Transactions", "Total Amount"])
    metric_col = "total_transactions" if metric_type == "Total Transactions" else "total_amount"

    selected_states = st.multiselect("Select State(s):", sorted(txn_by_state["state"].unique()), default=["maharashtra", "karnataka", "telangana"])
    filtered_state_df = txn_by_state[txn_by_state["state"].isin(selected_states)].sort_values(by=metric_col, ascending=False)

    col1, col2 = st.columns(2)
    with col1:
        fig1, ax1 = plt.subplots(figsize=(6,5))
        sns.barplot(data=filtered_state_df, y='state', x=metric_col, palette="coolwarm", ax=ax1)
        ax1.set_title(f"{metric_type} by Selected States")
        ax1.set_xlabel(metric_type)
        st.pyplot(fig1)

    with col2:
        top5 = filtered_state_df.head(5)
        st.markdown("### 🔝 Top 5 Insights")
        for i, row in top5.iterrows():
            val = f"{int(row[metric_col]):,}" if metric_type == "Total Transactions" else f"₹{int(row[metric_col]):,}"
            st.markdown(f"**{row['state'].title()}**: {val}")

    st.markdown("---")
    st.markdown("### 📈 Quarterly Transaction Trend")

    quarterly = quarterly_trend[quarterly_trend['state'].isin(selected_states)].copy()
    quarterly['year_quarter'] = quarterly['year'].astype(str) + " Q" + quarterly['quarter'].astype(str)

    fig2, ax2 = plt.subplots(figsize=(10,5))
    sns.lineplot(data=quarterly, x="year_quarter", y="transactions", hue="state", marker="o", ax=ax2)
    ax2.set_title("Quarterly Transactions Over Time")
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    st.markdown("---")
    col5, col6 = st.columns(2)
    with col5:
        st.markdown("### 🧾 Transaction Category Breakdown")

        selected_category_state = st.selectbox("📍 Choose a state for category view:", selected_states)
        cat_filtered = txn_by_category[txn_by_category['state'] == selected_category_state]

        fig3, ax3 = plt.subplots(figsize=(6,5))
        sns.barplot(data=cat_filtered, x='transaction_type', y='total_transactions', palette='pastel', ax=ax3)
        ax3.set_title(f"Transaction Categories – {selected_category_state.title()}")
        plt.xticks(rotation=30)
        st.pyplot(fig3)

    with col6:
        st.markdown("### 🥧 India-Wide Category Share")

        pie_data = txn_by_category.groupby("transaction_type")["total_transactions"].sum().reset_index()

        fig4, ax4 = plt.subplots(figsize=(4,4))
        ax4.pie(pie_data["total_transactions"], labels=pie_data["transaction_type"], autopct='%1.1f%%', startangle=140, radius=0.7)
        ax4.set_title("Overall Transaction Share by Category")
        ax4.axis("equal")
        st.pyplot(fig4)

    st.markdown("---")
    st.markdown("### 🔥 Heatmap: State vs Category")

    pivot = txn_by_category.pivot(index='state', columns='transaction_type', values='total_transactions').fillna(0)
    fig5, ax5 = plt.subplots(figsize=(14,10))
    sns.heatmap(pivot, cmap="YlGnBu", linewidths=0.5, ax=ax5)
    ax5.set_title("Heatmap: Transaction Categories by State")
    st.pyplot(fig5)

    st.subheader("📊 Key Insights & Actionable Recommendations from Data Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔍 **Key Insights from Data Analysis & Visualizations**")

        st.markdown("#### **Top 10 States by Total Transactions & Amount**")
        st.markdown("- **Maharashtra** leads in total transactions, followed by **Karnataka** and **Telangana**.")
        st.markdown("- In terms of total transaction amount, **Telangana**, **Karnataka**, and **Maharashtra** dominate.")
        st.markdown("- **Andhra Pradesh**, **Uttar Pradesh**, **Rajasthan**, and **Madhya Pradesh** show high transaction volumes and amounts, reflecting growing digital adoption.")
        st.markdown("- **Odisha**, **Bihar**, and **West Bengal** rank lower but show emerging growth potential.")

        st.markdown("#### **Quarterly Transaction Trend in Top States**")
        st.markdown("- Consistent growth observed across all top-performing states.")
        st.markdown("- **Maharashtra** and **Karnataka** show steady, strong quarter-over-quarter growth.")
        st.markdown("- **Telangana** shows an increasing trend with slight quarterly fluctuations.")
        st.markdown("- Other states like **Andhra Pradesh** and **Uttar Pradesh** show moderate, steady growth.")

        st.markdown("#### **Transaction Categories Across Top States**")
        st.markdown("- **Merchant Payments** dominate across all top 5 states.")
        st.markdown("- **Peer-to-Peer (P2P) Payments** form the second-largest share.")
        st.markdown("- Categories like **Recharge & Bill Payments** and **Financial Services** are smaller but have growth potential.")

        st.markdown("#### **Transaction Split by Category (National Level)**")
        st.markdown("- **Merchant Payments:** 55.4% of all transactions.")
        st.markdown("- **Peer-to-Peer Payments:** 36.1%.")
        st.markdown("- **Recharge & Bill Payments:** 6.3%.")
        st.markdown("- Financial Services & Others: Marginal shares.")

        st.markdown("#### **Heatmap of Transaction Categories by State**")
        st.markdown("- High density of **Merchant & P2P Payments** in **Maharashtra**, **Karnataka**, **Telangana**, and **Madhya Pradesh**.")
        st.markdown("- Low activity in smaller states/UTs like **Arunachal Pradesh**, **Lakshadweep**, and **Andaman & Nicobar Islands**.")
        st.markdown("- Moderate usage in **Punjab**, **Rajasthan**, and **Uttar Pradesh**.")

    with col2:
        st.markdown("### 📝 **Actionable Recommendations**")

        st.markdown("#### **Expand in Top-Performing States**")
        st.markdown("- Focus on **Maharashtra**, **Karnataka**, **Telangana**, and **Andhra Pradesh**.")
        st.markdown("- Launch exclusive cashback offers and merchant tie-ups.")
        st.markdown("- Run localized campaigns to boost transaction frequency and volume.")

        st.markdown("#### **Strengthen Merchant Ecosystem**")
        st.markdown("- Introduce advanced merchant tools like analytics dashboards, credit lines, and loyalty programs.")
        st.markdown("- Incentivize merchants to encourage digital payments.")

        st.markdown("#### **Boost Under-Utilized Categories**")
        st.markdown("- Promote **Recharge & Bill Payments** and **Financial Services** through bundled offers & discounts.")
        st.markdown("- Educate users via targeted in-app promotions on category benefits.")

        st.markdown("#### **Penetrate Emerging Regions**")
        st.markdown("- Focus on states like **Uttar Pradesh**, **Rajasthan**, and **Madhya Pradesh** with:")
        st.markdown("  - Regional language marketing.")
        st.markdown("  - Partnerships with local governments for digital literacy drives.")
        st.markdown("  - Referral programs for first-time users.")

        st.markdown("#### **Address Low-Adoption States/UTs**")
        st.markdown("- Launch pilot programs in low-adoption areas with:")
        st.markdown("  - Zero-transaction fee incentives.")
        st.markdown("  - Special promotions during regional festivals.")
        st.markdown("  - Partnerships with local organizations for awareness drives.")

        st.markdown("#### **Quarterly Monitoring for Agile Strategy**")
        st.markdown("- Monitor quarterly growth closely.")
        st.markdown("- Adjust marketing budgets dynamically based on performance.")
        st.markdown("- Quickly address sharp dips or surges to optimize strategy.")

    st.markdown("---")

    st.markdown("### ✅ **Conclusion**")
    st.markdown("""
    This analysis highlights strong growth in key Indian states, particularly in **Merchant Payments** and **P2P Payments**.
    By leveraging these insights, PhonePe can:
    - Prioritize high-impact regions.
    - Unlock new market opportunities in emerging states.
    - Strengthen its position in low-performing areas through targeted strategies.
    """)

