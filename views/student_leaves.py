import streamlit as st
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_student_leaves():
    """
    Renders the student leave application portal, institutional authority leave status board 
    (HOD, Subject Faculty, and Principal), monthly leave history filters, and application tracking.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    PragyanDatabase.initialize_database()
    
    st.markdown(f"# 📝 Student Leave Application & Authority Status Hub — {user_name}")
    st.markdown("### *Submit Leave Requests, Track Approval Statuses, and Check Department HOD, Faculty, & Principal Availability.*")
    
    st.info(
        "💡 **Leave Policy Notice:** Medical exemptions and on-duty requests must be submitted "
        "within 48 hours of return. HOD approval is required for absences exceeding 3 days."
    )

    st.markdown("---")

    # 2. Institutional Authority Leave & Availability Status Board (Fetched from DB)
    st.markdown("### 🏛️ Institutional Authority Leave & Availability Status Board")
    st.markdown("Real-time campus presence and approved leave schedules of your Department HOD, Subject Instructors, and Principal.")

    hod_records = PragyanDatabase.get_hod_records()
    faculty_allocations = PragyanDatabase.get_faculty_allocations()

    authority_rows = []
    
    # Add Principal Record
    authority_rows.append({
        "Authority Name": "Dr. Principal",
        "Role & Department": "Executive Deanery — Institutional Principal",
        "Campus Availability": "🟢 Available in Central Office",
        "Scheduled Leave Status": "No Active Leave Scheduled"
    })

    # Add HOD Records
    for hod in hod_records:
        authority_rows.append({
            "Authority Name": hod.get("hod_name", "Dr. HOD"),
            "Role & Department": f"HOD — {hod.get('department', 'ECE')}",
            "Campus Availability": hod.get("availability_status", "🟢 Available in Deanery"),
            "Scheduled Leave Status": "On Duty (Active)"
        })

    # Add Relevant Subject Faculty Records
    for fac in faculty_allocations:
        authority_rows.append({
            "Authority Name": fac.get("faculty_name", "Dr. Faculty"),
            "Role & Department": f"Subject Faculty — {fac.get('subject', 'Course')}",
            "Campus Availability": fac.get("availability_status", "🟢 Available in Cabin"),
            "Scheduled Leave Status": "Regular Teaching Schedule"
        })

    if authority_rows:
        st.dataframe({
            "Authority Name": [r["Authority Name"] for r in authority_rows],
            "Role & Department": [r["Role & Department"] for r in authority_rows],
            "Campus Availability": [r["Campus Availability"] for r in authority_rows],
            "Leave / Duty Status": [r["Scheduled Leave Status"] for r in authority_rows]
        }, use_container_width=True)

    st.markdown("---")

    # 3. Leave Application Submission Form
    with st.form("student_leave_application_form"):
        st.markdown("### 📋 New Leave Application Form")
        
        c1, c2 = st.columns(2)
        with c1:
            leave_type = st.selectbox(
                "Leave Category", 
                ["Medical Exemption", "On-Duty (Conference / Hackathon / Sports)", "Personal Leave", "Bereavement Leave"]
            )
            start_date = st.date_input("Start Date", value=datetime.date.today())
            
        with c2:
            end_date = st.date_input("End Date", value=datetime.date.today() + datetime.timedelta(days=1))
            supporting_doc = st.file_uploader(
                "Upload Supporting Certificate / Prescription / Approval (PDF/JPG)", 
                type=["pdf", "png", "jpg"]
            )
            
        reason = st.text_area(
            "Detailed Reason for Absence", 
            placeholder="Explain reason for leave and specify affected course codes..."
        )

        st.markdown("---")
        
        if st.form_submit_button("🚀 Submit Leave Application for HOD Review"):
            if not reason.strip():
                st.error("Please provide a detailed reason for your absence before submitting.")
            else:
                if "student_leave_requests" not in st.session_state:
                    st.session_state.student_leave_requests = []
                
                new_req = {
                    "student": user_name,
                    "type": leave_type,
                    "from": str(start_date),
                    "to": str(end_date),
                    "reason": reason,
                    "status": "🟡 Pending HOD Review"
                }
                st.session_state.student_leave_requests.insert(0, new_req)
                st.success(f"🎉 **{leave_type}** application successfully submitted to Department HOD for review!")

    st.markdown("---")

    # 4. Submitted Leave Requests Tracking Ledger with Monthly Filter
    st.markdown("### 🗄️ Submitted Leave Applications Tracking Ledger & Monthly Filter")
    
    default_leaves = [
        {"student": user_name, "type": "Medical Exemption", "from": "2026-08-10", "to": "2026-08-12", "reason": "Viral Fever (Doctor prescription attached)", "status": "🟢 Approved by HOD"},
        {"student": user_name, "type": "On-Duty", "from": "2026-07-15", "to": "2026-07-16", "reason": "National Robotics Symposium", "status": "🟢 Approved by HOD"}
    ]
    
    leaves_data = st.session_state.get("student_leave_requests", default_leaves)

    # Monthly Filter Control
    fc1, fc2 = st.columns([2, 4])
    with fc1:
        month_filter = st.selectbox(
            "Filter Past Leaves by Month", 
            ["All Months", "August 2026", "July 2026", "June 2026", "May 2026"]
        )

    # Filter logic based on start date string matching
    filtered_leaves = leaves_data
    if month_filter == "August 2026":
        filtered_leaves = [l for l in leaves_data if "2026-08" in l.get("from", "")]
    elif month_filter == "July 2026":
        filtered_leaves = [l for l in leaves_data if "2026-07" in l.get("from", "")]
    elif month_filter == "June 2026":
        filtered_leaves = [l for l in leaves_data if "2026-06" in l.get("from", "")]
    elif month_filter == "May 2026":
        filtered_leaves = [l for l in leaves_data if "2026-05" in l.get("from", "")]

    if filtered_leaves:
        st.dataframe(filtered_leaves, use_container_width=True)
    else:
        st.info(f"No leave applications found for **{month_filter}**.")
