import streamlit as st

class RBACManager:
    # Role permissions mapping matrix
    PERMISSIONS = {
        "Student": ["mark_attendance", "view_own_attendance", "submit_leave", "ai_chat", "view_profile"],
        "Faculty": ["create_qr", "view_class_analytics", "view_own_analytics", "submit_leave", "approve_leave", "ai_chat", "view_profile"],
        "Parent": ["view_ward_attendance", "receive_alerts", "submit_leave", "ai_chat", "view_profile"],
        "HOD": ["create_qr", "view_department_analytics", "approve_leave", "ai_chat", "view_profile", "download_pdf"],
        "Principal": ["view_institute_analytics", "approve_leave", "ai_chat", "view_profile", "download_pdf"],
        "Admin": ["manage_users", "institute_setup", "view_institute_analytics", "ai_chat", "view_profile", "download_pdf"]
    }

    @staticmethod
    def check_permission(role: str, permission: str) -> bool:
        """Verifies if a specific role has permission to execute a feature."""
        return permission in RBACManager.PERMISSIONS.get(role, [])

def init_session_state():
    """Initializes standard user authentication and session states."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "role" not in st.session_state:
        st.session_state.role = "Student"
    if "user_name" not in st.session_state:
        st.session_state.user_name = "Sateesh Ambesange"
