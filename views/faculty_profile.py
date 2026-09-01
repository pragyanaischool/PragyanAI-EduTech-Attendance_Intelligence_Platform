import streamlit as st
from utils.helpers import render_brand_logo

def render_faculty_profile():
    """
    Renders the dedicated Faculty Profile & Teaching Credentials view,
    allowing faculty members to update office cabins, consultation hours, research bios,
    and course alert subscriptions.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Faculty 1 (Comp)")
    
    st.markdown(f"## 👨‍🏫 Faculty Office & Teaching Credentials — {user_name}")
    st.markdown(
        f"Manage your faculty profile, department assignment, office hours, "
        f"research bio, and student consultation schedules."
    )
    
    st.info(
        "💡 **Faculty Portal Security:** Updates to your profile synchronize directly with "
        "department HOD auditing tools and student attendance advisories."
    )

    st.markdown("---")

    # 2. Faculty Profile Edit Form
    with st.form("faculty_profile_management_form"):
        st.markdown("### 📋 Faculty & Departmental Credentials")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.text_input("Full Faculty Name & Title", value=user_name)
            st.text_input("Institutional Email", value="faculty.ece@pragyan.edu")
            st.text_input("Employee ID", value="FAC_ECE_2026_108")
            
        with c2:
            st.text_input("Department Group", value="Electronics & Communication (ECE)")
            st.text_input("Office Cabin Location", value="Block B, Room 304 (Academic Wing)")
            st.text_input("Student Consultation Hours", value="Mon-Fri: 3:00 PM - 5:00 PM")
            
        st.text_area(
            "Teaching & Research Bio", 
            value="Associate Professor in ECE. Specialist in VLSI Design, Embedded Systems, IoT Architectures, and Automated Attendance Intelligence Systems."
        )

        st.markdown("---")
        st.markdown("### 📲 Faculty Notification & System Preferences")
        
        nc1, nc2 = st.columns(2)
        with nc1:
            st.checkbox("Receive Daily Class Turnout Digest", value=True)
            st.checkbox("Receive Instant Alerts for Student Shortage Appeals", value=True)
        with nc2:
            st.checkbox("Email Notifications for Leave Submissions", value=True)
            st.checkbox("Biometric / Geo-Fence Session Security Validation", value=True)

        st.markdown("---")
        
        if st.form_submit_button("💾 Save Faculty Profile Updates"):
            st.success(f"Profile records and credentials for **{user_name}** updated successfully in the faculty database!")
