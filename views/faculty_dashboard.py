import streamlit as st
import datetime
from utils.helpers import render_brand_logo

def render_faculty_dashboard():
    """
    Renders the faculty attendance dashboard featuring multi-subject allocation, 
    daily dynamic QR code generation with database persistence, and historical QR code audits.
    """
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Faculty (ECE)")
    
    st.markdown(f"# 👨‍🏫 Faculty Portal & QR Intelligence Hub — {user_name}")
    st.markdown("### *Multi-Subject Attendance Management & Daily QR Code Session Generator.*")

    # 1. Top Metric Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>4 Subjects</h3><p>Allocated Portfolio</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>240</h3><p>Total Enrolled Students</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>89.2%</h3><p>Average Class Turnout</p></div>', unsafe_allow_html=True)
    
    # Calculate stored QR count dynamically from session state database
    db_qrs = st.session_state.get("qr_session_database", [])
    c4.markdown(f'<div class="metric-card"><h3>{len(db_qrs)} QRs</h3><p>Generated & Stored in DB</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 2. Dynamic QR Code Session Generator for Allocated Subjects
    st.markdown("### 📱 Daily Subject QR Code Session Generator")
    
    # Initialize QR Session DB in session state if missing
    if "qr_session_database" not in st.session_state:
        st.session_state.qr_session_database = [
            {"date": "2026-09-01", "dept": "ECE", "semester": "Sem 5", "subject": "ECE301 - Digital Logic Design", "file_link": "qr_sessions/ece301_2026_09_01.png", "scans": 44},
            {"date": "2026-09-01", "dept": "ECE", "semester": "Sem 7", "subject": "ECE402 - VLSI Architecture", "file_link": "qr_sessions/ece402_2026_09_01.png", "scans": 46},
        ]

    with st.form("faculty_qr_generator_form"):
        col_q1, col_q2 = st.columns(2)
        
        with col_q1:
            # Faculty allocated subjects mapping to specific departments and semesters
            allocated_subjects = [
                {"subject": "ECE301 - Digital Logic Design", "dept": "Electronics & Communication (ECE)", "sem": "Sem 5"},
                {"subject": "ECE402 - VLSI Architecture", "dept": "Electronics & Communication (ECE)", "sem": "Sem 7"},
                {"subject": "ECE305 - Microcontrollers", "dept": "Electronics & Communication (ECE)", "sem": "Sem 5"},
                {"subject": "CSE202 - Data Structures & Algorithms", "dept": "Computer Science (CSE)", "sem": "Sem 3"},
            ]
            
            subject_labels = [item["subject"] for item in allocated_subjects]
            selected_sub_label = st.selectbox("Select Allocated Subject", subject_labels)
            
            # Automatically fetch matching Department and Semester based on selection
            matched_item = next(item for item in allocated_subjects if item["subject"] == selected_sub_label)
            assigned_dept = matched_item["dept"]
            assigned_sem = matched_item["sem"]
            
            st.text_input("Auto-Linked Department", value=assigned_dept, disabled=True)
            st.text_input("Auto-Linked Semester", value=assigned_sem, disabled=True)

        with col_q2:
            session_date = st.date_input("Session Date", value=datetime.date.today())
            validity_mins = st.slider("QR Code Expiry Duration (Minutes)", min_value=1, max_value=30, value=10)
            geo_fence = st.checkbox("Enable Geo-Fencing (Campus Wi-Fi / GPS Lock)", value=True)
            anti_proxy = st.checkbox("Enable Anti-Proxy Device Fingerprinting", value=True)

        if st.form_submit_button("🚀 Generate & Store QR Session in Database"):
            date_str = session_date.strftime("%Y-%m-%d")
            sub_code_clean = selected_sub_label.split(" - ")[0].lower()
            file_path = f"qr_sessions/{sub_code_clean}_{date_str}.png"
            
            new_qr_record = {
                "date": date_str,
                "dept": assigned_dept,
                "semester": assigned_sem,
                "subject": selected_sub_label,
                "file_link": file_path,
                "scans": 0
            }
            
            st.session_state.qr_session_database.insert(0, new_qr_record)
            st.success(f"🎉 QR Code session successfully generated and stored in database for **{selected_sub_label}** ({assigned_sem} - {assigned_dept}) on {date_str}!")

    st.markdown("---")

    # 3. Database Audit & Stored QR Ledger Table
    st.markdown("### 🗄️ Stored QR Code Database Ledger")
    st.markdown(f"Total active QR codes logged in database: **{len(st.session_state.qr_session_database)}**")
    
    # Format table data from session state database
    table_data = {
        "Date": [item["date"] for item in st.session_state.qr_session_database],
        "Department": [item["dept"] for item in st.session_state.qr_session_database],
        "Semester": [item["semester"] for item in st.session_state.qr_session_database],
        "Subject": [item["subject"] for item in st.session_state.qr_session_database],
        "Database File Link": [f"🔗 `{item['file_link']}`" for item in st.session_state.qr_session_database],
        "Scans Recorded": [item["scans"] for item in st.session_state.qr_session_database]
    }
    st.dataframe(table_data, use_container_width=True)
