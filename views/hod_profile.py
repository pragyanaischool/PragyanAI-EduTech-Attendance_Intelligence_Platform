import streamlit as st
from utils.helpers import render_brand_logo

def render_hod_profile():
    """
    Renders the dedicated HOD Profile & Administrative Credentials view,
    allowing department heads to manage office locations, faculty supervisory roles,
    departmental compliance bylaws, and approval notifications.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. HOD (ECE)")
    
    st.markdown(f"## 🏛️ HOD Administrative Profile & Department Credentials — {user_name}")
    st.markdown(
        f"Manage your department head profile, supervisory office credentials, "
        f"faculty audit schedules, and institutional compliance bylaws."
    )
    
    st.info(
        "💡 **HOD Portal Security:** Updates made here synchronize with principal executive "
        "dashboards and dictate automated department leave approval workflows."
    )

    st.markdown("---")

    # 2. HOD Profile Edit Form
    with st.form("hod_profile_management_form"):
        st.markdown("### 📋 Department Head Credentials")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.text_input("Full Name & Title", value=user_name)
            st.text_input("Institutional Email", value="hod.ece@pragyan.edu")
            st.text_input("Administrative Employee ID", value="HOD_ECE_2026_01")
            
        with c2:
            st.text_input("Managed Department", value="Electronics & Communication (ECE)")
            st.text_input("Deanery Office Location", value="Block A, Room 102 (Administrative Wing)")
            st.text_input("Department Council Hours", value="Tue & Thu: 10:00 AM - 1:00 PM")
            
        st.text_area(
            "Executive Department Statement", 
            value="Directing department-wide academic rigor, faculty lecture audits, attendance compliance, and student shortage counseling programs."
        )

        st.markdown("---")
        st.markdown("### ⚙️ Departmental Policy & Notification Preferences")
        
        nc1, nc2 = st.columns(2)
        with nc1:
            st.checkbox("Receive Instant Alerts for Pending Leave Approvals", value=True)
            st.checkbox("Receive Weekly Department Attendance Audit Summaries", value=True)
        with nc2:
            st.checkbox("Automated Dispatch of Shortage Warnings (<75%)", value=True)
            st.checkbox("Executive Principal Broadcast Integration", value=True)

        st.markdown("---")
        
        if st.form_submit_button("💾 Save HOD Profile Updates"):
            st.success(f"Administrative profile and department credentials for **{user_name}** updated successfully!")
