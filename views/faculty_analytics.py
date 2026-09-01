import streamlit as st
from utils.helpers import render_brand_logo

def render_faculty_analytics():
    """
    Renders a dedicated Analytics & Performance Intelligence dashboard for faculty members,
    showcasing course turnout comparisons, student risk distributions, and lecture punctuality metrics.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Faculty (ECE)")
    
    st.markdown(f"## 📊 Faculty Analytics & Performance Intelligence — {user_name}")
    st.markdown("Comprehensive statistical breakdowns of course turnouts, student attendance distributions, and risk cohorts.")

    # 2. Top Metric Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>89.2%</h3><p>Overall Turnout</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>240</h3><p>Total Students Taught</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>96.5%</h3><p>QR Compliance Rate</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>14</h3><p>Shortage Warnings</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 3. Course Turnout Comparison Table
    st.markdown("### 📋 Course-Wise Turnout & Engagement Breakdown")
    st.dataframe({
        "Course Code & Title": ["ECE301 - Digital Logic Design", "ECE402 - VLSI Architecture", "ECE305 - Microcontrollers"],
        "Enrolled": [48, 52, 60],
        "Avg Attendance %": ["92.4%", "88.1%", "87.5%"],
        "QR Code Scans Avg": ["44.5 / 48", "46.0 / 52", "52.5 / 60"],
        "Risk Health": ["🟢 Excellent", "🟢 Good", "🟡 Monitor"]
    }, use_container_width=True)

    st.markdown("---")

    # 4. Analytical Insights & Recommendations
    col_fa1, col_fa2 = st.columns(2)
    
    with col_fa1:
        st.markdown("### 📈 Weekly Attendance Trend")
        st.info(
            "**Observation:** Turnout peaks consistently on Tuesday and Wednesday mornings (>94%), "
            "while Friday afternoon lectures experience a minor dip (~81%). Consider interactive quizzes on Fridays to boost attendance."
        )

    with col_fa2:
        st.markdown("### ⚠️ At-Risk Cohort Summary")
        st.warning(
            "**Action Required:** 14 students across your 3 courses are currently hovering between 70% and 75% attendance. "
            "Automated warning notices have been dispatched, but direct faculty advisory is recommended."
        )
