import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide')
st.title("📊 PhonePe Transaction Dashboard – Case Study 1")

# Load Data
st.sidebar.header("📁 Load Data")
txn_by_state = pd.read_csv("transaction_by_state.csv")
quarterly_trend = pd.read_csv("quarterly_trend_by_state.csv")
txn_by_category = pd.read_csv("transactions_by_state_category.csv")

# --- Section 1: Total Transactions by State ---
st.subheader("1️⃣ Total Transactions and Amount by State")

top_states = txn_by_state.sort_values(by="total_transactions", ascending=False).head(10)

col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots(figsize=(8,6))
    sns.barplot(x='total_transactions', y='state', data=top_states, palette='Blues_d', ax=ax1)
    ax1.set_title("Top 10 States by Transactions")
    st.pyplot(fig1)

with col2:
    top_amount = txn_by_state.sort_values(by="total_amount", ascending=False).head(10)
    fig2, ax2 = plt.subplots(figsize=(8,6))
    sns.barplot(x='total_amount', y='state', data=top_amount, palette='Greens_d', ax=ax2)
    ax2.set_title("Top 10 States by Transaction Amount")
    st.pyplot(fig2)

# --- Section 2: Quarterly Trend per State ---
st.subheader("2️⃣ Quarterly Transaction Trend per State")

# Clean and prepare quarter column
quarterly_trend['year_quarter'] = quarterly_trend['year'].astype(str) + ' ' + quarterly_trend['quarter'].astype(str)
top5_states = quarterly_trend.groupby("state")["transactions"].sum().sort_values(ascending=False).head(5).index
df_top5 = quarterly_trend[quarterly_trend["state"].isin(top5_states)]

# Sort year_quarter chronologically
df_top5['year_quarter'] = pd.Categorical(df_top5['year_quarter'],
    sorted(df_top5['year_quarter'].unique(), key=lambda x: (int(x.split()[0]), x.split()[1])))

fig3, ax3 = plt.subplots(figsize=(14,6))
sns.lineplot(data=df_top5, x="year_quarter", y="transactions", hue="state", marker="o", ax=ax3)
ax3.set_title("Quarterly Transaction Trend – Top 5 States")
ax3.set_xlabel("Year and Quarter")
ax3.set_ylabel("Transactions")
plt.xticks(rotation=45)
st.pyplot(fig3)

# --- Section 3: Category-wise Analysis ---
st.subheader("3️⃣ Transaction Category Insights")

# Grouped Bar Chart (Top States)
top_states_cat = txn_by_category.groupby('state')['total_transactions'].sum().sort_values(ascending=False).head(10).index
df_top_cat = txn_by_category[txn_by_category['state'].isin(top_states_cat)]

fig4, ax4 = plt.subplots(figsize=(12,6))
sns.barplot(data=df_top_cat, x='state', y='total_transactions', hue='transaction_type', ax=ax4)
ax4.set_title("Transaction Categories by Top 10 States")
plt.xticks(rotation=45)
st.pyplot(fig4)

# Pie Chart – All India Category Split
st.markdown("#### 🥧 All-India Transaction Type Split")
df_pie = txn_by_category.groupby("transaction_type")["total_transactions"].sum().reset_index()

fig5, ax5 = plt.subplots(figsize=(6,6))
ax5.pie(df_pie["total_transactions"], labels=df_pie["transaction_type"], autopct='%1.1f%%', startangle=140)
ax5.set_title("Transaction Share by Category")
ax5.axis("equal")
st.pyplot(fig5)

# Heatmap
st.markdown("#### 🔥 Heatmap – Category Intensity by State")
heat_df = txn_by_category.pivot(index='state', columns='transaction_type', values='total_transactions').fillna(0)

fig6, ax6 = plt.subplots(figsize=(14,10))
sns.heatmap(heat_df, cmap="YlGnBu", linewidths=0.5, ax=ax6)
ax6.set_title("Heatmap of Transaction Categories by State")
st.pyplot(fig6)

st.markdown("---")
st.info("Built with ❤️ by Aarti | Case Study 1: Transaction Dynamics on PhonePe")
