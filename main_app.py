import streamlit as st
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

# --- Import Student Views ---
from views.student_dashboard import render_student_dashboard
from views.student_profile import render_student_profile
from views.student_chat import render_student_chat
from views.student_leaves import render_student_leaves
from views.student_reports import render_student_reports
from views.student_analytics import render_student_analytics

# --- Import Faculty Views ---
from views.faculty_dashboard import render_faculty_dashboard
from views.faculty_profile import render_faculty_profile
from views.faculty_chat import render_faculty_chat
from views.faculty_leaves import render_faculty_leaves
from views.faculty_reports import render_faculty_reports
from views.faculty_analytics import render_faculty_analytics

# --- Import HOD Views ---
from views.hod_dashboard import render_hod_dashboard
from views.hod_profile import render_hod_profile
from views.hod_dept_profile import render_hod_dept_profile
from views.hod_chat import render_hod_chat
from views.hod_leaves import render_hod_leaves
from views.hod_reports import render_hod_reports
from views.hod_analytics import render_hod_analytics

# --- Import Principal Views ---
from views.principal_dashboard import render_principal_dashboard
from views.principal_profile import render_principal_profile
from views.principal_chat import render_principal_chat
from views.principal_leaves import render_principal_leaves
from views.principal_reports import render_principal_reports
from views.principal_analytics import render_principal_analytics

# --- Import New Principal College Views ---
from views.principal_college_profile import render_principal_college_profile
from views.college_calendar import render_college_calendar
from views.college_faculty import render_college_faculty
from views.college_analytics import render_college_analytics
from views.college_chatbot import render_college_chatbot

# --- Import Parent Views ---
from views.parent_dashboard import render_parent_dashboard
from views.parent_profile import render_parent_profile
from views.parent_chat import render_parent_chat
from views.parent_analytics import render_parent_analytics

# --- Import Admin Seeder View ---
from views.admin_demo_seeder import render_admin_demo_seeder

