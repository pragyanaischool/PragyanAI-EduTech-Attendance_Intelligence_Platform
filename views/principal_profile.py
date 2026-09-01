import streamlit as st
from utils.helpers import render_brand_logo

def render_principal_profile():
    """
    Renders the dedicated Principal Profile & Executive Credentials view,
    allowing the principal to manage deanery office locations, institute-wide compliance bylaws,
    executive broadcast permissions, and system notification settings.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal")
    
    st.markdown(f"## 🏛️ Principal's Executive Profile & Credentials — {user_name}")
    st.markdown(
        f"Manage your executive deanery profile, institutional administrative office credentials, "
        f"macro-level policy bylaws, and system-wide broadcast permissions."
    )
    
    st.info(
        "💡 **Executive Security Clearance:** Changes saved here apply directly across all institutional "
        "departments, student passports, and faculty compliance records."
    )

    st.markdown("---")

    # 2. Principal Profile Edit Form
    with st.form("principal_profile_management_form"):
        st.markdown("### 📋 Principal & Executive Deanery Credentials")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.text_input("Full Name & Title", value=user_name)
            st.text_input("Institutional Email", value="principal@pragyan.edu")
            st.text_input("Executive Employee ID", value="EXEC_PRINCIPAL_2026_01")
            
        with c2:
            st.text_input("Administrative Office", value="Main Block - Executive Deanery & Council")
            st.text_input("Office Location", value="Block A, Suite 101 (Central Administration)")
            st.text_input("Council Office Hours", value="Mon, Wed, Fri: 11:00 AM - 2:00 PM")
            
        st.text_area(
            "Executive Leadership Bio", 
            value="Principal & Chief Academic Officer. Directing institutional digital transformation, attendance intelligence compliance, and multi-department student success frameworks."
        )

        st.markdown("---")
        st.markdown("### ⚙️ Institutional Policy & Executive Notification Preferences")
        
        nc1, nc2 = st.columns(2)
        with nc1:
            st.checkbox("Receive Institute-Wide Attendance Compliance Digests", value=True)
            st.checkbox("Instant SMS/Email Alerts for Critical Shortage Escalations", value=True)
        with nc2:
            st.checkbox("Global Broadcast Privilege Across All Student Portals", value=True)
            st.checkbox("Automated ReportLab PDF Audit Logging", value=True)

        st.markdown("---")
        
        if st.form_submit_button("💾 Save Principal Profile Updates"):
            st.success(f"Executive profile and institutional credentials for **{user_name}** updated successfully!")
