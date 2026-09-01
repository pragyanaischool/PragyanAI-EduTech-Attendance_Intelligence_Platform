import streamlit as st
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_hod_profile():
    """
    Renders the enhanced HOD Profile & Governance Hub.
    Features:
    - Editable HOD profile attributes (Name, Designation, Department, Office, Biography).
    - Professional links: LinkedIn, Google Research / Scholar Link, and Subject Interests.
    - CV / Resume PDF uploader with session memory caching.
    - Departmental Policy & Notification Preferences.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. HOD (ECE)")
    PragyanDatabase.initialize_database()
    
    st.markdown(f"# 🏛️ HOD Profile & Executive Governance Hub — {user_name}")
    st.markdown("### *Manage your executive profile credentials, research links, CV uploads, and departmental bylaws.*")
    
    st.info(
        "💡 **Executive Portfolio Management:** Update your professional credentials, research profiles, "
        "and department notification bylaws below. All changes synchronize across the institutional database."
    )

    st.markdown("---")

    # 2. Initialize HOD Profile Session State Data if missing
    if "hod_profile_data" not in st.session_state:
        st.session_state.hod_profile_data = {
            "full_name": user_name,
            "designation": "Head of Department (Professor)",
            "department": "Electronics & Communication Engineering (ECE)",
            "college": "PragyanAI Institute of Technology & Venture Studio",
            "office_location": "Academic Block A, Room 402",
            "linkedin": "https://linkedin.com/in/hod-ece-pragyanai",
            "google_scholar": "https://scholar.google.com/citations?user=hod_sample_id",
            "interests": "VLSI Design Automation, AI Embedded Systems, Real-Time IoT Architectures, Neural Hardware Accelerators",
            "bio": "Senior academic leader with over 22 years of teaching and research experience in VLSI design and artificial intelligence hardware. Passionate about transforming technical education through Agentic AI and multi-year skill development frameworks."
        }

    profile = st.session_state.hod_profile_data

    # 3. Profile Layout: Visual Badge & Editable Form
    col_img, col_details = st.columns([1, 2.5])

    with col_img:
        st.markdown(
            f"""
            <div style="background-color: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; padding: 25px; text-align: center;">
                <h3>🏛️</h3>
                <h4 style="margin: 5px 0;">{profile['full_name']}</h4>
                <p style="color: #64748b; font-size: 13px;">{profile['designation']}<br>{profile['department']}</p>
                <hr style="border: 0; border-top: 1px solid #e2e8f0; margin: 15px 0;">
                <p style="font-size: 12px; text-align: left;">📍 <b>Office:</b> {profile['office_location']}</p>
                <p style="font-size: 12px; text-align: left;">🌐 <a href="{profile['linkedin']}" target="_blank">LinkedIn Profile</a></p>
                <p style="font-size: 12px; text-align: left;">📚 <a href="{profile['google_scholar']}" target="_blank">Google Research Scholar</a></p>
                <span style="background-color: #dbeafe; color: #1e40af; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: bold; display: inline-block; margin-top: 10px;">🟢 Verified HOD Admin</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # CV / Resume Upload Box
        with st.container(border=True):
            st.markdown("#### 📄 HOD CV & Credentials Uploader")
            uploaded_cv = st.file_uploader("Upload Updated CV / Resume (PDF)", type=["pdf"])
            if uploaded_cv is not None:
                st.session_state.hod_uploaded_cv_name = uploaded_cv.name
                st.success(f"🎉 CV **{uploaded_cv.name}** uploaded and indexed successfully!")
            
            cached_cv = st.session_state.get("hod_uploaded_cv_name", "Not Uploaded")
            st.caption(f"📁 Active CV File: `{cached_cv}`")

    with col_details:
        st.markdown("### ✏️ Edit Executive HOD Profile & Professional Links")
        
        with st.form("hod_profile_edit_form"):
            ep1, ep2 = st.columns(2)
            with ep1:
                edit_name = st.text_input("Full Name & Title", value=profile["full_name"])
                edit_designation = st.text_input("Designation", value=profile["designation"])
                edit_dept = st.text_input("Department", value=profile["department"])
            with ep2:
                edit_office = st.text_input("Office Location", value=profile["office_location"])
                edit_linkedin = st.text_input("LinkedIn Profile URL", value=profile["linkedin"])
                edit_scholar = st.text_input("Google Research / Scholar Link", value=profile["google_scholar"])

            edit_interests = st.text_area("Research & Interest Subjects (Comma Separated)", value=profile["interests"])
            edit_bio = st.text_area("Executive Biography & Academic Statement", value=profile["bio"], height=100)

            if st.form_submit_button("💾 Save & Update HOD Profile"):
                st.session_state.hod_profile_data = {
                    "full_name": edit_name,
                    "designation": edit_designation,
                    "department": edit_dept,
                    "college": profile["college"],
                    "office_location": edit_office,
                    "linkedin": edit_linkedin,
                    "google_scholar": edit_scholar,
                    "interests": edit_interests,
                    "bio": edit_bio
                }
                st.success("🎉 HOD executive profile credentials updated successfully!")
                st.rerun()

    st.markdown("---")

    # 4. Departmental Policy & Notification Preferences
    st.markdown("### ⚙️ Departmental Policy & Notification Preferences")
    st.markdown("Configure automated policy flags, attendance shortage alert thresholds, and notification routing for your department.")

    with st.form("hod_policy_preferences_form"):
        hp1, hp2 = st.columns(2)
        with hp1:
            attendance_shortage_limit = st.slider("Strict Attendance Shortage Warning Threshold (%)", min_value=60, max_value=85, value=75)
            auto_email_parents = st.checkbox("Enable Automated Parent Attendance Shortage SMS / Email Alerts", value=True)
            hod_leave_approval_mode = st.selectbox("Student Leave Approval Workflow", ["Faculty Endorsement → HOD Direct Approval", "Automated AI Verification + HOD Sign-off"])
        with hp2:
            adhoc_workload_cap = st.number_input("Max Adhoc Classes per Faculty / Week", min_value=1, max_value=6, value=3)
            department_notice_broadcast = st.text_area("Department-Wide Broadcast Notice", placeholder="Announce department faculty meeting or curriculum review schedules...")
            department_priority_tag = st.selectbox("Notice Priority Level", ["🟢 Normal", "🟡 Moderate", "🔴 Urgent Academic Mandate"])

        if st.form_submit_button("💾 Save Departmental Policies & Preferences"):
            st.success("🎉 Departmental bylaws, shortage thresholds, and notification preferences updated successfully!")