# --- Streamlit Page Configuration ---
st.image("assets/PragyanAI_Transperent.png")
st.set_page_config(
    page_title="PragyanAI Attendance Intelligence Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

def render_login_portal():
    """Renders a secure institutional login gate for all user roles."""
    render_brand_logo(width=280, is_sidebar=False)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h2 style='text-align: center;'>🔐 PragyanAI Universal Login Gate</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #94a3b8;'>Select your institutional role and enter credentials to access your portal.</p>", unsafe_allow_html=True)
        
        with st.form("institutional_login_form"):
            selected_role = st.selectbox(
                "Select User Persona", 
                ["Student", "Faculty", "HOD", "Principal", "Parent", "⚙️ Admin / Demo Seeder"]
            )
            
            # Default mock credentials helper text
            default_user_map = {
                "Student": ("Sateesh Ambesange", "student2026"),
                "Faculty": ("Dr. Smitha Rao", "faculty101"),
                "HOD": ("Dr. HOD (ECE)", "hod2026"),
                "Principal": ("Dr. Principal Dean", "principal1"),
                "Parent": ("Mr. Ambesange (Guardian)", "parent42"),
                "⚙️ Admin / Demo Seeder": ("System Administrator", "adminpass")
            }
            
            suggested_name, suggested_pass = default_user_map.get(selected_role, ("User", "password"))
            
            username_input = st.text_input("Institutional ID / Name", value=suggested_name)
            password_input = st.text_input("Secure Passkey", type="password", value=suggested_pass)
            
            submitted = st.form_submit_button("🚀 Secure Login to Portal")
            if submitted:
                st.session_state.authenticated = True
                st.session_state.role = selected_role
                st.session_state.user_name = username_input
                st.success(f"Authentication successful! Welcome to PragyanAI, **{username_input}**.")
                st.rerun()

def main():
    PragyanDatabase.initialize_database()

    # Authentication state initialization
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "role" not in st.session_state:
        st.session_state.role = "Student"
    if "user_name" not in st.session_state:
        st.session_state.user_name = "Sateesh Ambesange"
    if "institutional_notices" not in st.session_state:
        st.session_state.institutional_notices = [
            {
                "id": 1, 
                "title": "Mid-Semester Examination Attendance Mandate", 
                "date": "2026-09-01", 
                "author": "Dr. Principal (Executive Deanery)", 
                "priority": "🔴 High", 
                "content": "All students must maintain a strict 75% attendance record across all courses to qualify for upcoming mid-semester examinations."
            }
        ]

    # If not authenticated, render login gate
    if not st.session_state.authenticated:
        render_login_portal()
        return

    # --- Authenticated Sidebar Navigation ---
    render_brand_logo(width=180, is_sidebar=True)
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🟢 Active Session")
    st.sidebar.info(f"**User:** {st.session_state.user_name}\n\n**Role:** {st.session_state.role}")
    
    if st.sidebar.button("🚪 Logout / Switch Role"):
        st.session_state.authenticated = False
        st.rerun()

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🧭 Portal Navigation")
    
    role = st.session_state.role
    
    # Role-Specific Navigation Routing
    if role == "Student":
        page = st.sidebar.radio("Navigation", ["Dashboard", "Profile", "Leaves", "Analytics", "AI Advisor", "Reports"])
    elif role == "Faculty":
        page = st.sidebar.radio("Navigation", ["Dashboard", "Profile", "Leaves", "Analytics", "Faculty AI Chat", "Report"])
    elif role == "Parent":
        page = st.sidebar.radio("Navigation", ["Dashboard", "Guardian AI Chat", "Analytics", "Profile"])
    elif role == "HOD":
        page = st.sidebar.radio("Navigation", ["Dashboard", "Profile", "Dept Profile", "Leaves", "Analytics", "HOD AI Chat", "Report"])
    elif role == "Principal":
        page = st.sidebar.radio(
            "Navigation", 
            [
                "Dashboard",
                "Profile",
                "College Profile",
                "College Calender",
                "College Faculty Page",
                "Leaves",
                "College Analytics",
                "College AI ChatBot",
                "Reports"
            ]
        )
    elif role == "⚙️ Admin / Demo Seeder":
        page = st.sidebar.radio("Navigation", ["Demo Seeder & DB Manager"])
    else:
        page = st.sidebar.radio("Navigation", ["Dashboard"])

    # --- Central Routing Dispatcher ---
    if role == "Student":
        if page == "Dashboard": render_student_dashboard()
        elif page == "Profile": render_student_profile()
        elif page == "Leaves": render_student_leaves()
        elif page == "Analytics": render_student_analytics()
        elif page == "AI Advisor": render_student_chat()
        elif page == "Reports": render_student_reports()
        
    elif role == "Parent":
        if page == "Dashboard": render_parent_dashboard()
        elif page == "Guardian AI Chat": render_parent_chat()
        elif page == "Analytics": render_parent_analytics()
        elif page == "Profile": render_parent_profile()
        
    elif role == "Faculty":
        if page == "Dashboard": render_faculty_dashboard()
        elif page == "Profile": render_faculty_profile()
        elif page == "Leaves": render_faculty_leaves()
        elif page == "Analytics": render_faculty_analytics()
        elif page == "Faculty AI Chat": render_faculty_chat()
        elif page == "Report": render_faculty_reports()
        
    elif role == "HOD":
        if page == "Dashboard": render_hod_dashboard()
        elif page == "Profile": render_hod_profile()
        elif page == "Dept Profile": render_hod_dept_profile()
        elif page == "Leaves": render_hod_leaves()
        elif page == "Analytics": render_hod_analytics()
        elif page == "HOD AI Chat": render_hod_chat()
        elif page == "Report": render_hod_reports()
        
    elif role == "Principal":
        if page == "Dashboard": render_principal_dashboard()
        elif page == "Profile": render_principal_profile()
        elif page == "College Profile": render_principal_college_profile()
        elif page == "College Calender": render_college_calendar()
        elif page == "College Faculty Page": render_college_faculty()
        elif page == "Leaves": render_principal_leaves()
        elif page == "College Analytics": render_college_analytics()
        elif page == "College AI ChatBot": render_college_chatbot()
        elif page == "Reports": render_principal_reports()
        
    elif role == "⚙️ Admin / Demo Seeder":
        render_admin_demo_seeder()

if __name__ == "__main__":
    main()
