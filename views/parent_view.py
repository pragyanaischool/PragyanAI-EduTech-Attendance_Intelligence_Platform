import streamlit as st

def render_parent_dashboard():
    """
    Renders the dedicated Parent Portal view for monitoring ward attendance,
    receiving shortage advisories, and auditing weekly performance records.
    """
    parent_name = st.session_state.get("user_name", "Mr. Ambesange")
    ward_name = "Sateesh Ambesange"
    
    st.markdown(f"# 👨‍👩‍👦 Parent Portal — Ward Attendance Dashboard")
    st.markdown(f"### *Welcome, {parent_name} | Monitoring Ward: {ward_name} (ECE, Semester 5)*")

    # 1. Top Metric Grid Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h3>73.0%</h3><p>Ward Overall Attendance</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card" style="border-color:#EF4444;"><h3>2</h3><p>Subjects Near Shortage</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>Approved</h3><p>Leave Application Status</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h3>Warning</h3><p>Institutional Cutoff (75%)</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 2. Shortage Advisory Alert Box
    st.warning(
        f"⚠️ **Attendance Shortage Advisory:** Your ward **{ward_name}** has fallen below or is close to the 75% mandatory safety cutoff in "
        f"**Signals & Systems (68%)** and **Microprocessors (72%)**. Please consult department faculty or review leave records."
    )

    st.markdown("---")

    # 3. Subject-Wise Performance Table for the Ward
    st.markdown("### 📊 Detailed Subject-Wise Turnout Record")
    st.dataframe({
        "Subject Code": ["ECE501", "ECE502", "ECE503", "ECE504", "ECE505"],
        "Subject Name": ["Digital Electronics", "VLSI Design", "Signals & Systems", "Microprocessors", "Control Systems"],
        "Classes Attended / Total": ["22 / 24", "19 / 22", "17 / 25", "18 / 25", "15 / 18"],
        "Attendance %": ["91.6%", "86.3%", "68.0%", "72.0%", "83.3%"],
        "Risk Status": ["Safe", "Safe", "CRITICAL SHORTAGE", "WARNING", "Safe"]
    }, use_container_width=True)

    st.markdown("---")

    # 4. Action Center for Parents
    col_action1, col_action2 = st.columns(2)
    
    with col_action1:
        st.markdown("### 📞 Faculty & HOD Direct Connect")
        st.info("Need to discuss attendance anomalies or medical exemptions? You can submit a formal inquiry or request a callback directly through the **Leave & Approvals** or **AI Chatbot** tabs.")
        
    with col_action2:
        st.markdown("### 🔔 Notification Channel Preferences")
        st.checkbox("Receive Daily WhatsApp Attendance Summaries", value=True)
        st.checkbox("Receive Immediate Email Alerts on Absence", value=True)
        st.checkbox("Automated SMS Shortage Warnings", value=True)
