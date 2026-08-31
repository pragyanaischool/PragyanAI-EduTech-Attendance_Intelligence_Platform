import streamlit as st

def render_profile_view():
    """
    Renders the personal profile management settings view with brand watermark logo
    and editable user fields.
    """
    # 1. Brand Watermark Logo Integration
    st.image("PragyanAI_Transparent.png", width=220)
    
    user_name = st.session_state.get("user_name", "User")
    user_role = st.session_state.get("role", "Student")
    
    st.markdown(f"## 👤 Personal Profile Management — [{user_role}]")
    st.markdown(f"Manage your account settings, contact information, and institutional profile preferences.")

    with st.form("profile_settings_form"):
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Full Name", value=user_name)
            st.text_input("Institutional Email", value="user@pragyan.edu")
        with c2:
            st.text_input("Phone Number", value="+91 98765 43210")
            st.text_input("Department / Role Group", value="Electronics & Communication (ECE)")
            
        st.text_area("Academic Bio", value="Committed to maintaining academic excellence, regular attendance, and active institutional engagement.")
        
        if st.form_submit_button("💾 Save Profile Settings"):
            st.success("Profile records and settings updated successfully!")
