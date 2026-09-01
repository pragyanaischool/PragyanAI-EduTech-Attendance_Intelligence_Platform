import streamlit as st
from utils.helpers import render_brand_logo

def render_hod_analytics():
    """
    Renders a dedicated Department Analytics & Performance Intelligence dashboard for HODs,
    showcasing macro turnout distributions, faculty compliance rankings, and student shortage trends.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. HOD (ECE)")
    dept_name = "Electronics & Communication (ECE)"
    
    st.markdown(f"## 📊 Department Analytics & Intelligence — {dept_name}")
    st.markdown(
        f"Macro-level statistical breakdowns, faculty audit rankings, and student shortage cohorts "
        f"monitored by **{user_name}** (*HOD*)."
    )

    # 2. Top Metric Summary Cards for Department
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>87.4%</h3><p>Department Average</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>420</h3><p>Total Enrolled Students</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>18</h3><p>Active Faculty Members</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>37 At-Risk</h3><p>Shortage Cohort (<75%)</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 3. Course & Faculty Performance Breakdown Table
    st.markdown("### 📋 Department Course Turnout & Faculty Compliance Ledger")
    st.dataframe({
        "Course Code & Title": ["ECE301 - VLSI Design", "ECE302 - Digital Systems", "ECE303 - Signals & Theory", "ECE304 - Microprocessors", "ECE305 - Antenna Propagation"],
        "Assigned Faculty": ["Dr. Smitha Rao", "Prof. Anand Kumar", "Dr. Rajeshwari", "Prof. Suresh Hegde", "Dr. Preeti Deshmukh"],
        "Avg Attendance": ["91.2%", "88.5%", "84.1%", "89.6%", "83.5%"],
        "QR Compliance": ["100%", "96.6%", "96.4%", "100%", "93.3%"],
        "Health Status": ["🟢 Optimal", "🟢 Optimal", "🟡 Monitor", "🟢 Optimal", "🟡 Monitor"]
    }, use_container_width=True)

    st.markdown("---")

    # 4. Department Trend Insights & Actionable Directives
    col_ha1, col_ha2 = st.columns(2)
    
    with col_ha1:
        st.markdown("### 📈 Department Attendance Trend")
        st.info(
            "**Macro Trend:** Overall department attendance has risen by **+3.1%** this month. "
            "The ECE-303 (Signals & Theory) cohort requires closer monitoring due to recent dip below 85%."
        )

    with col_ha2:
        st.markdown("### ⚠️ Shortage & Disciplinary Directives")
        st.warning(
            "**Executive Action:** 37 students are currently flagged under the 75% shortage threshold. "
            "Automated warning notifications have been successfully sent to guardians. Faculty counseling sessions are scheduled for Friday."
        )
