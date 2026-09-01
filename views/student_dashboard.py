import streamlit as st
from utils.helpers import render_brand_logo

def render_student_dashboard():
    """
    Renders the dedicated Student Attendance Dashboard with safe brand logo rendering,
    macro metric summary cards, course attendance ledgers, and live institutional notice boards.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    
    st.markdown(f"# 🎒 Student Attendance Intelligence Hub — {user_name}")
    st.markdown("### *Real-Time Attendance Passport, Course Ledger, and Institutional Notices.*")

    # 2. Top Metric Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(f'<div class="metric-card"><h3>{user_name}</h3><p>Student Name & ID</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>84.7%</h3><p>Current Attendance</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>ECE (Sem 5)</h3><p>Department & Term</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>🟢 Safe Status</h3><p>Exam Eligibility (>75%)</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 3. Course-Wise Attendance Ledger Table
    st.markdown("### 📊 Course-Wise Attendance Passport Ledger")
    st.dataframe({
        "Course Code & Name": ["ECE301 - Digital Logic Design", "ECE302 - VLSI Architecture", "ECE303 - Signals & Systems", "ECE304 - Microcontrollers"],
        "Classes Held": [24, 22, 25, 20],
        "Classes Attended": [22, 19, 19, 17],
        "Percentage": ["91.6%", "86.3%", "76.0% (Warning)", "85.0%"],
        "Status": ["🟢 Excellent", "🟢 Good", "🟡 Monitor Closely", "🟢 Good"]
    }, use_container_width=True)

    st.markdown("---")

    # 4. Student Notice Board Live Viewer
    st.markdown("### 📢 Institutional Notice Board & Live Announcements")
    st.markdown("Stay updated with official exam notices, departmental circulars, and attendance mandates.")

    # Access shared notices from session state with default fallback
    notices = st.session_state.get("institutional_notices", [
        {"id": 1, "title": "Mid-Semester Examination Attendance Mandate", "date": "2026-09-01", "author": "Dr. Principal", "priority": "🔴 High", "content": "All students must maintain a strict 75% attendance record to qualify for upcoming mid-semester examinations. No exemptions without valid medical certificates."},
        {"id": 2, "title": "IEEE Technical Paper Presentation", "date": "2026-08-28", "author": "Dr. HOD (ECE)", "priority": "🟡 Medium", "content": "ECE department students are invited to register for the upcoming national robotics and AI symposium in Block C."}
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
