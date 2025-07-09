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
    quarterly_brand_usage_trend = pd.read_csv("quarterly_brand_usage_trend.csv")

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



    st.subheader("📱 Device Brand Insights & Actionable Recommendations")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔍 **Key Insights from Data Analysis & Visualizations**")

        st.markdown("#### **Total Registered Users per Device Brand**")
        st.markdown("- **Xiaomi** has the highest number of registered users, followed by **Samsung**, **Vivo**, and **Oppo**.")
        st.markdown("- These four brands account for a significant majority of PhonePe’s user base.")
        st.markdown("- Other brands like **Realme**, **Apple**, **Motorola**, and **OnePlus** have comparatively lower user counts.")

        st.markdown("#### **Device Brand vs. Engagement (Avg. App Open %)**")
        st.markdown("- **Xiaomi** leads in both user base and highest average app open %.")
        st.markdown("- **Samsung** and **Vivo** also show decent engagement but lag behind Xiaomi.")
        st.markdown("- Brands like **Apple** and **Motorola** show lower engagement despite having a substantial user base.")
        st.markdown("- Smaller brands show extremely low engagement, indicating underutilization.")

        st.markdown("#### **App Open % by Device Brand**")
        st.markdown("- **Xiaomi** leads with ~26% average app open rate, indicating high engagement.")
        st.markdown("- **Samsung** and **Vivo** follow, with slightly lower engagement rates.")
        st.markdown("- Brands such as **Apple**, **Motorola**, and **Huawei** exhibit low app engagement despite registrations.")

        st.markdown("#### **Top Device Brands in Top 5 States by Registered Users**")
        st.markdown("- Across top states (**Andhra Pradesh, Karnataka, Maharashtra, Rajasthan, Uttar Pradesh**), **Xiaomi** consistently leads.")
        st.markdown("- The device brand hierarchy remains consistent across regions, with slight state-wise variations in gaps.")

        st.markdown("#### **Device Brand Share by State (Heatmap)**")
        st.markdown("- **Xiaomi** dominates most states, especially **Jammu & Kashmir**, **Punjab**, and northeastern states.")
        st.markdown("- **Samsung** shows strong presence in **Kerala**, **Karnataka**, and **Maharashtra**.")
        st.markdown("- **Oppo**, **Vivo**, and **Realme** have moderate, state-specific presence.")
        st.markdown("- Premium brands like **Apple** have minimal state-wise share.")

        st.markdown("#### **Quarterly Brand Usage Trend (Top Brands)**")
        st.markdown("- **Xiaomi** shows steady, consistent growth from 2019 to 2022, maintaining its lead.")
        st.markdown("- **Samsung** and **Vivo** also show consistent but slower growth.")
        st.markdown("- Overall trend shows increasing smartphone penetration and PhonePe’s growing adoption.")

    with col2:
        st.markdown("### 📝 **Actionable Recommendations**")

        st.markdown("#### **Maximize Engagement with High-User Brands**")
        st.markdown("- Prioritize optimizing app experience for **Xiaomi**, **Samsung**, **Vivo**, and **Oppo** users.")
        st.markdown("- Introduce brand-specific promotions or exclusive features (e.g., device-based UI enhancements).")

        st.markdown("#### **Boost Engagement for Low-Engagement Brands**")
        st.markdown("- Investigate low engagement in brands like **Apple**, **Motorola**, and **Huawei** despite significant user registrations.")
        st.markdown("- Optimize app compatibility, performance, and notifications for these devices.")
        st.markdown("- Run targeted push notifications or engagement campaigns for these user segments.")

        st.markdown("#### **State-Level Brand Targeting**")
        st.markdown("- Design regional campaigns based on dominant brands:")
        st.markdown("  - **North & Northeast India:** Xiaomi-focused promotions.")
        st.markdown("  - **South India:** Balanced campaigns for Xiaomi and Samsung users.")
        st.markdown("  - **Urban & Premium Markets:** Specialized strategies for **Apple** and **OnePlus** users.")

        st.markdown("#### **Quarterly Tracking & Dynamic Optimization**")
        st.markdown("- Track quarterly brand trends to detect emerging brands or declining engagement.")
        st.markdown("- Conduct quarterly reviews to fine-tune device-specific optimizations.")

        st.markdown("#### **In-App Personalization Based on Device Brands**")
        st.markdown("- Use device-brand segmentation for personalized onboarding, tutorials, or feature recommendations.")
        st.markdown("- Pre-load lighter app versions or optimize backend for low-end devices in certain brands.")

    st.markdown("---")

    st.markdown("### ✅ **Conclusion**")
    st.markdown("""
    This analysis highlights **Xiaomi’s** clear dominance in both user base and engagement metrics, making it the top priority for app optimization.
    Brands like **Samsung**, **Vivo**, and **Oppo** also remain significant contributors.
    Addressing low-engagement brands such as **Apple** and **Motorola** can unlock untapped user potential.
    Tailored device-wise and region-wise strategies will be essential for PhonePe’s continued growth and improved user satisfaction.
    """)
