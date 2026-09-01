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

# --- Import Parent Views ---
from views.parent_dashboard import render_parent_dashboard
from views.parent_profile import render_parent_profile
from views.parent_chat import render_parent_chat
from views.parent_analytics import render_parent_analytics

# --- Import Admin Seeder View ---
from views.admin_demo_seeder import render_admin_demo_seeder

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="PragyanAI Attendance Intelligence Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # 1. Initialize Central Database & Session State Defaults
    PragyanDatabase.initialize_database()

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
                "content": "All students must maintain a strict 75% attendance record across all courses to qualify for upcoming mid-semester examinations starting later this month."
            },
            {
                "id": 2, 
                "title": "IEEE Technical Paper Presentation Symposium", 
                "date": "2026-08-28", 
                "author": "Dr. HOD (ECE)", 
                "priority": "🟡 Medium", 
                "content": "ECE department students are invited to register for the upcoming national robotics and AI symposium hosted in Block C auditorium."
            }
        ]

    # 2. Sidebar Authentication & Role Switcher
    render_brand_logo(width=180, is_sidebar=True)
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔐 Role-Based Access Control")
    
    role_options = ["Student", "Faculty", "HOD", "Principal", "Parent", "⚙️ Admin / Demo Seeder"]
    current_role_index = role_options.index(st.session_state.role) if st.session_state.role in role_options else 0
    
    selected_role = st.sidebar.selectbox(
        "Select User Role", 
        role_options,
        index=current_role_index
    )
    
    if selected_role != st.session_state.role:
        st.session_state.role = selected_role
        default_names = {
            "Student": "Sateesh Ambesange",
            "Faculty": "Dr. Smitha Rao",
            "HOD": "Dr. HOD (ECE)",
            "Principal": "Dr. Principal",
            "Parent": "Mr. Ambesange (Guardian)",
            "⚙️ Admin / Demo Seeder": "System Administrator"
        }
        st.session_state.user_name = default_names.get(selected_role, "User")

    user_name = st.sidebar.text_input("Active User Name", value=st.session_state.user_name)
    st.session_state.user_name = user_name

    st.sidebar.markdown("---")
    
    # 3. Role-Specific Navigation Menus
    role = st.session_state.role
    
    if role == "Student":
        page = st.sidebar.radio("Navigation", ["Dashboard", "AI Advisor", "Analytics", "Profile", "Leaves", "Reports"])
    elif role == "Parent":
        page = st.sidebar.radio("Navigation", ["Dashboard", "Guardian AI Chat", "Analytics", "Profile"])
    elif role in ["Faculty", "HOD", "Principal"]:
        page = st.sidebar.radio("Navigation", ["Dashboard", "Analytics", "Profile", "Leaves", "Reports"])
    elif role == "⚙️ Admin / Demo Seeder":
        page = st.sidebar.radio("Navigation", ["Demo Seeder & DB Manager"])
    else:
        page = st.sidebar.radio("Navigation", ["Dashboard"])

    st.sidebar.markdown("---")
    st.sidebar.info(f"🟢 Active Session\n\n**User:** {user_name}\n**Role:** {role}")

    # 4. Central Routing Engine (Isolated View Dispatcher)
    if role == "Student":
        if page == "Dashboard": render_student_dashboard()
        elif page == "AI Advisor": render_student_chat()
        elif page == "Analytics": render_student_analytics()
        elif page == "Profile": render_student_profile()
        elif page == "Leaves": render_student_leaves()
        elif page == "Reports": render_student_reports()
        
    elif role == "Parent":
        if page == "Dashboard": render_parent_dashboard()
        elif page == "Guardian AI Chat": render_parent_chat()
        elif page == "Analytics": render_parent_analytics()
        elif page == "Profile": render_parent_profile()
        
    elif role == "Faculty":
        if page == "Dashboard": render_faculty_dashboard()
        elif page == "Analytics": render_faculty_analytics()
        elif page == "Profile": render_faculty_profile()
        elif page == "Leaves": render_faculty_leaves()
        elif page == "Reports": render_faculty_reports()
        
    elif role == "HOD":
        if page == "Dashboard": render_hod_dashboard()
        elif page == "Analytics": render_hod_analytics()
        elif page == "Profile": render_hod_profile()
        elif page == "Leaves": render_hod_leaves()
        elif page == "Reports": render_hod_reports()
        
    elif role == "Principal":
        if page == "Dashboard": render_principal_dashboard()
        elif page == "Analytics": render_principal_analytics()
        elif page == "Profile": render_principal_profile()
        elif page == "Leaves": render_principal_leaves()
        elif page == "Reports": render_principal_reports()
        
    elif role == "⚙️ Admin / Demo Seeder":
        render_admin_demo_seeder()

if __name__ == "__main__":
    main()
