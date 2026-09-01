import streamlit as st
import datetime
from utils.helpers import render_brand_logo

def render_student_leaves():
    """
    Renders the student leave application portal, allowing students 
    to submit medical exemptions, on-duty requests, and track approval statuses.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    
    st.markdown(f"# 📝 Student Leave Application Portal — {user_name}")
    st.markdown("### *Submit Medical Exemption Requests, On-Duty Applications, and Track Leave Statuses.*")
    
    st.info(
        "💡 **Leave Policy Notice:** Medical exemptions and on-duty requests must be submitted "
        "within 48 hours of return to campus. HOD approval is required for absences exceeding 3 days."
    )

    st.markdown("---")

    # 2. Leave Application Submission Form
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

    # 3. Submitted Leave Requests Tracking Ledger
    st.markdown("### 🗄️ Submitted Leave Applications Tracking Ledger")
    st.markdown("Review the real-time review status of all leave applications submitted from your student account.")
    
    default_leaves = [
        {"student": user_name, "type": "Medical Exemption", "from": "2026-08-10", "to": "2026-08-12", "reason": "Viral Fever (Doctor prescription attached)", "status": "🟢 Approved by HOD"}
    ]
    
    leaves_data = st.session_state.get("student_leave_requests", default_leaves)
    if leaves_data:
        st.dataframe(leaves_data, use_container_width=True)
    else:
        st.info("No leave requests submitted yet.")
