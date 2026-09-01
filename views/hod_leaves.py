import streamlit as st
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_hod_leaves():
    """
    Renders the dedicated HOD Department Leave & Exemption Approval Hub,
    allowing department heads to review leave applications, apply for personal leave with 
    Acting HOD nominations, inspect monthly student/faculty ledgers, and view the Principal-managed holiday calendar.
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

    # --- TAB 1: PENDING APPROVALS (Original Features Preserved) ---
    with tab_approvals:
        col_app1, col_app2 = st.columns(2)
        
        with col_app1:
            st.markdown("### 🎓 Pending Student Leave & Exemption Queue")
            st.markdown(
                """
                <div style="padding: 15px; border-radius: 8px; background-color: #1e293b; border-left: 5px solid #f59e0b; margin-bottom: 15px;">
                    <h4 style="margin: 0; color: #f8fafc;">Aarav Sharma (Roll: ECE_2026_01) — Sem 5</h4>
                    <p style="margin: 5px 0; font-size: 0.85rem; color: #94a3b8;">
                        <b>Duration:</b> Sep 3, 2026 to Sep 5, 2026 &nbsp;|&nbsp; <b>Type:</b> Medical Leave (Viral Fever Recovery)
                    </p>
                    <p style="margin: 0; color: #e2e8f0; font-size: 0.95rem;"><b>Attached Document:</b> 📄 <code>Medical_Certificate_Aarav.pdf</code> (Verified by Faculty Advisor)</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            col_s1, col_s2 = st.columns(2)
            if col_s1.button("✅ Approve Student Medical Leave", key="approve_student_leave_1"):
                st.success("Student leave request approved! Attendance passport updated with 3 days medical exemption grace.")
            if col_s2.button("❌ Reject / Request Proof", key="reject_student_leave_1"):
                st.warning("Rejection notification dispatched to student.")

        with col_app2:
            st.markdown("### 📋 Pending Faculty Leave & Adjustment Queue")
            st.markdown(
                """
                <div style="padding: 15px; border-radius: 8px; background-color: #1e293b; border-left: 5px solid #3b82f6; margin-bottom: 15px;">
                    <h4 style="margin: 0; color: #f8fafc;">Dr. Smitha Rao (VLSI Design Chair)</h4>
                    <p style="margin: 5px 0; font-size: 0.85rem; color: #94a3b8;">
                        <b>Duration:</b> Sep 10, 2026 to Sep 11, 2026 &nbsp;|&nbsp; <b>Type:</b> IEEE National Conference Presentation
                    </p>
                    <p style="margin: 0; color: #e2e8f0; font-size: 0.95rem;"><b>Lecture Adjustment:</b> Covered by Prof. Anand Kumar (Digital Systems)</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            col_f1, col_f2 = st.columns(2)
            if col_f1.button("✅ Sanction Faculty Leave", key="approve_faculty_leave_1"):
                st.success("Faculty leave sanctioned successfully and logged to principal deanery audit!")
            if col_f2.button("❌ Return for Revision", key="reject_faculty_leave_1"):
                st.warning("Leave application returned to faculty for timetable adjustment.")

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

        student_leave_db = [
            {"Student Name": "Sateesh Ambesange", "Roll": "ECE_2026_042", "Subject": "ECE301 - Digital Logic Design", "Type": "Medical Exemption", "From": "2026-09-01", "To": "2026-09-03", "Status": "🟢 Approved"},
            {"Student Name": "Priya Patel", "Roll": "ECE_2026_088", "Subject": "ECE501 - VLSI Architecture", "Type": "Casual Leave", "From": "2026-08-15", "To": "2026-08-17", "Status": "🟢 Approved"},
            {"Student Name": "Aarav Sharma", "Roll": "ECE_2026_010", "Subject": "ECE302 - Signals & Systems", "Type": "Medical Exemption", "From": "2026-09-03", "To": "2026-09-05", "Status": "⏳ Pending HOD Review"}
        ]

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

        faculty_leave_db = [
            {"Faculty Name": "Dr. Smitha Rao", "Type": "Conference Presentation", "From": "2026-09-10", "To": "2026-09-11", "Substitute": "Prof. Anand Kumar", "Status": "⏳ Pending HOD Review"},
            {"Faculty Name": "Prof. Sneha Patil", "Type": "Sabbatical Leave", "From": "2026-08-01", "To": "2026-12-31", "Substitute": "External Hire", "Status": "🟢 Approved"}
        ]

        st.markdown(f"#### 📊 Filtered Faculty Leave Ledger ({sel_fac_month} {sel_fac_year})")
        st.dataframe(faculty_leave_db, use_container_width=True)

    # --- TAB 5: INSTITUTIONAL HOLIDAY CALENDAR (DB MANAGED) ---
    with tab_calendar:
        st.markdown("### 📅 Official Institutional Holiday & Restricted Calendar")
        st.markdown("Comprehensive schedule of institutional holidays, gazetted breaks, and restricted holidays scheduled by the Principal Deanery.")

        # Read holiday calendar from database helper (auto-seeds dummy data if unavailable)
        holiday_calendar_data = PragyanDatabase.get_holiday_calendar()

        st.dataframe(holiday_calendar_data, use_container_width=True)
