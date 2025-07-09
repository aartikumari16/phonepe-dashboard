import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ------------------- Case Study 5: User Registration Analysis -------------------

def run():
    # Load Data
    state_registrations = pd.read_csv("state_registrations.csv")
    district_registrations = pd.read_csv("district_registrations.csv")
    pincode_registrations = pd.read_csv("pincode_registrations.csv")
    quarterly_registrations = pd.read_csv("quarterly_registrations.csv")

    # ---- 1. Top States by Total Registered Users ----
    st.subheader("📊 Total Registered Users by State")
    df_sorted = state_registrations.sort_values("total_registrations", ascending=True)

    fig1, ax1 = plt.subplots(figsize=(12, 10))
    sns.barplot(data=df_sorted, y='state', x='total_registrations', palette="crest")
    ax1.set_title("Total Registered Users by State")
    ax1.set_xlabel("Registered Users")
    st.pyplot(fig1)

    # ---- 2. District-wise Registered Users ----
    st.subheader("🏙️ District-wise Registered Users (Interactive)")
    #Sort and limit for clarity (Top 20 Districts)
    top_districts = district_registrations.sort_values("total_registrations", ascending=False).head(20)

    # Combine state & district for clarity
    top_districts["label"] = top_districts["district"] + " (" + top_districts["state"] + ")"

    # Plot Horizontal Bar Chart
    fig2, ax2 = plt.subplots(figsize=(12, 10))
    sns.barplot(data=top_districts, x="total_registrations", y="label", palette="magma")

    ax2.set_title("Top 20 Districts by Total User Registrations")
    ax2.set_xlabel("Total Registrations")
    ax2.set_ylabel("District (State)")
    st.pyplot(fig2)

    # ---- 3. Top 10 Pin Codes by Registered Users ----
    st.subheader("📌 Top 10 Pin Codes by Registered Users")
    top10_pincodes = pincode_registrations.sort_values(by="registered_users", ascending=False).head(10)

    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top10_pincodes, y='pincode', x='registered_users', palette="magma")
    ax3.set_title("Top 10 Pin Codes by Registered Users")
    ax3.set_xlabel("Registered Users")
    st.pyplot(fig3)

    # ---- 4. Quarterly User Registration Trend (All States) ----
    st.subheader("📈 Quarterly User Registration Trends (All States)")
    quarterly_registrations['year_quarter'] = quarterly_registrations['year'].astype(str) + ' Q' + quarterly_registrations['quarter'].astype(str)

    plt.figure(figsize=(14, 8))
    sns.lineplot(data=quarterly_registrations, x='year_quarter', y='total_registrations', hue='state', marker='o')
    plt.title("Quarterly User Registration Trends (All States)")
    plt.xlabel("Quarter")
    plt.ylabel("Total Registrations")
    plt.xticks(rotation=45)
    plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(plt)


    st.subheader("📈 User Registration Insights & Actionable Recommendations")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔍 **Key Insights from Data Analysis & Visualizations**")

        st.markdown("#### **Total User Registrations by State**")
        st.markdown("- **Maharashtra**, **Uttar Pradesh**, **Karnataka**, and **Andhra Pradesh** are the top states with the highest user registrations.")
        st.markdown("- These four states collectively dominate user registration volumes.")
        st.markdown("- Other significant contributors include **Rajasthan**, **West Bengal**, **Telangana**, and **Tamil Nadu**.")

        st.markdown("#### **Top 20 Districts by Total User Registrations**")
        st.markdown("- **Bengaluru Urban (Karnataka)** leads by a large margin, followed by:")
        st.markdown("  - **Pune**, **Thane**, **Jaipur**, and **Mumbai Suburban**.")
        st.markdown("- Districts from **Maharashtra**, **Telangana**, and **Gujarat** are also prominent.")
        st.markdown("- Urban districts dominate, showing a strong link between urbanization and app registrations.")

        st.markdown("#### **Top 20 Pincodes by Total User Registrations**")
        st.markdown("- Pincodes from metro cities show exceptionally high registration numbers.")
        st.markdown("- Frequent appearances of pincodes from **Karnataka**, **Maharashtra**, **Gujarat**, and **Uttar Pradesh**.")
        st.markdown("- Indicates highly localized adoption in dense urban and semi-urban pockets.")

        st.markdown("#### **Quarterly User Registration Trends – Top States**")
        st.markdown("- **Maharashtra** and **Uttar Pradesh** show strong, consistent growth across quarters.")
        st.markdown("- **Karnataka**, **Andhra Pradesh**, and **Rajasthan** also show steady upward trends.")
        st.markdown("- Other states with smaller bases are also showing gradual growth patterns.")

    with col2:
        st.markdown("### 📝 **Actionable Recommendations**")

        st.markdown("#### **Focus on High-Growth States & Districts**")
        st.markdown("- Prioritize **Maharashtra**, **Uttar Pradesh**, **Karnataka**, **Andhra Pradesh**, and **Rajasthan** for targeted campaigns.")
        st.markdown("- Deepen penetration in fast-growing districts like **Bengaluru Urban**, **Pune**, **Jaipur**, and **Hyderabad** via customized offers and partnerships.")

        st.markdown("#### **Leverage Top Performing Pincodes**")
        st.markdown("- Launch hyper-local campaigns in top-performing pincodes within metro cities.")
        st.markdown("- Offer rewards, cashback, or exclusive perks to boost engagement in these high-density areas.")

        st.markdown("#### **Expand in Underpenetrated but Growing Regions**")
        st.markdown("- Focus on growing states like **Telangana**, **West Bengal**, and **Tamil Nadu** with region-specific strategies.")
        st.markdown("- Use vernacular promotions and partner with local merchants to improve adoption.")

        st.markdown("#### **Monitor Urban-Rural Growth Gaps**")
        st.markdown("- Explore suburban and semi-rural areas near high-performing districts to tap into emerging markets.")

        st.markdown("#### **Use Quarterly Trends for Campaign Timing**")
        st.markdown("- Align new user acquisition campaigns with quarters showing historically high growth (e.g., festive or financial quarters).")
        st.markdown("- Introduce referral programs and onboarding bonuses during these periods.")

        st.markdown("#### **Product Optimization Based on Insights**")
        st.markdown("- Optimize app UI/UX for regional languages, local transaction patterns, and varying digital literacy levels in high-growth regions.")

    st.markdown("---")

    st.markdown("### ✅ **Conclusion**")
    st.markdown("""
    The analysis reveals that **Maharashtra**, **Uttar Pradesh**, and **Karnataka** are leading states in user registrations, along with key districts like **Bengaluru Urban** and **Pune**.
    Most registrations are concentrated in urban regions, with consistent growth across quarters.
    This indicates strong urban adoption and emerging opportunities in other regions that can be unlocked with targeted strategies and localized initiatives.
    """)
