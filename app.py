import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Define Tabs for Each Case Study ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Case Study 1 – Transaction Dynamics",
    "🏢 Case Study 2 – [Your Title]",
    "📍 Case Study 3 – [Your Title]",
    "💳 Case Study 4 – [Your Title]",
    "📈 Case Study 5 – [Your Title]"
])

# # ---------------- TAB 1 ---------------------
with tab1:
    st.header("🏙️ Case Study 1: Decoding Transaction Dynamics on PhonePe")
    
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
    st.markdown("### 📈 Quarterly Trend (for Selected States)")

    # Merge metric into quarterly trend
    quarterly = quarterly_trend[quarterly_trend['state'].isin(selected_states)].copy()
    quarterly['year_quarter'] = quarterly['year'].astype(str) + " Q" + quarterly['quarter'].astype(str)

    fig2, ax2 = plt.subplots(figsize=(14,6))
    sns.lineplot(data=quarterly, x="year_quarter", y="transactions", hue="state", marker="o", ax=ax2)
    ax2.set_title("Quarterly Transactions Over Time")
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    st.markdown("💡 **Observation**: Use the dropdowns above to compare how states evolved over time.")
