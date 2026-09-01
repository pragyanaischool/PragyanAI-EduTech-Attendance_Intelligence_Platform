import streamlit as st
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_student_dashboard():
    """
    Renders the student attendance intelligence dashboard, pulling records from the database,
    displaying course-wise attendance passports, the Faculty & HOD availability tracker, 
    and live institutional notices.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    
    # Initialize Database State
    PragyanDatabase.initialize_database()
    
    st.markdown(f"# 🎒 Student Attendance Intelligence Hub — {user_name}")
    st.markdown("### *Real-Time Attendance Passport, Course Ledger, and Faculty Availability Tracker.*")

    # 2. Fetch Student Record from Database
    students_db = PragyanDatabase.get_students()
    matched_student = next((s for s in students_db if s.get("name", "").lower() == user_name.lower()), students_db[2] if len(students_db) > 2 else {})
    
    roll_no = matched_student.get("roll", "ECE_2026_042")
    dept = matched_student.get("department", "Electronics & Communication")
    sem = matched_student.get("semester", "Sem 5")
    attendance_pct = matched_student.get("attendance_percentage", 84.7)
    status = matched_student.get("exam_eligibility_status", "🟢 Safe (>75% Cutoff)")

    # 3. Top Metric Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(f'<div class="metric-card"><h3>{roll_no}</h3><p>Student Roll Number</p></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="metric-card"><h3>{attendance_pct}%</h3><p>Current Attendance</p></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="metric-card"><h3>{sem}</h3><p>Department & Term</p></div>', unsafe_allow_html=True)
    c4.markdown(f'<div class="metric-card"><h3>{status}</h3><p>Exam Eligibility Status</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 4. Course-Wise Attendance Passport Ledger Table
    st.markdown("### 📊 Course-Wise Attendance Passport Ledger")
    st.dataframe({
        "Course Code & Name": ["ECE301 - Digital Logic Design", "ECE302 - VLSI Architecture", "ECE303 - Signals & Systems", "ECE304 - Microcontrollers"],
        "Classes Held": [24, 22, 25, 20],
        "Classes Attended": [22, 19, 19, 17],
        "Percentage": ["91.6%", "86.3%", "76.0% (Warning)", "85.0%"],
        "Status": ["🟢 Excellent", "🟢 Good", "🟡 Monitor Closely", "🟢 Good"]
    }, use_container_width=True)

    st.markdown("---")

    # 5. Faculty & HOD Availability & Leave Status Board (Integrated from DB Allocations)
    st.markdown("### 🟢 Faculty & HOD Availability & Leave Status Tracker")
    st.markdown("Check real-time campus availability, office hours, and approved leave statuses for your department instructors.")

    faculty_allocations = PragyanDatabase.get_faculty_allocations()
    hod_records = PragyanDatabase.get_hod_records()

    # Build combined availability ledger table payload
    availability_rows = []
    
    # Add HOD records
    for hod in hod_records:
        availability_rows.append({
            "Name & Title": hod.get("hod_name", "Dr. HOD"),
            "Role & Department": f"HOD — {hod.get('department', 'ECE')}",
            "Status": hod.get("availability_status", "🟢 Available in Deanery"),
            "Cabin / Location": hod.get("deanery_office", "Block A, Room 102"),
            "Consultation Hours": "Tue & Thu: 10AM - 1PM"
        })
        
    # Add Faculty records
    for fac in faculty_allocations:
        availability_rows.append({
            "Name & Title": fac.get("faculty_name", "Dr. Faculty"),
            "Role & Department": f"Faculty — {fac.get('subject', 'Course')}",
            "Status": fac.get("availability_status", "🟢 Available in Cabin"),
            "Cabin / Location": fac.get("cabin_location", "Block B, Room 304"),
            "Consultation Hours": "Mon-Fri: 3PM - 5PM"
        })

    if availability_rows:
        st.dataframe({
            "Instructor Name": [r["Name & Title"] for r in availability_rows],
            "Role & Course": [r["Role & Department"] for r in availability_rows],
            "Campus Availability Status": [r["Status"] for r in availability_rows],
            "Cabin / Location": [r["Cabin / Location"] for r in availability_rows],
            "Consultation Hours": [r["Consultation Hours"] for r in availability_rows]
        }, use_container_width=True)
    else:
        st.info("No faculty availability records found.")

    st.markdown("---")

    # 6. Student Notice Board Live Viewer
    st.markdown("### 📢 Institutional Notice Board & Live Announcements")
    notices = st.session_state.get("institutional_notices", [
        {"id": 1, "title": "Mid-Semester Examination Attendance Mandate", "date": "2026-09-01", "author": "Dr. Principal (Executive Deanery)", "priority": "🔴 High", "content": "All students must maintain a strict 75% attendance record across all courses to qualify for upcoming mid-semester examinations starting later this month."},
        {"id": 2, "title": "IEEE Technical Paper Presentation Symposium", "date": "2026-08-28", "author": "Dr. HOD (ECE)", "priority": "🟡 Medium", "content": "ECE department students are invited to register for the upcoming national robotics and AI symposium hosted in Block C auditorium."}
    ])

    for notice in notices:
        st.markdown(
            f"""
            <div style="padding: 15px; border-radius: 8px; background-color: #1e293b; border-left: 5px solid #3b82f6; margin-bottom: 15px;">
                <h4 style="margin: 0; color: #f8fafc;">{notice['title']}</h4>
                <p style="margin: 5px 0 0 0; font-size: 0.85rem; color: #94a3b8;">
                    <b>Date:</b> {notice['date']} &nbsp;|&nbsp; <b>Author:</b> {notice['author']} &nbsp;|&nbsp; <b>Priority:</b> {notice['priority']}
                </p>
                <hr style="margin: 8px 0; border-color: #334155;">
                <p style="margin: 0; color: #e2e8f0; font-size: 0.95rem;">{notice['content']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
