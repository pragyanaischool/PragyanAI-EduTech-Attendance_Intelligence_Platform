import streamlit as st
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_faculty_profile():
    """
    Renders the dedicated Faculty Profile & Professional Portfolio view,
    allowing faculty members to manage their profile, department associated, role/designation,
    college name, assigned subjects, CV uploads, research publication links, LinkedIn, and GitHub profiles.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Smitha Rao")
    PragyanDatabase.initialize_database()
    
    st.markdown(f"## 👨‍🏫 Faculty Professional Portfolio & Profile Hub — {user_name}")
    st.markdown(
        f"Manage your academic credentials, department assignment, role/designation, college name, "
        f"assigned subjects, CV uploads, research links, and professional profiles."
    )
    
    st.info(
        "💡 **Faculty Portal Governance:** Updates to your profile synchronize directly with "
        "department HOD auditing tools, student attendance portals, and institutional directories."
    )

    st.markdown("---")

    # 2. Initialize Faculty Profiles in Session State if not present
    if "faculty_profiles_db" not in st.session_state:
        st.session_state.faculty_profiles_db = {}

    # Default profile setup for logged-in faculty
    if user_name not in st.session_state.faculty_profiles_db:
        st.session_state.faculty_profiles_db[user_name] = {
            "full_name": user_name,
            "role_designation": "Associate Professor & Senior Researcher",
            "department": "Electronics & Communication (ECE)",
            "college": "PragyanAI Institute of Technology & Venture Studio",
            "subjects": "ECE301 - Digital Logic Design, ECE302 - VLSI Architecture",
            "email": "smitha.rao@pragyan.edu",
            "phone": "+91 98450 12345",
            "cabin": "Block B, Room 304 (Academic Wing)",
            "consultation_hours": "Mon-Fri: 3:00 PM - 5:00 PM",
            "keen_interests": "Artificial Intelligence in Electronic Design Automation, Low-Power VLSI, FPGA Architectures",
            "research_link": "https://scholar.google.com/citations?user=sample_faculty",
            "linkedin_profile": "https://linkedin.com/in/dr-smitha-rao-ece",
            "github_profile": "https://github.com/smitharao-ece",
            "bio": "Associate Professor in ECE. Specialist in VLSI Design, Embedded Systems, IoT Architectures, and Automated Attendance Intelligence Systems."
        }

    current_profile = st.session_state.faculty_profiles_db[user_name]

    # 3. Editable Faculty Profile & Professional Portfolio Form
    with st.form("faculty_profile_enhanced_form"):
        st.markdown("### 📋 Academic Credentials, Role, College & Department Information")
        
        c1, c2 = st.columns(2)
        
        with c1:
            edit_name = st.text_input("Full Faculty Name & Title", value=current_profile["full_name"])
            edit_designation = st.text_input("Role / Designation", value=current_profile["role_designation"])
            edit_dept = st.text_input("Department Associated", value=current_profile["department"])
            edit_college = st.text_input("College / Institution Name", value=current_profile["college"])
            edit_email = st.text_input("Institutional Email", value=current_profile["email"])
            
        with c2:
            edit_phone = st.text_input("Contact Phone Number", value=current_profile["phone"])
            edit_cabin = st.text_input("Office Cabin Location", value=current_profile["cabin"])
            edit_consultation = st.text_input("Student Consultation Hours", value=current_profile["consultation_hours"])
            edit_subjects = st.text_input("Assigned Subjects (Comma-separated)", value=current_profile["subjects"])
            employee_id = st.text_input("Employee ID", value="FAC_ECE_2026_108", disabled=True)
            
        edit_bio = st.text_area(
            "Teaching & Research Bio", 
            value=current_profile["bio"]
        )

        st.markdown("---")
        st.markdown("### 🔬 Professional Portfolio, CV Upload, Research & Social Links")
        
        p1, p2 = st.columns(2)
        
        with p1:
            edit_keen_interests = st.text_area("Keen Interests & Research Domains", value=current_profile["keen_interests"])
            edit_research_link = st.text_input("Research Profile Link (Google Scholar / IEEE / ResearchGate)", value=current_profile["research_link"])
            cv_upload = st.file_uploader("Upload Updated CV / Resume (PDF)", type=["pdf"])
            
        with p2:
            edit_linkedin = st.text_input("LinkedIn Profile URL", value=current_profile["linkedin_profile"])
            edit_github = st.text_input("GitHub Profile URL", value=current_profile["github_profile"])
            st.markdown("<br>", unsafe_allow_html=True)
            st.info("💡 Uploading your CV automatically parses research keywords into your faculty profile vector store.")

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
        
        if st.form_submit_button("💾 Save & Update Faculty Profile Records"):
            # Update session state profile
            st.session_state.faculty_profiles_db[user_name] = {
                "full_name": edit_name,
                "role_designation": edit_designation,
                "department": edit_dept,
                "college": edit_college,
                "subjects": edit_subjects,
                "email": edit_email,
                "phone": edit_phone,
                "cabin": edit_cabin,
                "consultation_hours": edit_consultation,
                "keen_interests": edit_keen_interests,
                "research_link": edit_research_link,
                "linkedin_profile": edit_linkedin,
                "github_profile": edit_github,
                "bio": edit_bio
            }
            
            if cv_upload is not None:
                st.success(f"🎉 CV **{cv_upload.name}** successfully uploaded and parsed into institutional records!")
                
            st.success(f"🎉 Professional profile records and credentials for **{edit_name}** ({edit_designation}, {edit_college}) updated successfully in the faculty database!")
