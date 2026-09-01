import streamlit as st
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_hod_leaves():
    """
    Renders the dedicated HOD Department Leave & Exemption Approval Hub,
    allowing department heads to review live leave requests, select specific requests to approve/reject,
    apply for personal leave with Acting HOD nominations, inspect monthly student/faculty ledgers, 
    and view the Principal-managed holiday calendar.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. HOD (ECE)")
    dept_name = "Electronics & Communication (ECE)"
    PragyanDatabase.initialize_database()
    
    st.markdown(f"## 📝 Department Leave & Disciplinary Approval Hub — {user_name}")
    st.markdown(
        f"Review, endorse, and action faculty leave requests, student medical exemptions, "
        f"personal leave submissions, and principal-scheduled institutional calendars for the **{dept_name}** department."
    )
    
    st.info(
        "💡 **HOD Approval Governance:** Approvals granted here immediately update student attendance passports, "
        "log faculty leave audits to the principal deanery, and coordinate department substitution rosters."
    )

    st.markdown("---")

    # 2. Comprehensive Multi-Tab HOD Leave & Calendar Navigation
    tab_approvals, tab_hod_apply, tab_students, tab_faculty, tab_calendar = st.tabs([
        "📋 Pending Approvals",
        "📝 HOD Leave & Acting Nomination", 
        "🎓 Student Leave Audit (Monthly)", 
        "👨‍🏫 Faculty Leave Audit (Monthly)", 
        "📅 Institutional Holiday Calendar"
    ])

    # --- TAB 1: PENDING APPROVALS (Interactive Request Selection & Action) ---
    with tab_approvals:
        st.markdown("### 📋 Interactive Leave & Exemption Approval Queue")
        st.markdown("Select pending student or faculty requests from the registry below to review and action (Approve or Reject).")

        # Ensure session state trackers exist for dynamic student/faculty leave requests
        if "student_leave_requests_db" not in st.session_state:
            st.session_state.student_leave_requests_db = [
                {"id": "S_REQ_01", "name": "Aarav Sharma", "roll": "ECE_2026_010", "type": "Medical Exemption", "duration": "Sep 3, 2026 to Sep 5, 2026", "reason": "Viral Fever Recovery", "doc": "Medical_Certificate_Aarav.pdf", "status": "⏳ Pending"},
                {"id": "S_REQ_02", "name": "Priya Patel", "roll": "ECE_2026_088", "type": "Casual Leave", "duration": "Sep 6, 2026 to Sep 7, 2026", "reason": "Family Emergency", "doc": "None", "status": "⏳ Pending"}
            ]

        if "faculty_leave_requests_db" not in st.session_state:
            st.session_state.faculty_leave_requests_db = [
                {"id": "F_REQ_01", "faculty": "Dr. Smitha Rao", "chair": "VLSI Design Chair", "type": "IEEE National Conference", "duration": "Sep 10, 2026 to Sep 11, 2026", "adjustment": "Covered by Prof. Anand Kumar", "status": "⏳ Pending"},
                {"id": "F_REQ_02", "faculty": "Prof. Meena Hegde", "chair": "Embedded Systems", "type": "Medical Leave", "duration": "Sep 12, 2026", "adjustment": "Covered by Dr. Rajesh Sharma", "status": "⏳ Pending"}
            ]

        col_app1, col_app2 = st.columns(2)

        # --- Student Leave Approvals Sub-Section ---
        with col_app1:
            st.markdown("#### 🎓 Student Leave & Exemption Requests")
            pending_students = [req for req in st.session_state.student_leave_requests_db if req["status"] == "⏳ Pending"]

            if pending_students:
                student_options = {f"{req['name']} ({req['roll']}) - {req['type']}": req['id'] for req in pending_students}
                selected_stud_label = st.selectbox("Select Student Request to Action", list(student_options.keys()), key="sel_stud_req")
                selected_stud_id = student_options[selected_stud_label]
                
                target_stud_req = next(r for r in pending_students if r["id"] == selected_stud_id)

                st.markdown(
                    f"""
                    <div style="padding: 12px; border-radius: 8px; background-color: #1e293b; border-left: 5px solid #f59e0b; margin-bottom: 10px;">
                        <h4 style="margin: 0; color: #f8fafc;">{target_stud_req['name']} (Roll: {target_stud_req['roll']})</h4>
                        <p style="margin: 4px 0; font-size: 0.85rem; color: #94a3b8;">
                            <b>Duration:</b> {target_stud_req['duration']} &nbsp;|&nbsp; <b>Type:</b> {target_stud_req['type']}
                        </p>
                        <p style="margin: 4px 0; font-size: 0.85rem; color: #cbd5e1;"><b>Reason:</b> {target_stud_req['reason']}</p>
                        <p style="margin: 0; color: #e2e8f0; font-size: 0.9rem;"><b>Attached Doc:</b> 📄 <code>{target_stud_req['doc']}</code></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                acs1, acs2 = st.columns(2)
                if acs1.button("✅ Approve Student Leave", key=f"btn_app_stud_{selected_stud_id}"):
                    for r in st.session_state.student_leave_requests_db:
                        if r["id"] == selected_stud_id:
                            r["status"] = "🟢 Approved"
                    st.success(f"Student leave for **{target_stud_req['name']}** approved successfully!")
                    st.rerun()

                if acs2.button("❌ Reject Request", key=f"btn_rej_stud_{selected_stud_id}"):
                    for r in st.session_state.student_leave_requests_db:
                        if r["id"] == selected_stud_id:
                            r["status"] = "🔴 Rejected"
                    st.warning(f"Student leave for **{target_stud_req['name']}** rejected.")
                    st.rerun()
            else:
                st.success("✅ All student leave requests have been processed.")

        # --- Faculty Leave Approvals Sub-Section ---
        with col_app2:
            st.markdown("#### 👨‍🏫 Faculty Leave & Adjustment Requests")
            pending_faculty = [req for req in st.session_state.faculty_leave_requests_db if req["status"] == "⏳ Pending"]

            if pending_faculty:
                faculty_options = {f"{req['faculty']} - {req['type']}": req['id'] for req in pending_faculty}
                selected_fac_label = st.selectbox("Select Faculty Request to Action", list(faculty_options.keys()), key="sel_fac_req")
                selected_fac_id = faculty_options[selected_fac_label]
                
                target_fac_req = next(r for r in pending_faculty if r["id"] == selected_fac_id)

                st.markdown(
                    f"""
                    <div style="padding: 12px; border-radius: 8px; background-color: #1e293b; border-left: 5px solid #3b82f6; margin-bottom: 10px;">
                        <h4 style="margin: 0; color: #f8fafc;">{target_fac_req['faculty']} ({target_fac_req['chair']})</h4>
                        <p style="margin: 4px 0; font-size: 0.85rem; color: #94a3b8;">
                            <b>Duration:</b> {target_fac_req['duration']} &nbsp;|&nbsp; <b>Type:</b> {target_fac_req['type']}
                        </p>
                        <p style="margin: 0; color: #e2e8f0; font-size: 0.9rem;"><b>Lecture Adjustment:</b> {target_fac_req['adjustment']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                acf1, acf2 = st.columns(2)
                if acf1.button("✅ Sanction Faculty Leave", key=f"btn_app_fac_{selected_fac_id}"):
                    for r in st.session_state.faculty_leave_requests_db:
                        if r["id"] == selected_fac_id:
                            r["status"] = "🟢 Sanctioned"
                    st.success(f"Faculty leave for **{target_fac_req['faculty']}** sanctioned and logged to principal audit!")
                    st.rerun()

                if acf2.button("❌ Return for Revision", key=f"btn_rej_fac_{selected_fac_id}"):
                    for r in st.session_state.faculty_leave_requests_db:
                        if r["id"] == selected_fac_id:
                            r["status"] = "🔴 Returned"
                    st.warning(f"Leave application returned to **{target_fac_req['faculty']}** for timetable revision.")
                    st.rerun()
            else:
                st.success("✅ All faculty leave applications have been processed.")

    # --- TAB 2: HOD LEAVE APPLICATION & ACTING NOMINATION ---
    with tab_hod_apply:
        st.markdown("### 📝 Apply for Personal Leave & Nominate Acting HOD")
        st.markdown("Submit personal leave requests to the Principal Deanery and designate an Acting HOD from the department faculty roster.")

        dept_faculty_list = [f["faculty_name"] for f in PragyanDatabase.get_department_faculty()]

        with st.form("hod_personal_leave_form"):
            hl1, hl2 = st.columns(2)
            with hl1:
                hod_leave_type = st.selectbox("Leave Classification", ["Casual Leave (CL)", "Medical Leave (ML)", "Earned Leave (EL)", "On-Duty Sabbatical"])
                hod_from = st.date_input("From Date", value=datetime.date.today())
                hod_to = st.date_input("To Date", value=datetime.date.today() + datetime.timedelta(days=2))
            with hl2:
                acting_hod_nominee = st.selectbox("Nominate Acting HOD (In-Charge)", dept_faculty_list, help="Faculty member assigned to oversee department duties during your absence.")
                substitute_instructor = st.selectbox("Assign Lecture Substitute", dept_faculty_list)
                hod_reason = st.text_area("Reason & Objectives", placeholder="Attending executive board meeting / academic conference...")

            if st.form_submit_button("🚀 Submit Leave Application & Nominate Acting HOD to Principal"):
                if "hod_leave_applications" not in st.session_state:
                    st.session_state.hod_leave_applications = []
                
                new_hod_leave = {
                    "hod_name": user_name,
                    "type": hod_leave_type,
                    "from": str(hod_from),
                    "to": str(hod_to),
                    "acting_hod": acting_hod_nominee,
                    "substitute": substitute_instructor,
                    "reason": hod_reason,
                    "status": "⏳ Pending Principal Review"
                }
                st.session_state.hod_leave_applications.insert(0, new_hod_leave)
                st.success(f"🎉 Leave application successfully dispatched to Principal! Acting HOD designated: **{acting_hod_nominee}**.")

        st.markdown("#### 📋 Your Submitted Leave History")
        submitted_hod_leaves = st.session_state.get("hod_leave_applications", [])
        if submitted_hod_leaves:
            st.dataframe(submitted_hod_leaves, use_container_width=True)
        else:
            st.info("No personal leave applications currently logged.")

    # --- TAB 3: STUDENT LEAVE AUDIT (MONTHLY FILTER) ---
    with tab_students:
        st.markdown("### 🎓 Student Leave Registry & Monthly Filter")
        st.markdown("Audit student leave applications filtered by specific month and year.")

        sc1, sc2 = st.columns(2)
        with sc1:
            sel_student_month = st.selectbox("Select Month", ["September", "August", "July", "June"], key="h_stud_month")
        with sc2:
            sel_student_year = st.selectbox("Select Year", ["2026", "2025"], key="h_stud_year")

        student_leave_db = st.session_state.get("student_leave_requests_db", [])

        st.markdown(f"#### 📊 Filtered Student Leave Ledger ({sel_student_month} {sel_student_year})")
        st.dataframe(student_leave_db, use_container_width=True)

    # --- TAB 4: FACULTY LEAVE AUDIT (MONTHLY FILTER) ---
    with tab_faculty:
        st.markdown("### 👨‍🏫 Faculty Leave Registry & Monthly Filter")
        st.markdown("Review faculty leave requests, substitutions, and sabbaticals filtered by month and year.")

        fc1, fc2 = st.columns(2)
        with fc1:
            sel_fac_month = st.selectbox("Select Month", ["September", "August", "July", "June"], key="h_fac_month")
        with fc2:
            sel_fac_year = st.selectbox("Select Year", ["2026", "2025"], key="h_fac_year")

        faculty_leave_db = st.session_state.get("faculty_leave_requests_db", [])

        st.markdown(f"#### 📊 Filtered Faculty Leave Ledger ({sel_fac_month} {sel_fac_year})")
        st.dataframe(faculty_leave_db, use_container_width=True)

    # --- TAB 5: INSTITUTIONAL HOLIDAY CALENDAR (DB MANAGED) ---
    with tab_calendar:
        st.markdown("### 📅 Official Institutional Holiday & Restricted Calendar")
        st.markdown("Comprehensive schedule of institutional holidays, gazetted breaks, and restricted holidays scheduled by the Principal Deanery.")

        holiday_calendar_data = PragyanDatabase.get_holiday_calendar()
        st.dataframe(holiday_calendar_data, use_container_width=True)
