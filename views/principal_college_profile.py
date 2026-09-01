import streamlit as st
import pandas as pd
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_principal_college_profile():
    """
    Renders the Principal College Profile & Institutional Governance Hub.
    Extracts live data from PragyanDatabase, featuring institutional accreditation, executive deanery rosters,
    statutory bylaws, and an interactive 'Select Department & Get Faculty List' module showcasing 
    degrees, designations, college experience years, and total professional experience.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal Dean")
    college_name = "PragyanAI Institute of Technology & Venture Studio"
    PragyanDatabase.initialize_database()
    
    st.markdown(f"## 🏛️ Institutional College Profile & Governance Hub — {user_name}")
    st.markdown(
        f"Manage institutional credentials, executive campus portfolios, department affiliations, "
        f"and database-driven faculty rosters for **{college_name}**."
    )
    
    st.info(
        "💡 **Principal Authority Portal:** Information configured here extracts live records from PragyanDatabase, "
        "governing departmental oversight, faculty experience audits, and institutional compliance parameters."
    )

    st.markdown("---")

    # 2. Pull Live Data from Database
    faculty_db = PragyanDatabase.get_department_faculty()
    fac_df = pd.DataFrame(faculty_db)

    # 3. Multi-Tab College Governance Navigation
    tab_overview, tab_deans, tab_dept_faculty, tab_policy = st.tabs([
        "🏫 Institution Overview & Accreditation",
        "👨‍💼 Executive Deanery Roster",
        "🏢 Department & Faculty Directory (DB)",
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
            st.metric("Active Faculty & Researchers", f"{len(fac_df)} Registered Profiles", delta="100% Ph.D. / Industry Led")
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

    # --- TAB 3: SELECT DEPT & GET FACULTY LIST (DB Extracted) ---
    with tab_dept_faculty:
        st.markdown("### 🏢 Department-Wise Faculty Roster & Experience Audit")
        st.markdown("Select a department below to query database-backed faculty members, degrees, designations, joining dates, and experience metrics.")

        if not fac_df.empty and "department" in fac_df.columns:
            all_departments = fac_df["department"].unique().tolist()
            selected_dept = st.selectbox("🎯 Select Department to Filter Faculty Roster", all_departments, key="college_profile_dept_sel")

            # Filter faculty by selected department
            filtered_fac_df = fac_df[fac_df["department"] == selected_dept]

            st.markdown(f"#### 📋 Faculty Roster for: `{selected_dept}`")
            st.info(f"Displaying **{len(filtered_fac_df)}** faculty member(s) registered under this department in PragyanDatabase.")

            # Format dataframe for clean presentation
            display_df = filtered_fac_df[[
                "faculty_name", "degree", "designation", "joined_date", 
                "college_experience_years", "total_experience_years", "active_courses", "status"
            ]].rename(columns={
                "faculty_name": "Faculty Name",
                "degree": "Highest Degree",
                "designation": "Designation",
                "joined_date": "Joining Date",
                "college_experience_years": "Yrs in College",
                "total_experience_years": "Total Exp (Yrs)",
                "active_courses": "Active Courses",
                "status": "Status"
            })

            st.dataframe(display_df, use_container_width=True)

            # Summary Metrics for Selected Department
            avg_college_exp = round(filtered_fac_df["college_experience_years"].mean(), 1)
            avg_total_exp = round(filtered_fac_df["total_experience_years"].mean(), 1)

            mc1, mc2, mc3 = st.columns(3)
            with mc1:
                st.metric(label="Total Department Faculty", value=f"{len(filtered_fac_df)} Members")
            with mc2:
                st.metric(label="Avg Tenure in College", value=f"{avg_college_exp} Years")
            with mc3:
                st.metric(label="Avg Total Experience", value=f"{avg_total_exp} Years")
        else:
            st.warning("No departmental faculty records found in PragyanDatabase.")

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
