import streamlit as st
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_principal_college_profile():
    """
    Renders the Principal College Profile & Institutional Governance Hub.
    Displays college accreditation, executive leadership rosters, department metrics, 
    and campus-wide statutory policy frameworks for PragyanAI Institute of Technology.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal Dean")
    college_name = "PragyanAI Institute of Technology & Venture Studio"
    
    st.markdown(f"## 🏛️ Institutional College Profile & Governance Hub — {user_name}")
    st.markdown(
        f"Manage institutional credentials, executive campus portfolios, department affiliations, "
        f"and statutory governance frameworks for **{college_name}**."
    )
    
    st.info(
        "💡 **Principal Authority Portal:** Information configured here governs campus-wide attendance thresholds, "
        "deanery audit reporting, and institutional accreditation parameters."
    )

    st.markdown("---")

    # 2. Multi-Tab College Governance Navigation
    tab_overview, tab_deans, tab_departments, tab_policy = st.tabs([
        "🏫 Institution Overview & Accreditation",
        "👨‍💼 Executive Deanery Roster",
        "🏢 Campus Departments & Metrics",
        "📜 Statutory Policies & Bylaws"
    ])

    # --- TAB 1: INSTITUTION OVERVIEW ---
    with tab_overview:
        st.markdown("### 🏛️ Institution Profile & Accreditation Status")
        
        col_cp1, col_cp2 = st.columns(2)
        with col_cp1:
            st.markdown(
                f"""
                <div style="padding: 20px; background-color: #1e293b; border-radius: 10px; border-left: 5px solid #3b82f6;">
                    <h3 style="margin-top: 0; color: #f8fafc;">{college_name}</h3>
                    <p style="margin: 5px 0; color: #94a3b8;"><b>Campus Location:</b> Bengaluru, Karnataka, India</p>
                    <p style="margin: 5px 0; color: #94a3b8;"><b>Establishment Year:</b> 2019</p>
                    <p style="margin: 5px 0; color: #94a3b8;"><b>Accreditation:</b> NAAC A++ Grade & AICTE Deep-Tech Autonomous Status</p>
                    <p style="margin: 0; color: #34d399;"><b>Operational Status:</b> 🟢 Fully Active & Autonomous</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_cp2:
            st.markdown("#### 📊 Campus-Wide Vital Statistics")
            st.metric("Total Enrolled Students across Batches", "1,450+ Students", delta="+120 vs previous year")
            st.metric("Active Faculty & Researchers", "85 Members", delta="100% Ph.D. / Industry Led")
            st.metric("Undergraduate & Postgraduate Programs", "12 Specialized Degrees", delta="AI & Systems Focus")

    # --- TAB 2: EXECUTIVE DEANERY ---
    with tab_deans:
        st.markdown("### 👨‍💼 Executive Deanery & Leadership Roster")
        st.markdown("Core administrative leadership overseeing academic execution, research ventures, and student welfare.")

        deanery_data = [
            {"Position": "Principal & Chief Academic Officer", "Name": "Dr. Principal Dean", "Office": "Administrative Block A", "Email": "principal@pragyanai.edu"},
            {"Position": "Dean of Research & Deep-Tech Ventures", "Name": "Dr. Sateesh Ambesange", "Office": "Innovation Studio Wing B", "Email": "research.dean@pragyanai.edu"},
            {"Position": "Registrar & Academic Operations", "Name": "Prof. R. V. Swaminathan", "Office": "Central Registry", "Email": "registrar@pragyanai.edu"},
            {"Position": "Controller of Examinations", "Name": "Dr. Meenakshi Sundaram", "Office": "Exam Bhavan", "Email": "coe@pragyanai.edu"}
        ]
        st.dataframe(deanery_data, use_container_width=True)

    # --- TAB 3: DEPARTMENTS ---
    with tab_departments:
        st.markdown("### 🏢 Campus Departmental Distribution")
        st.markdown("Active engineering and science departments operating under the PragyanAI institutional umbrella.")

        dept_data = [
            {"Department Name": "Electronics & Communication (ECE)", "HOD": "Dr. HOD (ECE)", "Active Students": 350, "Faculty Count": 18, "Status": "🟢 Optimal"},
            {"Department Name": "Artificial Intelligence & Data Science", "HOD": "Dr. Kavitha Murthy", "Active Students": 420, "Faculty Count": 22, "Status": "🟢 Optimal"},
            {"Department Name": "Computer Science & Engineering", "HOD": "Dr. Rajesh Hegde", "Active Students": 480, "Faculty Count": 25, "Status": "🟢 Optimal"},
            {"Department Name": "Electrical & Electronics Engineering", "HOD": "Prof. Anand Rao", "Active Students": 200, "Faculty Count": 20, "Status": "🟢 Optimal"}
        ]
        st.dataframe(dept_data, use_container_width=True)

    # --- TAB 4: STATUTORY POLICIES ---
    with tab_policy:
        st.markdown("### 📜 Statutory Institutional Policies & Bylaws")
        st.markdown("Mandatory campus guidelines enforced across all departments.")

        st.markdown(
            """
            - **Strict 75% Attendance Mandate:** Automated shortage flagging triggers below 75% aggregate turnout. Medical exemptions require certified documentation and HOD endorsement.
            - **Acting HOD Delegation Protocol:** During personal leave or sabbaticals, HODs must nominate an in-charge faculty member to maintain academic continuity.
            - **Curriculum Pacing Compliance:** All subjects must maintain scheduled vs. delivered class deficits of fewer than 10 sessions before midterm audits.
            - **Deep-Tech Venture Integration:** Research scholars and undergraduate capstones are governed by the PragyanAI IP and Venture Studio incubation framework.
            """
        )
