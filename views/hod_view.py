import streamlit as st
import pandas as pd
import plotly.express as px
from modules.analytics import AttendanceAnalytics

def render_hod_dashboard():
    """
    Renders the dedicated HOD Department Intelligence Hub with department-wide metrics,
    class comparisons, subject-wise lecture counts, and critical shortage identification.
    """
    user_name = st.session_state.get("user_name", "Dr. HOD (ECE)")
    dept_name = "Electronics & Communication Engineering (ECE)"
    
    st.markdown(f"# 🏛️ HOD Department Intelligence Hub — {dept_name}")
    st.markdown(f"### *Welcome, {user_name} | Department Management & Session Audits*")

    # 1. Top Department Metric Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>420</h3><p>Total Department Students</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>86.4%</h3><p>Overall Department Average</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card" style="border-color:#EF4444;"><h3>37</h3><p>Shortage Students (<75%)</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>28</h3><p>Classes Conducted Today</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 2. Section / Class-Wise Breakdown & Subject-Wise Sessions
    col_class, col_sub = st.columns(2)
    
    with col_class:
        st.markdown("### 🏫 Class & Section Turnout Comparison")
        df_classes = pd.DataFrame({
            "Class Section": ["ECE - Section A", "ECE - Section B", "ECE - Section C", "ECE - Section D"],
            "Semester": [5, 5, 6, 6],
            "Students": [105, 108, 102, 105],
            "Average %": ["89.0%", "84.2%", "81.5%", "91.1%"]
        })
        st.dataframe(df_classes, use_container_width=True)

    with col_sub:
        st.markdown("### 📚 Subject-Wise Turnout Audit")
        df_subjects = pd.DataFrame({
            "Subject Name": ["Digital Electronics", "Signals & Systems", "VLSI Design", "Microprocessors"],
            "Semester": [5, 5, 6, 6],
            "Turnout %": ["88.0%", "79.0%", "91.0%", "84.0%"],
            "Status": ["Safe", "Warning", "Safe", "Safe"]
        })
        st.dataframe(df_subjects, use_container_width=True)

    st.markdown("---")

    # 3. HOD Subject-wise Session Intelligence (Calling Analytics Module)
    AttendanceAnalytics.render_hod_subject_sessions_dashboard()

    st.markdown("---")

    # 4. Critical Shortage Student Audit Table
    st.markdown("### ⚠️ Department Shortage & Critical Risk Student Audit")
    st.markdown("Students requiring administrative counseling or warning notices due to sub-75% attendance:")
    
    df_shortage = pd.DataFrame({
        "Student Name": ["Student A", "Student B", "Student C", "Student D"],
        "Enrollment No": ["PRG2026ECE042", "PRG2026ECE119", "PRG2026ECE205", "PRG2026ECE312"],
        "Semester / Sec": ["Sem 5 (ECE-A)", "Sem 5 (ECE-B)", "Sem 6 (ECE-C)", "Sem 6 (ECE-A)"],
        "Subject in Shortage": ["Signals & Systems", "Microprocessors", "Digital Electronics", "VLSI Design"],
        "Attendance %": ["61.0% (Critical)", "68.5% (High Risk)", "72.0% (Warning)", "64.2% (Critical)"],
        "Action Status": ["Notice Sent", "Pending Review", "Parent Alerted", "Detention Risk"]
    })
    st.dataframe(df_shortage, use_container_width=True)
