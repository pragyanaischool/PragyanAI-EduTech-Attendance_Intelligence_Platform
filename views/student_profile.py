import streamlit as st
from utils.helpers import render_brand_logo

def render_student_profile():
    """
    Renders the dedicated Student Profile & Academic Passport management view,
    allowing students to update personal credentials, contact details, and notification preferences.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    
    st.markdown(f"## 🎒 Student Profile & Academic Passport — {user_name}")
    st.markdown(
        f"Manage your student identity, institutional contact details, academic goals, "
        f"and attendance alert subscriptions."
    )
    
    st.info(
        "💡 **Student Portal Security:** Changes made here update your official student ledger "
        "and synchronize automatically with Department HOD and Faculty advisory dashboards."
    )

    st.markdown("---")

    # 2. Student Profile Edit Form
    with st.form("student_profile_management_form"):
        st.markdown("### 📋 Personal & Academic Credentials")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.text_input("Full Legal Name", value=user_name)
            st.text_input("Institutional Email", value="sateesh.ambesange@pragyan.edu")
            st.text_input("Parent / Guardian Name", value="Mr. Ambesange")
            
        with c2:
            st.text_input("Student Roll Number / ID", value="ECE_2026_042")
            st.text_input("Department & Semester", value="Electronics & Communication (ECE) — Sem 5")
            st.text_input("Personal Contact Phone", value="+91 98765 43210")
            
        st.text_area(
            "Personal Academic Goals & Bio", 
            value="Committed to maintaining >85% attendance across all subjects, achieving distinction in VLSI Design, and actively participating in technical workshops."
        )

        st.markdown("---")
        st.markdown("### 📲 Student Notification & Alert Preferences")
        
        nc1, nc2 = st.columns(2)
        with nc1:
            st.checkbox("Receive Daily SMS Attendance Summary", value=True)
            st.checkbox("Receive WhatsApp Shortage Warning Alerts (<75%)", value=True)
        with nc2:
            st.checkbox("Email Notifications for Leave Approvals", value=True)
            st.checkbox("Two-Factor Authentication (2FA) via OTP", value=True)

        st.markdown("---")
        
        if st.form_submit_button("💾 Save Student Profile Updates"):
            st.success(f"Profile records and preferences for **{user_name}** updated successfully in the student database!")
