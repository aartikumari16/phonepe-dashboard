# case_study_2.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.header("🏢 Case Study 2: Device Dominance and User Engagement")

    # Load data
    device_engagement = pd.read_csv("device_users_by_brand.csv")
    state_users_by_device = pd.read_csv("state_users_by_device.csv")
    normalized_device_state = pd.read_csv("state_users_by_device.csv")
    brand_quarterly = pd.read_csv("quarterly_brand_usage_trend.csv")

    # --- Visualization 1: Avg. App Open % ---
    st.subheader("📊 Avg. App Open % by Device Brand")
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sorted_df = device_engagement.sort_values(by="avg_app_open_percentage", ascending=False)
    sns.barplot(data=sorted_df, x="brand", y="avg_app_open_percentage", palette="Set2", ax=ax1)
    ax1.set_title("Avg. App Open % per Device Brand")
    ax1.set_ylabel("Avg. App Open Percentage (%)")
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
    st.pyplot(fig1)

    # --- Visualization 2: Total Registered Users ---
    st.subheader("👥 Total Registered Users by Brand")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sorted_df = device_engagement.sort_values(by="total_registered_users", ascending=False)
    sns.barplot(data=sorted_df, x="brand", y="total_registered_users", palette="pastel", ax=ax2)
    ax2.set_title("Total Registered Users per Device Brand")
    ax2.set_ylabel("Total Registered Users")
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
    st.pyplot(fig2)

    # --- Combined Bar + Line Chart ---
    st.subheader("📊 Device Brand: Users vs. Engagement")
    fig3, ax3 = plt.subplots(figsize=(12, 5))
    bar = ax3.bar(device_engagement["brand"], device_engagement["total_registered_users"], label="Total Users", color="skyblue")
    ax3.set_ylabel("Total Registered Users", color="blue")
    ax3.tick_params(axis='y', labelcolor='blue')

    ax4 = ax3.twinx()
    line = ax4.plot(device_engagement["brand"], device_engagement["avg_app_open_percentage"], color="red", marker="o", label="Avg App Open %")
    ax4.set_ylabel("Avg. App Open %", color="red")
    ax4.tick_params(axis='y', labelcolor='red')

    ax3.set_title("Device Brand: Users vs. Engagement")
    ax3.set_xticklabels(device_engagement["brand"], rotation=45)
    st.pyplot(fig3)

    # Get top 5 states by total users
    top_states = state_users_by_device.groupby('state')['total_users'].sum().nlargest(5).index.tolist()
    filtered_df = state_users_by_device[state_users_by_device['state'].isin(top_states)]

    fig3, ax3 = plt.subplots(figsize=(12, 6))
    sns.barplot(data=filtered_df, x='state', y='total_users', hue='brand', ax=ax3)
    ax3.set_title("Top Device Brands in Top 5 States by Registered Users")
    ax3.set_ylabel("Total Users")
    ax3.set_xlabel("State")
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45)
    ax3.legend(title="Brand", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig3)

    # --- Visualization 4: Heatmap – Brand Share by State (Normalized) ---
    st.subheader("🌐 Device Brand Share by State (Normalized Heatmap)")

    pivot_df = state_users_by_device.pivot(index='state', columns='brand', values='total_users').fillna(0)
    normalized = pivot_df.div(pivot_df.sum(axis=1), axis=0)

    fig4, ax4 = plt.subplots(figsize=(14, 10))
    sns.heatmap(normalized, cmap='YlGnBu', linewidths=0.5, linecolor='gray', ax=ax4)
    ax4.set_title("Device Brand Share by State (Normalized)")
    ax4.set_xlabel("Brand")
    ax4.set_ylabel("State")
    st.pyplot(fig4)

    # --- Visualization 5: Line Chart – Quarterly Brand Usage Trend ---
    st.subheader("📈 Quarterly Brand Usage Trend – Top Brands")

    quarterly_brand_usage_trend['year_quarter'] = (
        quarterly_brand_usage_trend['year'].astype(str) +
        ' Q' +
        quarterly_brand_usage_trend['quarter'].astype(str)
    )

    top_brands = ['Xiaomi', 'Samsung', 'Vivo']
    df_trend_filtered = quarterly_brand_usage_trend[
        quarterly_brand_usage_trend['brand'].isin(top_brands)
    ]

    fig5, ax5 = plt.subplots(figsize=(14, 6))
    sns.lineplot(
        data=df_trend_filtered,
        x='year_quarter',
        y='total_registered_users',
        hue='brand',
        marker='o',
        ax=ax5
    )
    ax5.set_title('Quarterly Brand Usage Trend (Top Brands)')
    ax5.set_xlabel('Year - Quarter')
    ax5.set_ylabel('Total Registered Users')
    plt.xticks(rotation=45)
    st.pyplot(fig5)

    # --- Final Insights ---
    st.markdown("### 💡 Summary Insights")
    st.markdown("""
    - **Xiaomi** leads in both user base and app engagement, indicating strong brand-user affinity.
    - **Samsung** maintains steady growth but trails behind in engagement.
    - **Vivo** is gaining momentum with consistent growth in newer quarters.
    - Brand popularity differs by state, and regional user behavior is evident from the heatmap.
    """)
