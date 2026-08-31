import streamlit as st
from utils.styles import load_custom_css
from utils.helpers import render_brand_logo
from modules.sample_data import SampleDataGenerator
from modules.auth import init_session_state
from views.student_view import render_student_dashboard
from views.faculty_view import render_faculty_dashboard
from views.parent_view import render_parent_dashboard
from views.hod_view import render_hod_dashboard
from views.principal_view import render_principal_dashboard
from views.admin_view import render_admin_dashboard
from views.ai_chat import render_ai_chat_view
from views.leaves import render_leave_portal
from views.reports import render_reports_view
from views.profile import render_profile_view

# 1. Page Configuration
st.set_page_config(
    page_title="PragyanAI Attendance Intelligence",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Load Sleek Dark-Mode Custom CSS
load_custom_css()

# 3. Initialize Large-Scale Mock Dataset (6 Depts, 120 Faculty, 6k Students)
SampleDataGenerator.initialize_institutional_data()

# 4. Initialize Session State Variables
init_session_state()

def login_sidebar():
    """
    Renders the brand logo and secure login sidebar for authenticating 
    across all 6 institutional roles.
    """
    # Render Brand Logo safely at Top of Sidebar
    render_brand_logo(width=180, is_sidebar=True)
    
    st.sidebar.markdown("### *Attendance Intelligence*")
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("## 🔐 Secure Portal Login")
    role = st.sidebar.selectbox("Select Access Role", ["Student", "Faculty", "Parent", "HOD", "Principal", "Admin"])
    
    name_map = {
        "Student": "Sateesh Ambesange", 
        "Faculty": "Dr. Faculty 1 (Comp)", 
        "Parent": "Mr. Ambesange", 
        "HOD": "Dr. HOD (ECE)", 
        "Principal": "Dr. Principal", 
        "Admin": "System Admin"
    }
    
    user_name = st.sidebar.text_input("Full Name", value=name_map.get(role, "User"))
    email = st.sidebar.text_input("Institutional Email", value="user@pragyan.edu")
    password = st.sidebar.text_input("Password", type="password", value="••••••••")
    
    if st.sidebar.button("🚀 Authorize & Enter"):
        st.session_state.authenticated = True
        st.session_state.role = role
        st.session_state.user_name = user_name
        st.rerun()

def main():
    """
    Main application router managing authentication states and modular view navigation.
    """
    if not st.session_state.authenticated:
        # Welcome Hero Page if unauthenticated
        render_brand_logo(width=280, is_sidebar=False)
        st.markdown("# 🎓 PragyanAI Attendance Intelligence Platform")
        st.markdown("### *From Attendance Capture to Academic Intelligence. Capture. Analyse. Predict. Improve.*")
        st.markdown("---")
        st.info("💡 **Getting Started:** Please select your portal role and enter credentials in the sidebar to access your tailored dashboard.")
        login_sidebar()
        return

    # Render Brand Logo safely at Top of Authenticated Sidebar
    render_brand_logo(width=160, is_sidebar=True)
    st.sidebar.title(f"Portal: {st.session_state.role}")
    st.sidebar.markdown(f"**User:** {st.session_state.user_name}")
    st.sidebar.markdown("---")
    
    # Modular Multi-Page Navigation Hub
    page = st.sidebar.radio("Navigation Hub", [
        f"📊 {st.session_state.role} Dashboard", 
        "🤖 AI Chatbot Assistant", 
        "📝 Leave Applications & Approvals", 
        "📄 PDF Reports Center", 
        "👤 Personal Profile", 
        "🚪 Logout"
    ])

    # Handle Logout Action
    if page == "🚪 Logout":
        st.session_state.authenticated = False
        st.rerun()

    # Dynamic User-Wise View Routing
    dashboard_label = f"📊 {st.session_state.role} Dashboard"
    
    if page == dashboard_label:
        role = st.session_state.role
        if role == "Student":
            render_student_dashboard()
        elif role == "Faculty":
            render_faculty_dashboard()
        elif role == "Parent":
            render_parent_dashboard()
        elif role == "HOD":
            render_hod_dashboard()
        elif role == "Principal":
            render_principal_dashboard()
        elif role == "Admin":
            render_admin_dashboard()
            
    elif page == "🤖 AI Chatbot Assistant":
        render_ai_chat_view()
    elif page == "📝 Leave Applications & Approvals":
        render_leave_portal()
    elif page == "📄 PDF Reports Center":
        render_reports_view()
    elif page == "👤 Personal Profile":
        render_profile_view()

if __name__ == "__main__":
    main()
