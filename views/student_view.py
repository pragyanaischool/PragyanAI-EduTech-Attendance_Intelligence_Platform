import streamlit as st
from modules.analytics import AttendanceAnalytics

def render_student_dashboard():
    """
    Renders the dedicated student portal view with metrics, subject-wise passport,
    trajectory trends, and shortage calculation intelligence.
    """
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    
    st.markdown(f"# 🎒 Student Attendance Passport — {user_name}")
    st.markdown("### *Capture. Analyse. Predict. Improve.*")
    
    # 1. Top Metric Grid Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>84.7%</h3><p>Overall Attendance</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>92</h3><p>Classes Present</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>17</h3><p>Classes Absent</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>Warning</h3><p>Cutoff Status (>75%)</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 2. Subject-wise Breakdown Table & Visual Status
    st.markdown("### 📊 Subject-wise Attendance Passport")
    st.dataframe({
        "Subject": ["Digital Electronics", "VLSI Design", "Signals & Systems", "Microprocessors", "Control Systems"],
        "Classes Conducted": [24, 22, 25, 20, 18],
        "Classes Attended": [22, 19, 19, 17, 15],
        "Attendance %": ["91.6%", "86.3%", "76.0%", "85.0%", "83.3%"],
        "Visual Status": ["Excellent", "Good", "Warning", "Good", "Good"]
    }, use_container_width=True)

    st.markdown("---")
    
    # 3. Attendance Trajectory Trend Chart
    col_chart, col_intel = st.columns([1.2, 1])
    
    with col_chart:
        st.markdown("### 📈 Monthly Trajectory")
        fig = AttendanceAnalytics.render_student_trend_chart()
        st.plotly_chart(fig, use_container_width=True)
        
    with col_intel:
        st.markdown("### 🤖 GenAI Cutoff Intelligence")
        st.info("💡 **Shortage Projection Calculator:**")
        
        # Interactive Student Shortage Simulation
        selected_subject = st.selectbox("Select Subject for Simulation", ["Signals & Systems (76%)", "VLSI Design (86.3%)"])
        
        if "Signals" in selected_subject:
            st.warning("⚠️ **Current Status:** At risk in Signals & Systems. \n- **Current Classes:** 19/25 present (76%). \n- **To reach 75%:** Maintain stability (already safe above cutoff). \n- **If you miss next 3 classes:** Attendance drops to **65.5% (CRITICAL)**.")
        else:
            st.success("✅ **Current Status:** Safe and healthy margin in VLSI Design. \n- **Current Classes:** 19/22 present (86.3%). \n- **Buffer:** You can afford to miss up to 2 classes without breaching the 75% cutoff limit.")
            
        st.markdown("👉 *Need deeper predictive insights? Use the **AI Chatbot Assistant** tab to ask specific scenario questions.*")
