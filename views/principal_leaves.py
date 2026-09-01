import streamlit as st
import pandas as pd
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_principal_leaves():
    """
    Renders the dedicated Principal's Institutional Leave & Sabbatical Governance Hub.
    Allows the principal to review escalated departmental leaves, sabbaticals, approve/reject pending applications stored in DB,
    and audit month-wise department-wide faculty availability and leave lists.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal")
    college_name = "PragyanAI Institute of Technology & Venture Studio"
    PragyanDatabase.initialize_database()
    
    st.markdown(f"## 📝 Institutional Leave Governance & Sabbatical Hub — {user_name}")
    st.markdown(
        f"Review escalated departmental leave requests, faculty sabbaticals, and institute-wide attendance policy bylaws "
        f"across **{college_name}**."
    )
    
    st.info(
        "💡 **Executive Governance:** Approvals granted at this level apply institution-wide "
        "and synchronize with state university compliance records and database ledgers."
    )

    st.markdown("---")

    # 2. Fetch Leave & Faculty Records from Database
    leaves_db = PragyanDatabase.get_faculty_leaves()
    faculty_db = PragyanDatabase.get_department_faculty()

    # 3. Multi-Tab Navigation for Principal Leaves & Availability
    tab_approvals, tab_availability = st.tabs([
        "📥 Leave Approvals & Pending Requests (DB)",
        "📅 Month-Wise Faculty Availability & Leave Audit"
    ])

    # --- TAB 1: LEAVE APPROVALS & PENDING (DB CONNECTED) ---
    with tab_approvals:
        st.markdown("### 🏛️ Escalated Department Head & Faculty Leave/Sabbatical Applications")
        st.markdown("Live leave requests submitted by faculty and HODs, synchronized persistently with PragyanDatabase.")

        pending_leaves = [l for l in leaves_db if l["status"] == "Pending"]
        history_leaves = [l for l in leaves_db if l["status"] != "Pending"]

        st.markdown(f"#### ⏳ Pending Leave & Sabbatical Requests ({len(pending_leaves)})")

        if pending_leaves:
            for leave in pending_leaves:
                with st.container():
                    st.markdown(
                        f"""
                        <div style="padding: 15px; border-radius: 8px; background-color: #1e293b; border-left: 5px solid #3b82f6; margin-bottom: 15px;">
                            <h4 style="margin: 0; color: #f8fafc;">{leave.get('faculty_name')} — {leave.get('department')}</h4>
                            <p style="margin: 5px 0; font-size: 0.85rem; color: #94a3b8;">
                                <b>Duration:</b> {leave.get('start_date')} to {leave.get('end_date')} &nbsp;|&nbsp; <b>Reason:</b> {leave.get('reason')}
                            </p>
                            <p style="margin: 0; color: #e2e8f0; font-size: 0.95rem;"><b>Status:</b> 🟡 Pending Executive Sanction</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    
                    col_p1, col_p2 = st.columns(2)
                    with col_p1:
                        if st.button("✅ Sanction Executive Leave / Sabbatical", key=f"approve_princ_leave_{leave['id']}"):
                            PragyanDatabase.update_faculty_leave_status(leave['id'], "Approved")
                            st.success(f"Leave for **{leave['faculty_name']}** sanctioned successfully and interim charge notification dispatched!")
                            st.rerun()
                    with col_p2:
                        if st.button("❌ Request Administrative Review", key=f"reject_princ_leave_{leave['id']}"):
                            PragyanDatabase.update_faculty_leave_status(leave['id'], "Rejected")
                            st.warning(f"Administrative review request dispatched to **{leave['faculty_name']}**.")
                            st.rerun()
                    st.markdown("---")
        else:
            st.info("🎉 No pending leave or sabbatical requests requiring executive review at this time.")

        st.markdown("#### 📜 Approved & Sanctioned Leave History")
        if history_leaves:
            history_df = pd.DataFrame(history_leaves)
            st.dataframe(history_df[["faculty_name", "department", "start_date", "end_date", "reason", "status"]], use_container_width=True)
        else:
            st.info("No historical leave records found.")

    # --- TAB 2: MONTH-WISE FACULTY AVAILABILITY & LEAVE AUDIT ---
    with tab_availability:
        st.markdown("### 📅 Month-Wise Faculty Availability & Leave Audit")
        st.markdown("Select a year, month, and department to generate separate detailed lists of available faculties and those on approved leave.")

        # Filter controls
        mc1, mc2, mc3 = st.columns(3)
        with mc1:
            sel_year = st.selectbox("Select Year", [2026, 2027], key="prin_leave_yr")
        with mc2:
            months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            sel_month = st.selectbox("Select Month", months_list, index=8, key="prin_leave_mo") # Default September
        with mc3:
            all_depts = list(set([f.get("department", "Electronics & Communication (ECE)") for f in faculty_db]))
            sel_dept = st.selectbox("Select Department", all_depts, key="prin_leave_dept")

        st.markdown("---")

        month_num_map = {m: i for i, m in enumerate(months_list, 1)}
        target_month_num = month_num_map[sel_month]

        dept_faculty = [f for f in faculty_db if f.get("department") == sel_dept]

        faculties_on_leave = []
        faculties_available = []

        for fac in dept_faculty:
            fac_name = fac.get("faculty_name")
            is_on_leave = False
            matched_leave_info = ""

            for l in leaves_db:
                if l.get("faculty_name") == fac_name and l.get("status") == "Approved":
                    try:
                        s_date = datetime.datetime.strptime(l.get("start_date"), "%Y-%m-%d")
                        e_date = datetime.datetime.strptime(l.get("end_date"), "%Y-%m-%d")
                        
                        if (s_date.year == sel_year and s_date.month == target_month_num) or \
                           (e_date.year == sel_year and e_date.month == target_month_num) or \
                           (s_date <= datetime.datetime(sel_year, target_month_num, 1) and e_date >= datetime.datetime(sel_year, target_month_num, 28)):
                            is_on_leave = True
                            matched_leave_info = f"From {l.get('start_date')} to {l.get('end_date')} ({l.get('reason')})"
                    except ValueError:
                        pass

            if is_on_leave:
                faculties_on_leave.append({
                    "Faculty Name": fac_name,
                    "Designation": fac.get("designation", "Assistant Professor"),
                    "Degree": fac.get("degree", "Ph.D."),
                    "Leave Period & Reason": matched_leave_info
                })
            else:
                faculties_available.append({
                    "Faculty Name": fac_name,
                    "Designation": fac.get("designation", "Assistant Professor"),
                    "Degree": fac.get("degree", "Ph.D."),
                    "Active Courses": fac.get("active_courses", "N/A"),
                    "Total Exp (Yrs)": f"{fac.get('total_experience_years', 5)} Years"
                })

        st.markdown(f"### 📋 Department Audit Report for `{sel_dept}` — `{sel_month} {sel_year}`")

        mk1, mk2 = st.columns(2)
        with mk1:
            st.metric(label="🟢 Available Faculties", value=f"{len(faculties_available)} Members")
        with mk2:
            st.metric(label="🔴 Faculties on Approved Leave", value=f"{len(faculties_on_leave)} Members", delta_color="inverse")

        st.markdown("---")

        st.markdown("#### 🟢 List 1: Available Faculties")
        if faculties_available:
            st.dataframe(pd.DataFrame(faculties_available), use_container_width=True)
        else:
            st.info("No faculty members available for the selected period.")

        st.markdown("---")

        st.markdown("#### 🔴 List 2: Faculties on Approved Leave")
        if faculties_on_leave:
            st.dataframe(pd.DataFrame(faculties_on_leave), use_container_width=True)
        else:
            st.success("🟢 Zero faculty members on approved leave during this month. 100% departmental staffing available!")
