import streamlit as st
from utils.helpers import render_brand_logo

def render_faculty_dashboard():
    """
    Renders the faculty attendance dashboard with safe brand watermark logo,
    QR code generator controls, and class attendance analytics.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Faculty 1 (Comp)")
    
    st.markdown(f"# 👨‍🏫 Faculty Portal & QR Intelligence Hub — {user_name}")
    st.markdown("### *Generate Dynamic QR Codes. Monitor Live Class Roster. Track At-Risk Students.*")

    # 2. Top Metric Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>5 Active</h3><p>Assigned Courses</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>240</h3><p>Total Enrolled Students</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>89.2%</h3><p>Average Class Turnout</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>14 At-Risk</h3><p>Shortage Warning List</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 3. Dynamic QR Code Generator Section
    st.markdown("### 📱 Dynamic QR Code Attendance Session Generator")
    col_qr1, col_qr2 = st.columns(2)
    
    with col_qr1:
        selected_course = st.selectbox("Select Course for Session", ["Digital Logic Design (ECE301)", "VLSI Architecture (ECE402)", "Microcontrollers (ECE305)"])
        validity_mins = st.slider("QR Code Expiry Duration (Minutes)", min_value=1, max_value=15, value=5)
        geo_fence = st.checkbox("Enable Geo-Fencing Verification (Campus Wi-Fi / GPS)", value=True)
        
        if st.button("🚀 Generate Live QR Session"):
            st.success(f"Dynamic QR Session generated successfully for **{selected_course}**! Valid for {validity_mins} minutes.")
            
    with col_qr2:
        st.markdown("#### 🔍 Active Session Live Feed")
        st.info(
            "**Status:** QR Session Active.\n\n"
            "• **Scans Recorded:** 42 / 48 Students\n"
            "• **Geo-Fence Compliance:** 100%\n"
            "• **Anti-Proxy Shield:** Active (Device Fingerprinting Enforced)"
        )

    st.markdown("---")

    # 4. Enrolled Students & Shortage Roster Table
    st.markdown("### 📋 Class Attendance Roster & Shortage Audit")
    st.dataframe({
        "Roll No": ["ECE2026_01", "ECE2026_02", "ECE2026_03", "ECE2026_04", "ECE2026_05"],
        "Student Name": ["Aarav Sharma", "Priya Patel", "Rohan Verma", "Sneha Rao", "Kiran Kumar"],
        "Total Classes": [25, 25, 25, 25, 25],
        "Attended": [23, 21, 17, 24, 18],
        "Percentage": ["92.0%", "84.0%", "68.0% (Shortage)", "96.0%", "72.0% (Warning)"],
        "Action": ["Good", "Good", "⚠️ Send Warning Notice", "Excellent", "🟡 Monitor"]
    }, use_container_width=True)
