import streamlit as st
import pandas as pd
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_faculty_analytics():
    """
    Renders a dedicated Analytics & Performance Intelligence dashboard for faculty members,
    showcasing course turnout comparisons, student risk distributions, lecture punctuality metrics,
    subject-wise student analytics, and student-wise granular drill-down tables.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Faculty (ECE)")
    PragyanDatabase.initialize_database()
    
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

    st.markdown("---")

    # ==========================================
    # NEW ENHANCEMENT 1: SUBJECT-WISE STUDENTS ANALYTICS
    # ==========================================
    st.markdown("### 📚 Subject-Wise Cohort Analytics & Turnout Distribution")
    st.markdown("Analyze attendance turnout, exam eligibility ratios, and shortage risk distributions per subject.")

    sc1, sc2, sc3 = st.columns(3)
    with sc1:
        subj_year = st.selectbox("Select Academic Year", ["2026 - 2027", "2025 - 2026", "2024 - 2025"], key="subj_year")
    with sc2:
        subject_choice = st.selectbox(
            "Select Subject / Course", 
            ["ECE301 - Digital Logic Design", "ECE302 - VLSI Architecture", "ECE303 - Signals & Systems", "ECE304 - Microcontrollers"],
            key="subj_choice"
        )
    with sc3:
        metric_choice = st.selectbox(
            "Select Analytics Metric", 
            ["Attendance Turnout Distribution (%)", "Exam Eligibility Pass Rates", "Shortage Risk Breakdown (<75%)"],
            key="metric_choice"
        )

    st.markdown(f"#### 📈 Cohort Performance Report: `{subject_choice}` ({subj_year})")

    # Generate Mock Data Based on Subject Selection
    if "ECE301" in subject_choice:
        subj_df = pd.DataFrame({
            "Performance Tier": ["Safe (>85%)", "Moderate (75%-85%)", "At-Risk (<75%)"],
            "Student Count": [142, 68, 15],
            "Percentage of Cohort (%)": [62.7, 30.0, 7.3]
        }).set_index("Performance Tier")
    elif "ECE302" in subject_choice:
        subj_df = pd.DataFrame({
            "Performance Tier": ["Safe (>85%)", "Moderate (75%-85%)", "At-Risk (<75%)"],
            "Student Count": [120, 85, 20],
            "Percentage of Cohort (%)": [53.3, 37.8, 8.9]
        }).set_index("Performance Tier")
    else:
        subj_df = pd.DataFrame({
            "Performance Tier": ["Safe (>85%)", "Moderate (75%-85%)", "At-Risk (<75%)"],
            "Student Count": [130, 75, 20],
            "Percentage of Cohort (%)": [56.5, 32.6, 8.7]
        }).set_index("Performance Tier")

    col_sa1, col_sa2 = st.columns([1.2, 1])
    with col_sa1:
        st.dataframe(subj_df, use_container_width=True)
    with col_sa2:
        st.bar_chart(subj_df["Student Count"])

    st.markdown("---")

    # ==========================================
    # NEW ENHANCEMENT 2: STUDENT-WISE DEEP-DIVE ANALYTICS
    # ==========================================
    st.markdown("### 🎓 Student-Wise Granular Analytics & Drill-Down")
    st.markdown("Inspect individual student attendance logs filtered by semester, subject, and year.")

    dc1, dc2, dc3 = st.columns(3)
    with dc1:
        drill_sem = st.selectbox("Select Semester / Term", ["Sem 3", "Sem 5", "Sem 7"], key="drill_sem")
    with dc2:
        drill_subj = st.selectbox("Select Enrolled Subject", ["ECE301 - Digital Logic Design", "ECE302 - VLSI Architecture", "ECE303 - Signals & Systems"], key="drill_subj")
    with dc3:
        drill_year = st.selectbox("Academic Year", ["2026", "2025"], key="drill_year")

    # Fetch students from database for realistic drill-down
    students_db = PragyanDatabase.get_students()
    
    # Build student performance table for selected semester/subject
    student_drill_records = []
    for idx, s in enumerate(students_db[:25]):  # Show top 25 students for deep-dive
        student_drill_records.append({
            "Roll No": s.get("roll", f"ECE_2026_{idx+1:03d}"),
            "Student Name": s.get("name", f"Student {idx+1}"),
            "Semester": s.get("semester", drill_sem),
            "Subject": drill_subj.split(" - ")[0],
            "Classes Held": 30,
            "Classes Attended": round(30 * (s.get("attendance_percentage", 80.0) / 100)),
            "Attendance %": f"{s.get('attendance_percentage', 80.0)}%",
            "Exam Eligibility Status": s.get("exam_eligibility_status", "🟢 Safe")
        })

    st.markdown(f"#### 📋 Individual Student Ledger — `{drill_sem}` | `{drill_subj}` ({drill_year})")
    
    # Search / Filter Bar for Students
    student_search = st.text_input("🔍 Search Student by Name or Roll Number", placeholder="Type student name...")
    
    filtered_drill = student_drill_records
    if student_search.strip():
        filtered_drill = [r for r in filtered_drill if student_search.lower() in r["Student Name"].lower() or student_search.lower() in r["Roll No"].lower()]

    if filtered_drill:
        st.dataframe(filtered_drill, use_container_width=True)
    else:
        st.info("No students found matching your search query.")
