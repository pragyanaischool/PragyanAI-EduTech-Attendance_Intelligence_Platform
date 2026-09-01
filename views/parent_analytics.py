import streamlit as st
from utils.helpers import render_brand_logo

def render_parent_analytics():
    """
    Renders a dedicated Analytics & Visual Performance dashboard for parents/guardians,
    showcasing ward course breakdown ledgers, monthly trends, and exam cutoff safety margins.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Mr. Ambesange")
    ward_name = "Sateesh Ambesange"
    
    st.markdown(f"## 📊 Ward Analytics & Performance Intelligence — {ward_name}")
    st.markdown(
        f"Detailed statistical breakdown and trend analysis for your ward, monitored by **{user_name}** (*Guardian*)."
    )

    # 2. Top Metric Summary Cards for Ward
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>84.7%</h3><p>Overall Attendance</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>92 / 109</h3><p>Classes Attended</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>17</h3><p>Total Absences</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>🟢 Safe (>75%)</h3><p>Exam Eligibility</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 3. Course-wise Detailed Ledger Table
    st.markdown("### 📋 Course-wise Attendance Ledger & Status")
    st.dataframe({
        "Course Code & Name": ["ECE301 - Digital Design", "ECE302 - VLSI Architecture", "ECE303 - Signals & Systems", "ECE304 - Microprocessors", "ECE305 - Control Systems"],
        "Classes Held": [24, 22, 25, 20, 18],
        "Classes Attended": [22, 19, 19, 17, 15],
        "Attendance %": ["91.6%", "86.3%", "76.0%", "85.0%", "83.3%"],
        "Safety Status": ["🟢 Excellent", "🟢 Good", "🟡 Monitor Closely", "🟢 Good", "🟢 Good"]
    }, use_container_width=True)

    st.markdown("---")

    # 4. Guardian Trend Insights & Counseling Summary
    col_a1, col_a2 = st.columns(2)
    
    with col_a1:
        st.markdown("### 📈 Monthly Attendance Trend")
        st.info(
            "**Trend Observation:** Your ward's attendance has improved by **+4.2%** "
            "over the past month following the submission of medical recovery certificates for viral fever."
        )

    with col_a2:
        st.markdown("### 💡 Faculty Advisor Notes")
        st.success(
            "**Advisor Feedback:** *'Sateesh is performing well in practical evaluations. "
            "Encourage consistent attendance in Signals & Systems to maintain comfort above the 75% cutoff line.'*"
        )
