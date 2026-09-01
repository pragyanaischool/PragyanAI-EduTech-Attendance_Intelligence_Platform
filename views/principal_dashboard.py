import streamlit as st
from utils.helpers import render_brand_logo

def render_principal_dashboard():
    """
    Renders the Principal Executive Dashboard with safe brand watermark logo,
    institute-wide metric summary cards, multi-department comparisons, and broadcast publishers.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal")
    
    st.markdown(f"# 🏛️ Principal's Executive Command Hub — {user_name}")
    st.markdown("### *Institute-Wide Attendance Intelligence, Multi-Department Compliance, and Global Broadcasts.*")

    # 2. Top Executive Metric Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>2,450</h3><p>Total Institute Students</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>112</h3><p>Total Faculty & Staff</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>88.6%</h3><p>Institute Average Turnout</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>142 At-Risk</h3><p>Institute Shortage Cohort</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 3. Multi-Department Attendance Comparison Table
    st.markdown("### 📊 Multi-Department Attendance & Compliance Ledger")
    st.dataframe({
        "Department Name": ["Electronics & Communication (ECE)", "Computer Science & Engineering (CSE)", "Mechanical Engineering (ME)", "Civil Engineering (CE)", "Artificial Intelligence & DS (AIDS)"],
        "HOD In-Charge": ["Dr. HOD (ECE)", "Dr. HOD (CSE)", "Dr. HOD (ME)", "Dr. HOD (CE)", "Dr. HOD (AIDS)"],
        "Students": [420, 650, 480, 400, 500],
        "Avg Attendance": ["87.4%", "91.2%", "84.5%", "83.9%", "92.0%"],
        "Compliance Status": ["🟢 Optimal", "🟢 Excellent", "🟡 Monitor", "🟡 Monitor", "🟢 Excellent"]
    }, use_container_width=True)

    st.markdown("---")

    # 4. Institute-Wide Notice Board Broadcaster
    st.markdown("### 📢 Executive Notice Board & Global Broadcast Center")
    with st.form("principal_global_broadcast_form"):
        notice_title = st.text_input("Broadcast Title", placeholder="e.g., Mandatory Mid-Semester Exam Guidelines or Holiday Circular")
        priority = st.selectbox("Broadcast Priority Level", ["🟢 Low (General Circular)", "🟡 Medium (Important Advisory)", "🔴 High (Mandatory Executive Directive)"])
        notice_content = st.text_area("Broadcast Content & Directives", placeholder="Type official announcement to be pushed across all student and faculty portals...")
        
        if st.form_submit_button("🚀 Broadcast Globally to All Portals"):
            if notice_title.strip() and notice_content.strip():
                if "institutional_notices" not in st.session_state:
                    st.session_state.institutional_notices = []
                new_notice = {
                    "id": len(st.session_state.get("institutional_notices", [])) + 1,
                    "title": notice_title,
                    "date": "2026-09-01",
                    "author": f"{user_name} (Principal & CAO)",
                    "priority": priority,
                    "content": notice_content
                }
                st.session_state.institutional_notices.insert(0, new_notice)
                st.success("🎉 Executive broadcast published successfully! Live across all student and faculty dashboards.")
            else:
                st.error("Please provide both a broadcast title and content.")
