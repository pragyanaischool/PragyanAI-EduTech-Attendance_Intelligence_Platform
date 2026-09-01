import streamlit as st
from utils.helpers import render_brand_logo

def render_student_analytics():
    """
    Renders a dedicated Student Analytics & Performance Intelligence dashboard,
    showcasing personal course attendance ledgers, exam eligibility safety margins, and trend insights.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    
    st.markdown(f"## 📊 Student Analytics & Performance Intelligence — {user_name}")
    st.markdown(
        f"Detailed statistical breakdown, course attendance ledgers, and exam eligibility safety margins "
        f"monitored for **{user_name}** (*Student*)."
    )

    # 2. Top Metric Summary Cards for Student
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>84.7%</h3><p>Overall Attendance</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>92 / 109</h3><p>Classes Attended</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>17</h3><p>Total Absences</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>🟢 Safe (>75%)</h3><p>Exam Eligibility</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 3. Course-wise Detailed Ledger Table
    st.markdown("### 📋 Course-Wise Attendance Ledger & Safety Status")
    st.dataframe({
        "Course Code & Name": ["ECE301 - Digital Design", "ECE302 - VLSI Architecture", "ECE303 - Signals & Systems", "ECE304 - Microprocessors", "ECE305 - Control Systems"],
        "Classes Held": [24, 22, 25, 20, 18],
        "Classes Attended": [22, 19, 19, 17, 15],
        "Attendance %": ["91.6%", "86.3%", "76.0%", "85.0%", "83.3%"],
        "Safety Status": ["🟢 Excellent", "🟢 Good", "🟡 Monitor Closely", "🟢 Good", "🟢 Good"]
    }, use_container_width=True)

    st.markdown("---")

    # 4. Student Trend Insights & Faculty Advisor Notes
    col_sa1, col_sa2 = st.columns(2)
    
    with col_sa1:
        st.markdown("### 📈 Monthly Attendance Trend")
        st.info(
            "**Trend Observation:** Your attendance has improved by **+4.2%** over the past month "
            "following the successful submission and approval of medical recovery certificates for viral fever."
        )

    with col_sa2:
        st.markdown("### 💡 Faculty Advisor Feedback")
        st.success(
            "**Advisor Note:** *'Sateesh is demonstrating strong technical aptitude in practical sessions. "
            "Maintain consistent attendance in Signals & Systems to keep a safe buffer above the 75% university cutoff line.'*"
        )
