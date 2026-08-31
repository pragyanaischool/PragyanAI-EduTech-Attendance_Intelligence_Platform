import streamlit as st
from utils.helpers import render_brand_logo
from modules.analytics import AttendanceAnalytics

def render_student_dashboard():
    """
    Renders the Student Attendance Dashboard allowing students to track their overall attendance,
    subject-wise percentages, shortage risk warnings, and semester records.
    """
    # 1. Safe Brand Watermark Header
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    
    st.markdown(f"# 🎒 Student Attendance Passport — {user_name}")
    st.markdown("### *Capture. Analyse. Predict. Improve.*")

    # 2. Top Metric Cards Grid
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>84.7%</h3><p>Overall Attendance</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>92</h3><p>Classes Present</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>17</h3><p>Classes Absent</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>Safe (>75%)</h3><p>Cutoff Status</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 3. Subject-wise Attendance Passport Table & Analytics
    st.markdown("### 📊 Subject-wise Attendance Passport")
    st.markdown("Detailed breakdown of your attendance across active semester courses:")
    
    subject_attendance_data = {
        "Subject": ["Digital Electronics", "VLSI Design", "Signals & Systems", "Microprocessors", "Control Systems", "Embedded Systems"],
        "Code": ["ECE501", "ECE502", "ECE503", "ECE504", "ECE505", "ECE506"],
        "Classes Conducted": [24, 22, 25, 20, 18, 21],
        "Classes Attended": [22, 19, 19, 17, 15, 18],
        "Attendance %": ["91.6%", "86.3%", "76.0%", "85.0%", "83.3%", "85.7%"],
        "Status": ["🟢 Excellent", "🟢 Good", "🟡 Warning", "🟢 Good", "🟢 Good", "🟢 Good"]
    }
    
    st.dataframe(subject_attendance_data, use_container_width=True)

    st.markdown("---")

    # 4. Shortage Prediction & Counseling Advice
    col_pred1, col_pred2 = st.columns(2)
    
    with col_pred1:
        st.markdown("### 🔮 AI Shortage Predictor")
        st.info(
            "**Prediction Insight:** Based on your current attendance trend of **84.7%**, "
            "you can afford to miss up to **4 consecutive classes** in *Signals & Systems* before "
            "breaching the mandatory 75% university examination eligibility threshold."
        )

    with col_pred2:
        st.markdown("### 📝 Quick Academic Actions")
        st.markdown("- 📤 **Submit Medical Leave:** If you missed classes due to illness, submit certificates via the Leave Portal.")
        st.markdown("- 💬 **Ask PragyanAI Chatbot:** Query specific attendance bylaws or exemption criteria anytime.")
        st.markdown("- 📄 **Download Passport PDF:** Export your official semester attendance summary report.")
