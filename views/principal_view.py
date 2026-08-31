import streamlit as st
from utils.helpers import render_brand_logo

def render_principal_dashboard():
    """
    Renders the Principal's Institute-Wide Executive Dashboard with safe brand watermark logo,
    macro-level institutional metrics, cross-department comparison tables, and compliance controls.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal")
    
    st.markdown(f"# 🏛️ Principal's Executive Intelligence Hub — {user_name}")
    st.markdown("### *Macro-Level Institutional Attendance Analytics, Department Comparisons, and Audit Controls.*")

    # 2. Top Institutional Macro Metric Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>5,840</h3><p>Total Enrolled Students</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>185</h3><p>Total Faculty Staff</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>88.6%</h3><p>Institute Average Turnout</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>214 At-Risk</h3><p>Total Shortage Roster</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 3. Department-wise Macro Comparison Table
    st.markdown("### 📊 Department-Wise Institutional Compliance Overview")
    st.dataframe({
        "Department Name": ["Electronics & Comm. (ECE)", "Computer Science (CSE)", "Mechanical Engineering (ME)", "Civil Engineering (CE)", "Electrical & Electronics (EEE)", "Information Science (ISE)"],
        "Students": [920, 1450, 890, 780, 910, 890],
        "Avg Attendance": ["89.4%", "91.2%", "85.1%", "83.6%", "87.9%", "89.0%"],
        "Shortage Count": [37, 42, 48, 41, 28, 18],
        "Compliance Health": ["🟢 Excellent", "🟢 Excellent", "🟡 Moderate", "🟡 Moderate", "🟢 Good", "🟢 Good"]
    }, use_container_width=True)

    st.markdown("---")

    # 4. Executive Institutional Controls & Policy Audits
    st.markdown("### ⚙️ Executive Policy & Broadcast Center")
    col_pr1, col_pr2 = st.columns(2)
    
    with col_pr1:
        st.markdown("#### Institute-Wide Broadcast Notice")
        notice_text = st.text_area("Draft institutional announcement for all departments:", placeholder="Type urgent examination cutoff notice or attendance compliance reminder...")
        if st.button("📢 Broadcast to All Portals"):
            if notice_text.strip():
                st.success("Official institutional notice successfully broadcast across all student, faculty, and parent dashboards!")
            else:
                st.error("Please enter a valid notice message.")

    with col_pr2:
        st.markdown("#### Executive Audit Controls")
        st.info(
            "**Audit Certification Status:**\n\n"
            "• **Term Exam Eligibility Lock:** Active (75% Threshold)\n"
            "• **Twilio SMS Gateway:** Operational\n"
            "• **SendGrid Email Dispatcher:** Operational\n"
            "• **ReportLab PDF Engine:** Ready for Export"
        )
