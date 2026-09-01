import streamlit as st
from utils.helpers import render_brand_logo

def render_parent_profile():
    """
    Renders the dedicated Parent & Guardian Profile management view,
    allowing guardians to update contact details, linked ward identifiers, 
    and SMS/WhatsApp attendance alert subscriptions.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Mr. Ambesange")
    
    st.markdown(f"## 👨‍👩‍👧 Parent & Guardian Profile Hub — {user_name}")
    st.markdown(
        f"Manage your guardian profile, linked ward details, emergency contact numbers, "
        f"and automated attendance alert subscriptions."
    )
    
    st.info(
        "💡 **Guardian Security:** Updates made here synchronize with faculty counseling records "
        "and ensure real-time delivery of attendance notifications and shortage warnings."
    )

    st.markdown("---")

    # 2. Parent Profile Edit Form
    with st.form("parent_profile_management_form"):
        st.markdown("### 📋 Guardian & Linked Ward Credentials")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.text_input("Guardian Full Name", value=user_name)
            st.text_input("Registered Email Address", value="parent.ambesange@gmail.com")
            st.text_input("Primary Contact Phone (SMS / WhatsApp)", value="+91 98765 43210")
            
        with c2:
            st.text_input("Linked Ward Name", value="Sateesh Ambesange")
            st.text_input("Ward Roll Number / ID", value="ECE_2026_042")
            st.text_input("Ward Department & Term", value="Electronics & Communication (ECE) — Sem 5")
            
        st.text_area(
            "Guardian Statement & Notes", 
            value="Committed to monitoring ward attendance regularly, reviewing medical leaves promptly, and coordinating with faculty advisors for academic excellence."
        )

        st.markdown("---")
        st.markdown("### 📲 Automated Alert & Notification Subscriptions")
        
        nc1, nc2 = st.columns(2)
        with nc1:
            st.checkbox("Receive Daily SMS Attendance Summary Digest", value=True)
            st.checkbox("Receive Instant WhatsApp Shortage Warnings (<75%)", value=True)
        with nc2:
            st.checkbox("Receive Monthly Faculty Counseling Notes", value=True)
            st.checkbox("Email Notifications for Approved Medical Leaves", value=True)

        st.markdown("---")
        
        if st.form_submit_button("💾 Save Guardian Profile Updates"):
            st.success(f"Guardian profile records and ward links for **{user_name}** updated successfully!")
