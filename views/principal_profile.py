import streamlit as st
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_principal_profile():
    """
    Renders the dedicated Principal Profile & Executive Credentials view,
    allowing the principal to manage deanery office locations, institute-wide compliance bylaws,
    executive broadcast permissions, system notification settings, position start dates, professional links, and keen interests.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal")
    PragyanDatabase.initialize_database()
    
    # 2. Initialize or Retrieve Persistent Principal Executive Record in Session State
    if "principal_executive_profile_db" not in st.session_state:
        st.session_state.principal_executive_profile_db = {
            "full_name": user_name,
            "email": "principal@pragyan.edu",
            "employee_id": "EXEC_PRINCIPAL_2026_01",
            "admin_office": "Main Block - Executive Deanery & Council",
            "office_location": "Block A, Suite 101 (Central Administration)",
            "office_hours": "Mon, Wed, Fri: 11:00 AM - 2:00 PM",
            "position_start_date": datetime.date(2022, 7, 15),
            "resume_link": "https://pragyanai.edu/resumes/principal_cv.pdf",
            "linkedin_link": "https://linkedin.com/in/principal-dean-pragyanai",
            "research_profile": "https://scholar.google.com/citations?user=principal_sample",
            "keen_interests": "Agentic AI in Higher Education Governance, Automated EDA Verification, Institutional Scalability Models",
            "bio": "Principal & Chief Academic Officer. Directing institutional digital transformation, attendance intelligence compliance, and multi-department student success frameworks.",
            "digest_alerts": True,
            "sms_alerts": True,
            "broadcast_privilege": True,
            "pdf_logging": True
        }

    profile = st.session_state.principal_executive_profile_db

    st.markdown(f"## 🏛️ Principal's Executive Profile & Credentials — {profile['full_name']}")
    st.markdown(
        f"Manage your executive deanery profile, institutional administrative office credentials, "
        f"position start tenure, professional research profiles, and system-wide broadcast permissions."
    )
    
    st.info(
        "💡 **Executive Security Clearance:** Changes saved here apply directly across all institutional "
        "departments, student passports, and faculty compliance records."
    )

    st.markdown("---")

    # 3. Principal Profile Edit Form with Enhanced Fields
    with st.form("principal_profile_management_form"):
        st.markdown("### 📋 Principal & Executive Deanery Credentials")
        
        c1, c2 = st.columns(2)
        
        with c1:
            new_name = st.text_input("Full Name & Title", value=profile["full_name"])
            new_email = st.text_input("Institutional Email", value=profile["email"])
            new_emp_id = st.text_input("Executive Employee ID", value=profile["employee_id"])
            new_start_date = st.date_input("Date of Position Start", value=profile["position_start_date"])
            
        with c2:
            new_admin_office = st.text_input("Administrative Office", value=profile["admin_office"])
            new_office_loc = st.text_input("Office Location", value=profile["office_location"])
            new_office_hours = st.text_input("Council Office Hours", value=profile["office_hours"])

        st.markdown("#### 🔗 Professional Portfolios & Research Links")
        p1, p2, p3 = st.columns(3)
        with p1:
            new_resume = st.text_input("Resume / CV URL", value=profile["resume_link"])
        with p2:
            new_linkedin = st.text_input("LinkedIn Profile URL", value=profile["linkedin_link"])
        with p3:
            new_research = st.text_input("Google Research Profile URL", value=profile["research_profile"])

        new_interests = st.text_area(
            "🎯 Keen Research & Governance Interests",
            value=profile["keen_interests"],
            placeholder="Enter core research domains, academic interests, and institutional focus areas..."
        )
        
        new_bio = st.text_area(
            "Executive Leadership Bio", 
            value=profile["bio"]
        )

        st.markdown("---")
        st.markdown("### ⚙️ Institutional Policy & Executive Notification Preferences")
        
        nc1, nc2 = st.columns(2)
        with nc1:
            new_digest = st.checkbox("Receive Institute-Wide Attendance Compliance Digests", value=profile["digest_alerts"])
            new_sms = st.checkbox("Instant SMS/Email Alerts for Critical Shortage Escalations", value=profile["sms_alerts"])
        with nc2:
            new_broadcast = st.checkbox("Global Broadcast Privilege Across All Student Portals", value=profile["broadcast_privilege"])
            new_pdf = st.checkbox("Automated ReportLab PDF Audit Logging", value=profile["pdf_logging"])

        st.markdown("---")
        
        if st.form_submit_button("💾 Save Principal Profile Updates"):
            # Persist updates to session state database record
            st.session_state.principal_executive_profile_db = {
                "full_name": new_name,
                "email": new_email,
                "employee_id": new_emp_id,
                "admin_office": new_admin_office,
                "office_location": new_office_loc,
                "office_hours": new_office_hours,
                "position_start_date": new_start_date,
                "resume_link": new_resume,
                "linkedin_link": new_linkedin,
                "research_profile": new_research,
                "keen_interests": new_interests,
                "bio": new_bio,
                "digest_alerts": new_digest,
                "sms_alerts": new_sms,
                "broadcast_privilege": new_broadcast,
                "pdf_logging": new_pdf
            }
            st.session_state["user_name"] = new_name
            st.success(f"Executive profile, tenure start date, and institutional credentials for **{new_name}** updated and saved successfully!")
            st.rerun()
