import streamlit as st
from utils.helpers import render_brand_logo

def render_parent_dashboard():
    """
    Renders the parent portal dashboard allowing guardians to track their ward's 
    attendance percentage, receive automated SMS/WhatsApp shortage alerts, and view medical leaves.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Mr. Ambesange")
    
    st.markdown(f"# 👨‍👩‍👧 Parent & Guardian Intelligence Portal — {user_name}")
    st.markdown("### *Real-Time Ward Tracking, Attendance Alerts, and Leave Approvals.*")

    # 2. Ward Overview Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>Sateesh Ambesange</h3><p>Ward Name & Roll #</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>84.7%</h3><p>Current Attendance</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>ECE (Sem 5)</h3><p>Department & Term</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>🟢 Safe Status</h3><p>Exam Eligibility</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 3. Ward Course Breakdown & Attendance Tracking
    st.markdown("### 📊 Ward's Course Attendance Ledger")
    st.dataframe({
        "Course Code & Name": ["ECE301 - Digital Design", "ECE302 - VLSI Architecture", "ECE303 - Signals & Systems", "ECE304 - Microprocessors"],
        "Classes Held": [24, 22, 25, 20],
        "Classes Attended": [22, 19, 19, 17],
        "Percentage": ["91.6%", "86.3%", "76.0% (Warning)", "85.0%"],
        "Status": ["🟢 Excellent", "🟢 Good", "🟡 Monitor Closely", "🟢 Good"]
    }, use_container_width=True)

    st.markdown("---")

    # 4. Guardian Communications & Alert Settings
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.markdown("### 📲 Automated Alert Subscriptions")
        st.checkbox("Receive Daily SMS Attendance Digest", value=True)
        st.checkbox("Receive Instant WhatsApp Shortage Warnings (<75%)", value=True)
        st.checkbox("Receive Monthly Faculty Counseling Notes", value=True)
        if st.button("💾 Save Alert Preferences"):
            st.success("Guardian alert notification preferences updated successfully!")

    with col_p2:
        st.markdown("### 📝 Ward Leave & Medical History")
        st.info(
            "**Recent Leave Record:**\n\n"
            "• **Duration:** Sep 2 to Sep 4, 2026\n"
            "• **Reason:** Viral Fever Recovery (Certificate Verified)\n"
            "• **Status:** Approved by Department HOD"
        )
