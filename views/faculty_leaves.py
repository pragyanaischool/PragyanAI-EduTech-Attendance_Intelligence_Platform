import streamlit as st
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_faculty_leaves():
    """
    Renders the Faculty Leaves & Student Absence Audit Hub.
    Features:
    - List of Students on Leave with filters based on Subject and Date/Month.
    - List of Student Leave Applications (Approved/Pending) with Month & Year filters.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Smitha Rao")
    PragyanDatabase.initialize_database()
    
    st.markdown(f"# 📋 Faculty Leave Audit & Student Absence Hub — {user_name}")
    st.markdown("### *Monitor student leave applications, check subject-wise absences, and audit approval statuses.*")
    
    st.info(
        "💡 **Faculty Governance Portal:** Review student leave requests and filter absences by subject "
        "and date to manage classroom attendance accurately."
    )

    st.markdown("---")

    # 2. Section 1: List of Students on Leave (with Subject & Date/Month Filters)
    st.markdown("### 🎓 Students on Leave Roster & Subject Filters")
    st.markdown("Filter active and past student absences by enrolled subject and specific dates or months.")

    # Mock or Session Database Student Leaves
    all_student_leaves = st.session_state.get("student_leave_requests", [
        {"student": "Sateesh Ambesange", "roll": "ECE_2026_042", "subject": "ECE301 - Digital Logic Design", "type": "Medical Exemption", "from": "2026-09-01", "to": "2026-09-03", "reason": "Viral Fever", "status": "🟢 Approved"},
        {"student": "Aarav Sharma", "roll": "ECE_2026_010", "subject": "ECE301 - Digital Logic Design", "type": "On-Duty", "from": "2026-08-25", "to": "2026-08-26", "reason": "Robotics Symposium", "status": "🟢 Approved"},
        {"student": "Priya Patel", "roll": "ECE_2026_088", "subject": "ECE302 - VLSI Architecture", "type": "Personal Leave", "from": "2026-09-02", "to": "2026-09-02", "reason": "Family Function", "status": "🟡 Pending Review"},
        {"student": "Rohan Verma", "roll": "ECE_2026_102", "subject": "ECE303 - Signals & Systems", "type": "Medical Exemption", "from": "2026-07-14", "to": "2026-07-16", "reason": "Dengue Recovery", "status": "🟢 Approved"}
    ])

    # Filter Controls for Students on Leave
    fc1, fc2, fc3 = st.columns(3)
    with fc1:
        subject_filter = st.selectbox(
            "Filter by Subject", 
            ["All Subjects", "ECE301 - Digital Logic Design", "ECE302 - VLSI Architecture", "ECE303 - Signals & Systems"]
        )
    with fc2:
        month_roster_filter = st.selectbox(
            "Filter by Month / Period", 
            ["All Time", "September 2026", "August 2026", "July 2026"]
        )
    with fc3:
        status_roster_filter = st.selectbox(
            "Filter by Approval Status", 
            ["All Statuses", "🟢 Approved", "🟡 Pending Review"]
        )

    # Apply Filters to Students on Leave
    filtered_roster = all_student_leaves
    if subject_filter != "All Subjects":
        filtered_roster = [l for l in filtered_roster if l.get("subject") == subject_filter]
    if month_roster_filter == "September 2026":
        filtered_roster = [l for l in filtered_roster if "2026-09" in l.get("from", "")]
    elif month_roster_filter == "August 2026":
        filtered_roster = [l for l in filtered_roster if "2026-08" in l.get("from", "")]
    elif month_roster_filter == "July 2026":
        filtered_roster = [l for l in filtered_roster if "2026-07" in l.get("from", "")]
    if status_roster_filter != "All Statuses":
        filtered_roster = [l for l in filtered_roster if status_roster_filter in l.get("status", "")]

    if filtered_roster:
        st.dataframe(filtered_roster, use_container_width=True)
    else:
        st.info("No student leave records match the selected filters.")

    st.markdown("---")

    # 3. Section 2: Student Leave Applications Audit & Month/Year Filters
    st.markdown("### 🗄️ Student Leave Applications Audit & Approval Ledger")
    st.markdown("Review all leave applications submitted by students across department courses with Month and Year filtering.")

    # Filter Controls for Audit Ledger
    ac1, ac2 = st.columns(2)
    with ac1:
        audit_month_filter = st.selectbox(
            "Audit Month", 
            ["All Months", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
            index=9 # Default September
        )
    with ac2:
        audit_year_filter = st.selectbox(
            "Audit Year", 
            ["2026", "2025", "2024"]
        )

    # Date string matching based on year and month number
    month_map = {
        "January": "01", "February": "02", "March": "03", "April": "04", 
        "May": "05", "June": "06", "July": "07", "August": "08", 
        "September": "09", "October": "10", "November": "11", "December": "12"
    }
    
    target_year = audit_year_filter
    target_month_code = month_map.get(audit_month_filter, "")

    filtered_audit = all_student_leaves
    if audit_month_filter != "All Months":
        filtered_audit = [l for l in filtered_audit if f"{target_year}-{target_month_code}" in l.get("from", "")]
    else:
        filtered_audit = [l for l in filtered_audit if f"{target_year}" in l.get("from", "")]

    if filtered_audit:
        st.dataframe({
            "Student Name": [l.get("student") for l in filtered_audit],
            "Roll Number": [l.get("roll", "ECE_2026_0X") for l in filtered_audit],
            "Leave Category": [l.get("type") for l in filtered_audit],
            "From Date": [l.get("from") for l in filtered_audit],
            "To Date": [l.get("to") for l in filtered_audit],
            "Reason": [l.get("reason") for l in filtered_audit],
            "Status": [l.get("status") for l in filtered_audit]
        }, use_container_width=True)
    else:
        st.info(f"No leave applications found for **{audit_month_filter} {audit_year_filter}**.")
