# case_study_2.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.header("🏢 Case Study 2: Device Dominance and User Engagement")

    # Load data
    device_engagement = pd.read_csv("device_users_by_brand.csv")
    top_devices_states = pd.read_csv("state_users_by_device.csv")
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

    # --- Visualization 4: Top Brands in Top 5 States ---
    st.subheader("📍 Top Device Brands in Top 5 States")
    fig4, ax4 = plt.subplots(figsize=(12, 6))
    sns.barplot(data=top_devices_states, x="state", y="total_users", hue="brand", ax=ax4)
    ax4.set_title("Top Device Brands in Top 5 States by Registered Users")
    ax4.set_ylabel("Total Users")
    ax4.set_xticklabels(ax4.get_xticklabels(), rotation=30)
    st.pyplot(fig4)

    # --- Visualization 5: Heatmap (Normalized) ---
    st.subheader("🌐 Device Brand Share by State (Normalized)")
    heat_df = normalized_device_state.set_index("state")
    fig5, ax5 = plt.subplots(figsize=(14, 10))
    sns.heatmap(heat_df, cmap="YlGnBu", linewidths=0.5, ax=ax5)
    ax5.set_title("Device Brand Share by State")
    st.pyplot(fig5)

    # --- Visualization 6: Quarterly Brand Usage Trend ---
    st.subheader("📆 Quarterly Brand Usage Trend – Top Brands")
    fig6, ax6 = plt.subplots(figsize=(14, 6))
    brand_quarterly['year_quarter'] = brand_quarterly['year'].astype(str) + " Q" + brand_quarterly['quarter'].astype(str)
    sns.lineplot(data=brand_quarterly, x="year_quarter", y="total_users", hue="brand", marker="o", ax=ax6)
    ax6.set_title("Quarterly Brand Usage Trend (Top Brands)")
    plt.xticks(rotation=45)
    st.pyplot(fig6)

    st.markdown("💡 **Insights:**")
    st.markdown("- Xiaomi leads in both registrations and engagement.")
    st.markdown("- Vivo shows rapid growth and engagement, especially in later quarters.")
    st.markdown("- Regional preferences vary significantly for brands.")
