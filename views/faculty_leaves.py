import streamlit as st
from utils.helpers import render_brand_logo

def render_faculty_leaves():
    """
    Renders the dedicated Faculty Leave & Student Exemption Review Portal,
    enabling faculty to submit personal leave requests and evaluate student medical certificates.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Faculty (ECE)")
    
    st.markdown(f"## 📝 Faculty Leave & Student Exemption Hub — {user_name}")
    st.markdown("Review student medical leave applications or submit your own faculty leave requests.")

    st.markdown("---")

    # 2. Split view: Review Student Leaves vs Submit Faculty Leave
    col_fl1, col_fl2 = st.columns(2)
    
    with col_fl1:
        st.markdown("### 👨‍🎓 Pending Student Leave Requests")
        st.info(
            "**Student:** Aarav Sharma (ECE2026_01)\n\n"
            "• **Duration:** Sep 3 to Sep 5, 2026\n"
            "• **Reason:** Medical Recovery (Certificate Attached)\n"
            "• **Status:** Pending Faculty Endorsement"
        )
        c_a, c_r = st.columns(2)
        if c_a.button("✅ Endorse Leave"):
            st.success("Student leave endorsed and forwarded to HOD!")
        if c_r.button("❌ Request Clarification"):
            st.warning("Clarification request sent to student.")

    with col_fl2:
        st.markdown("### 📤 Submit Faculty Leave Request")
        with st.form("faculty_leave_form"):
            leave_type = st.selectbox("Leave Type", ["Academic Conference / Workshop", "Medical Leave", "Casual Leave"])
            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date")
            reason = st.text_area("Reason & Alternate Lecture Arrangement", placeholder="Describe adjustment details...")
            
            if st.form_submit_button("🚀 Submit to HOD"):
                if reason.strip():
                    st.success("Faculty leave request successfully submitted to Department HOD!")
                else:
                    st.error("Please provide leave reasons and lecture adjustments.")
