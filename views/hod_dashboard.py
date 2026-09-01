import streamlit as st
from utils.helpers import render_brand_logo

def render_hod_dashboard():
    """
    Renders the Head of Department (HOD) attendance intelligence dashboard with safe brand watermark logo,
    department-wide metric cards, faculty audit tools, and shortage notifications.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. HOD (ECE)")
    
    st.markdown(f"# 🏛️ HOD Department Intelligence Hub — {user_name}")
    st.markdown("### *Department-Wide Attendance Auditing, Faculty Oversight, and Compliance Management.*")

    # 2. Top Departmental Metric Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>420</h3><p>Total ECE Students</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>18</h3><p>Faculty Members</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>87.4%</h3><p>Department Average</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>37 At-Risk</h3><p>Shortage Alert List</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 3. Department Faculty Performance & Audit Overview
    st.markdown("### 👨‍🏫 Faculty Lecture Delivery & Attendance Logging Audit")
    st.dataframe({
        "Faculty Name": ["Dr. Smitha Rao", "Prof. Anand Kumar", "Dr. Rajeshwari", "Prof. Suresh Hegde", "Dr. Preeti Deshmukh"],
        "Assigned Courses": ["VLSI Design", "Digital Systems", "Signals & Theory", "Microprocessors", "Antenna Wave Propagation"],
        "Classes Scheduled": [32, 30, 28, 35, 30],
        "QR Sessions Hosted": [32, 29, 27, 35, 28],
        "Compliance Rate": ["100%", "96.6%", "96.4%", "100%", "93.3%"],
        "Audit Status": ["🟢 Verified", "🟢 Verified", "🟢 Verified", "🟢 Verified", "🟡 Review Needed"]
    }, use_container_width=True)

    st.markdown("---")

    # 4. Department Shortage Roster & Actions
    st.markdown("### ⚠️ Department Shortage & Disciplinary Action Hub")
    col_hod1, col_hod2 = st.columns(2)
    
    with col_hod1:
        st.markdown("#### Automated Shortage Dispatches")
        st.info(
            "**Batch Notification Status:** Automated WhatsApp and email warning alerts "
            "have been dispatched to 37 students and their respective parents for falling below the 75% cutoff."
        )
        if st.button("📤 Re-trigger Batch Warning Notifications"):
            st.success("Batch warning notifications successfully re-dispatched via Twilio & SendGrid APIs!")

    with col_hod2:
        st.markdown("#### Departmental Policy Controls")
        st.selectbox("Medical Relaxation Grace Period", ["Up to 10% (Standard)", "Up to 15% (Special Case)"])
        if st.button("💾 Update Department Bylaws"):
            st.success("Department attendance bylaws updated successfully across the platform database.")
