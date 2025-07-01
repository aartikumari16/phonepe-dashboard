import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="📊 PhonePe Dashboard", layout="wide")
st.title("📱 PhonePe Data Analysis – Business Case Studies")

# Load data
txn_by_state = pd.read_csv("transaction_by_state.csv")
quarterly_trend = pd.read_csv("quarterly_trend_by_state.csv")
txn_by_category = pd.read_csv("transactions_by_state_category.csv")

# Define tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Case Study 1 – Transaction Dynamics",
    "🏢 Case Study 2 – [Title]",
    "📍 Case Study 3 – [Title]",
    "💳 Case Study 4 – [Title]",
    "📈 Case Study 5 – [Title]"
])

# ---------------- CASE STUDY 1 ---------------------
with tab1:
    st.header("📊 Case Study 1: Decoding Transaction Dynamics on PhonePe")

    metric_type = st.radio("📊 Select Metric:", ["Total Transactions", "Total Amount"])
    metric_col = "total_transactions" if metric_type == "Total Transactions" else "total_amount"

    selected_states = st.multiselect("Select State(s):", sorted(txn_by_state["state"].unique()), default=["maharashtra", "karnataka", "telangana"])
    filtered_state_df = txn_by_state[txn_by_state["state"].isin(selected_states)].sort_values(by=metric_col, ascending=False)

    col1, col2 = st.columns(2)
    with col1:
        fig1, ax1 = plt.subplots(figsize=(8,6))
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

    fig2, ax2 = plt.subplots(figsize=(14,6))
    sns.lineplot(data=quarterly, x="year_quarter", y="transactions", hue="state", marker="o", ax=ax2)
    ax2.set_title("Quarterly Transactions Over Time")
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    st.markdown("💡 **Trend Insight:** All top states show seasonal spikes, especially in Q3–Q4 due to festivals and year-end sales.")

    st.markdown("---")
    st.markdown("### 🧾 Transaction Category Breakdown")

    selected_category_state = st.selectbox("📍 Choose a state for category view:", selected_states)
    cat_filtered = txn_by_category[txn_by_category['state'] == selected_category_state]

    fig3, ax3 = plt.subplots(figsize=(10,6))
    sns.barplot(data=cat_filtered, x='transaction_type', y='total_transactions', palette='pastel', ax=ax3)
    ax3.set_title(f"Transaction Categories – {selected_category_state.title()}")
    plt.xticks(rotation=30)
    st.pyplot(fig3)

    st.markdown("### 🥧 India-Wide Category Share")

    pie_data = txn_by_category.groupby("transaction_type")["total_transactions"].sum().reset_index()

    fig4, ax4 = plt.subplots(figsize=(6,6))
    ax4.pie(pie_data["total_transactions"], labels=pie_data["transaction_type"], autopct='%1.1f%%', startangle=140)
    ax4.set_title("Overall Transaction Share by Category")
    ax4.axis("equal")
    st.pyplot(fig4)

    st.markdown("### 🔥 Heatmap: State vs Category")

    pivot = txn_by_category.pivot(index='state', columns='transaction_type', values='total_transactions').fillna(0)
    fig5, ax5 = plt.subplots(figsize=(14,10))
    sns.heatmap(pivot, cmap="YlGnBu", linewidths=0.5, ax=ax5)
    ax5.set_title("Heatmap: Transaction Categories by State")
    st.pyplot(fig5)

    st.markdown("💡 **Category Insight:** P2P and Merchant dominate across states, while niche services like Insurance and EMI are used in specific regions.")

# ---------------- Other tabs (placeholders) ---------------------
with tab2:
    st.info("📍 Case Study 2 will appear here once prepared.")

with tab3:
    st.info("📍 Case Study 3 will appear here once prepared.")

with tab4:
    st.info("📍 Case Study 4 will appear here once prepared.")

with tab5:
    st.info("📍 Case Study 5 will appear here once prepared.")
