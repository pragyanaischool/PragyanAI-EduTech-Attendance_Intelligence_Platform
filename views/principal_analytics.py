import streamlit as st
from utils.helpers import render_brand_logo

def render_principal_analytics():
    """
    Renders a dedicated Executive Analytics & Intelligence dashboard for the Principal,
    showcasing institute-wide turnout trends, cross-department rankings, and macro risk cohorts.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal")
    
    st.markdown(f"## 📊 Executive Analytics & Institutional Intelligence — {user_name}")
    st.markdown("Macro-level statistical breakdowns, cross-department benchmarks, and institute-wide student success cohorts.")

    # 2. Top Metric Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>88.6%</h3><p>Institute Average</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>2,450</h3><p>Enrolled Students</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>112</h3><p>Faculty Members</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>142 At-Risk</h3><p>Shortage Cohort (<75%)</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 3. Cross-Department Benchmark Table
    st.markdown("### 📋 Cross-Department Turnout & Compliance Benchmarks")
    st.dataframe({
        "Department": ["Computer Science (CSE)", "AI & Data Science (AIDS)", "Electronics (ECE)", "Mechanical (ME)", "Civil (CE)"],
        "Students": [650, 500, 420, 480, 400],
        "Avg Turnout": ["91.2%", "92.0%", "87.4%", "84.5%", "83.9%"],
        "QR Adherence": ["98.5%", "99.0%", "96.5%", "94.2%", "93.0%"],
        "Performance Tier": ["🟢 Tier 1 (Optimal)", "🟢 Tier 1 (Optimal)", "🟢 Tier 2 (Good)", "🟡 Tier 3 (Monitor)", "🟡 Tier 3 (Monitor)"]
    }, use_container_width=True)

    st.markdown("---")

    # 4. Executive Trend Insights & Institutional Directives
    col_pa1, col_pa2 = st.columns(2)
    
    with col_pa1:
        st.markdown("### 📈 Macro Attendance Trend")
        st.info(
            "**Institutional Trend:** Institute-wide attendance has increased by **+2.8%** quarter-over-quarter. "
            "Engineering departments are showing strong adoption of the dynamic QR code anti-proxy system."
        )

    with col_pa2:
        st.markdown("### ⚠️ Strategic Directives & Risk Mitigations")
        st.warning(
            "**Executive Action:** 142 students across Mechanical and Civil engineering departments are flagged under the 75% shortage line. "
            "Automated guardian warnings have been triggered, and HOD counseling reviews are underway."
        )
