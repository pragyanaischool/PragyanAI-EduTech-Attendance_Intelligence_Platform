import streamlit as st
from utils.helpers import render_brand_logo

def render_student_leaves():
    """
    Renders the dedicated Student Leave Application & Tracking portal,
    enabling students to apply for medical/personal leaves and track HOD approval statuses.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    
    st.markdown(f"## 📝 Student Leave Application & Tracking Portal — {user_name}")
    st.markdown("Submit medical leave applications, attach recovery certificates, and track approval status in real time.")

    st.markdown("---")

    # 2. Leave Application Form
    col_l1, col_l2 = st.columns(2)
    
    with col_l1:
        st.markdown("### 📤 Submit New Leave Request")
        with st.form("student_leave_form"):
            leave_type = st.selectbox("Leave Classification", ["Medical Leave (Illness / Recovery)", "Personal Emergency", "Official University Event / Sports"])
            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date")
            reason_text = st.text_area("Reason & Medical Justification", placeholder="Describe reason for absence...")
            cert_file = st.file_uploader("Upload Medical Certificate / Supporting Document (PDF/JPG)", type=["pdf", "png", "jpg"])
            
            if st.form_submit_button("🚀 Submit Application to HOD"):
                if reason_text.strip():
                    st.success("Leave application successfully submitted and routed to the Department HOD for review!")
                else:
                    st.error("Please provide a reason for your leave.")

    with col_l2:
        st.markdown("### 📋 Leave Application History & Status")
        st.info(
            "**Request #LN-2026-04:**\n\n"
            "• **Duration:** Sep 2 to Sep 4, 2026\n"
            "• **Type:** Medical Leave (Viral Fever Recovery)\n"
            "• **Status:** ✅ Approved by HOD (ECE)\n"
            "• **Attendance Grace Applied:** 3 Days Exemption Credited"
        )
        st.markdown("---")
        st.info(
            "**Request #LN-2026-01:**\n\n"
            "• **Duration:** Aug 10 to Aug 11, 2026\n"
            "• **Type:** Personal Emergency\n"
            "• **Status:** ✅ Approved by Faculty Advisor"
        )
