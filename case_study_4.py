import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

def run():
    st.header("👥 Case Study 4: User Engagement and Growth Strategy")

    # 1️⃣ Top States by Total Registered Users & App Opens
    st.subheader("📊 Registered Users vs App Opens by State")
    state_user_summary = pd.read_csv("state_user_summary.csv")

    df_sorted = state_user_summary.sort_values("total_registered_users", ascending=True)

    fig1, ax1 = plt.subplots(figsize=(12, 10))
    sns.set_style("whitegrid")
    ax1.barh(df_sorted['state'], df_sorted['total_registered_users'], color='green', label='Registered Users')
    ax1.barh(df_sorted['state'], df_sorted['total_app_opens'], color='salmon', alpha=0.7, label='App Opens')
    ax1.set_xlabel("User Count")
    ax1.set_title("Registered Users vs App Opens by State")
    ax1.legend()
    st.pyplot(fig1)

    st.markdown("---")

    # 2️⃣ District-Wise User Summary (with Plotly Dropdown)
    st.subheader("🌐 District-Wise Registered Users (Interactive)")

    district_user_summary = pd.read_csv("district_user_summary.csv")
    states = sorted(district_user_summary['state'].unique())
    fig2 = go.Figure()

    for state in states:
        df_state = district_user_summary[district_user_summary['state'] == state].sort_values(by='registered_users', ascending=False)
        fig2.add_trace(go.Bar(
            x=df_state['registered_users'],
            y=df_state['district'],
            name=state,
            orientation='h',
            visible=False
        ))

    fig2.data[0].visible = True

    buttons = []
    for i, state in enumerate(states):
        visible = [False] * len(states)
        visible[i] = True
        buttons.append(dict(label=state,
                            method="update",
                            args=[{"visible": visible},
                                  {"title": f"District-wise Registered Users in {state}"}]))

    fig2.update_layout(
        updatemenus=[dict(
            active=0,
            buttons=buttons,
            x=1.15,
            y=1
        )],
        title=f"District-wise Registered Users in {states[0]}",
        xaxis_title="Registered Users",
        yaxis_title="District",
        height=800
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # 3️⃣ Top Districts by Registered Users
    st.subheader("🏆 Top 10 Districts by Total Registered Users")
    top_district_users = pd.read_csv("top_district_uers.csv")

    top_district_users = top_district_users.sort_values(by="total_registered_users", ascending=False).head(10)
    top_district_users["label"] = top_district_users["district"] + " (" + top_district_users["state"] + ")"

    fig3, ax3 = plt.subplots(figsize=(12, 8))
    sns.barplot(data=top_district_users, y="label", x="total_registered_users", palette="magma", ax=ax3)
    ax3.set_title("Top 10 Districts by Total Registered Users")
    ax3.set_xlabel("Total Registered Users")
    ax3.set_ylabel("District (State)")
    st.pyplot(fig3)


    st.subheader("📱 User Engagement Insights & Actionable Recommendations")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔍 **Key Insights from Data Analysis & Visualizations**")

        st.markdown("#### **Registered Users vs. App Opens by State**")
        st.markdown("- **Maharashtra** has the highest number of registered users and app opens, followed by **Uttar Pradesh**, **Karnataka**, **Andhra Pradesh**, and **Madhya Pradesh**.")
        st.markdown("- States like **Bihar**, **Gujarat**, **Rajasthan**, and **Telangana** also have large user bases with moderate app engagement.")
        st.markdown("##### Notable Observations:")
        st.markdown("- **Bihar** and **Gujarat** show high registrations but relatively low app opens, indicating lower engagement despite large user bases.")
        st.markdown("- Southern states like **Karnataka**, **Andhra Pradesh**, and **Telangana** show strong engagement relative to their user base.")

        st.markdown("#### **District-wise User Summary (Interactive Chart)**")
        st.markdown("- This interactive visualization allows drilling down into union territories and districts.")
        st.markdown("- Example: **Andaman & Nicobar Islands:**")
        st.markdown("  - Districts like **South Andaman** have higher registered users compared to others.")
        st.markdown("- Enables focused, hyper-local analysis and strategy formulation.")

        st.markdown("#### **Top 10 Districts by Total Registered Users**")
        st.markdown("- **Bengaluru Urban (Karnataka)** leads with the highest registered users, followed by:")
        st.markdown("  - **Pune** and **Thane** (Maharashtra)")
        st.markdown("  - **Jaipur** (Rajasthan)")
        st.markdown("  - **Mumbai Suburban** (Maharashtra)")
        st.markdown("  - **Hyderabad** and **Rangareddy** (Telangana)")
        st.markdown("  - **Ahmedabad** and **Surat** (Gujarat)")
        st.markdown("  - **North 24 Parganas** (West Bengal)")
        st.markdown("- Most are urban/commercial hubs, reflecting strong app adoption in metro regions.")

    with col2:
        st.markdown("### 📝 **Actionable Recommendations**")

        st.markdown("#### **Capitalize on High User-High Engagement States**")
        st.markdown("- Focused marketing in **Maharashtra**, **Karnataka**, and **Andhra Pradesh** to boost user retention and cross-sell services like insurance, mutual funds, and gold.")
        st.markdown("- Promote exclusive offers and loyalty programs in these regions.")

        st.markdown("#### **Re-engagement Campaigns for Low Engagement Regions**")
        st.markdown("- Regions like **Bihar**, **Gujarat**, and **Rajasthan** show low engagement despite large user bases.")
        st.markdown("##### Suggested Actions:")
        st.markdown("- Push notifications, SMS, and email campaigns to re-engage dormant users.")
        st.markdown("- Localized in-app offers and regional language support.")
        st.markdown("- Collaborations with local merchants to increase app utility.")

        st.markdown("#### **Hyperlocal Expansion Using Interactive Dashboard Insights**")
        st.markdown("- Utilize district-wise interactive tools to:")
        st.markdown("  - Identify promising micro-markets within underperforming states.")
        st.markdown("  - Launch hyperlocal campaigns in high-density but low-engagement districts.")
        st.markdown("  - Customize marketing strategies based on district-specific performance.")

        st.markdown("#### **Urban-Centric Growth Opportunities**")
        st.markdown("- Continue leveraging high-user metros like **Bengaluru Urban**, **Pune**, **Hyderabad**, and **Mumbai Suburban**.")
        st.markdown("- Offer premium services, early-access features, and fintech innovations to increase wallet share in these areas.")

        st.markdown("#### **Enhance Data-Driven Decision Making**")
        st.markdown("- Regularly use the interactive district-wise chart to:")
        st.markdown("  - Monitor changes in user engagement over time.")
        st.markdown("  - Identify emerging districts with growing traction.")
        st.markdown("  - Optimize campaign budgets based on granular insights.")

    st.markdown("---")

    st.markdown("### ✅ **Conclusion**")
    st.markdown("""
    The user engagement analysis reveals a clear divide between high-engagement metro areas and large but under-engaged states.
    By leveraging strong metro markets and launching targeted reactivation campaigns in underperforming regions, PhonePe can significantly boost app usage and market share.
    """)
