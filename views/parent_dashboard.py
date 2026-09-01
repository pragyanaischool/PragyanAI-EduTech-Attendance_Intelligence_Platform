import streamlit as st
from utils.helpers import render_brand_logo

def render_parent_dashboard():
    """
    Renders the dedicated Parent & Guardian Dashboard allowing guardians to monitor 
    their ward's live attendance percentage, exam eligibility, course ledgers, and recent leave approvals.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Mr. Ambesange")
    ward_name = "Sateesh Ambesange"
    
    st.markdown(f"# 👨‍👩‍👧 Parent & Guardian Dashboard — {user_name}")
    st.markdown(f"### *Real-Time Attendance Monitoring & Ward Progress Tracker for {ward_name}.*")

    # 2. Ward Overview Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(f'<div class="metric-card"><h3>{ward_name}</h3><p>Linked Ward & Roll #</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>84.7%</h3><p>Current Attendance</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>ECE (Sem 5)</h3><p>Department & Term</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>🟢 Safe Status</h3><p>Exam Eligibility (>75%)</p></div>', unsafe_allow_html=True)

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

    # 4. Guardian Quick Actions & Recent Leave Status
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.markdown("### 📝 Recent Ward Leave & Medical Status")
        st.info(
            "**Leave Record #LN-2026-04:**\n\n"
            "• **Duration:** Sep 2 to Sep 4, 2026\n"
            "• **Reason:** Viral Fever Recovery (Medical Certificate Attached)\n"
            "• **Approval Status:** ✅ Approved by Department HOD"
        )
        if st.button("📤 Submit New Leave Application for Ward"):
            st.success("Leave application form unlocked. You can now submit medical certificates.")

    with col_p2:
        st.markdown("### 📢 Important Institutional Notices")
        st.success(
            "**Mid-Semester Examination Mandate:**\n\n"
            "All students must maintain a strict 75% attendance record to qualify for "
            "upcoming examinations starting later this month. Guardian notifications are active."
        )
