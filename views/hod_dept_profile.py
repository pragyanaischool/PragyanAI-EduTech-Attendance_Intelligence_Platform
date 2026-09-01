import streamlit as st
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_hod_dept_profile():
    """
    Renders the dedicated Departmental Management & Faculty Allocation Hub for HODs.
    Features:
    - Faculty Roster with Joined Dates and Roles (pulled from DB + CRUD onboarding).
    - Semester-wise Subject List and Assigned Faculties.
    - Semester-wise Class Schedule / Timetable.
    - Subject Allocation to Faculties (Regular).
    - Extra or Adhoc Class Allocation to Faculties.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. HOD (ECE)")
    PragyanDatabase.initialize_database()
    
    st.markdown(f"# 🏛️ Departmental Management & Faculty Allocation Hub — {user_name}")
    st.markdown("### *Manage Department Rosters, Semester Curriculum Allocations, Timetables, and Adhoc Duties.*")
    
    st.info(
        "💡 **Departmental Command Center:** Inspect faculty tenures, review semester course distributions, "
        "manage class schedules, and assign regular or adhoc teaching responsibilities."
    )

    st.markdown("---")

    # 2. Multi-Tab Departmental Governance Navigation
    tab_roster, tab_subjects, tab_schedule, tab_alloc = st.tabs([
        "👥 Faculty Roster & Tenure", 
        "📚 Semester Subjects & Instructors", 
        "📅 Semester Class Schedule", 
        "⚡ Subject & Adhoc Allocation"
    ])

    # --- TAB 1: FACULTY ROSTER & JOINED DATE / ROLE ---
    with tab_roster:
        st.markdown("### 👥 Department Faculty Directory & Tenure")
        st.markdown("Complete roster of all faculty members in the Electronics & Communication department, including joined dates and designated roles.")

        faculty_directory = PragyanDatabase.get_department_faculty()
        
        # Search & Filter Roster
        search_term = st.text_input("🔍 Search Faculty by Name or Role", placeholder="Type faculty name...")
        filtered_roster = faculty_directory
        if search_term.strip():
            filtered_roster = [f for f in filtered_roster if search_term.lower() in f["faculty_name"].lower() or search_term.lower() in f["role"].lower()]

        st.dataframe(filtered_roster, use_container_width=True)

        # Quick Add Faculty Expander
        with st.expander("➕ Onboard New Department Faculty Member"):
            with st.form("onboard_faculty_form"):
                fc1, fc2 = st.columns(2)
                with fc1:
                    new_f_name = st.text_input("Faculty Full Name", placeholder="Dr. Jane Doe")
                    new_f_role = st.selectbox("Designation / Role", ["Professor", "Associate Professor", "Assistant Professor", "Senior Lecturer"])
                with fc2:
                    new_f_date = st.date_input("Joined Date", value=datetime.date.today())
                    new_f_courses = st.text_input("Assigned Courses", placeholder="ECE301, ECE302")

                if st.form_submit_button("🚀 Onboard Faculty to Department"):
                    new_faculty_entry = {
                        "faculty_name": new_f_name,
                        "role": new_f_role,
                        "joined_date": str(new_f_date),
                        "active_courses": new_f_courses,
                        "status": "🟢 Active"
                    }
                    PragyanDatabase.add_department_faculty(new_faculty_entry)
                    st.success(f"🎉 Faculty **{new_f_name}** successfully added to the department roster!")
                    st.rerun()

    # --- TAB 2: SEMESTER SUBJECT LIST & FACULTIES TAKING SUBJECTS ---
    with tab_subjects:
        st.markdown("### 📚 Semester-Wise Subject List & Assigned Faculties")
        st.markdown("Inspection matrix mapping curriculum subjects to active faculty instructors per semester.")

        all_allocations = PragyanDatabase.get_course_allocations()
        sem_choice = st.selectbox("Select Semester for Curriculum Audit", ["Semester 3", "Semester 5", "Semester 7"], key="dept_sem_choice")

        filtered_allocs = [a for a in all_allocations if sem_choice.lower() in a.get("semester", "").lower()]
        if filtered_allocs:
            st.dataframe(filtered_allocs, use_container_width=True)
        else:
            st.info(f"No specific subject allocations logged for **{sem_choice}** yet.")

    # --- TAB 3: SEMESTER CLASS SCHEDULE ---
    with tab_schedule:
        st.markdown("### 📅 Semester Master Class Schedule & Timetable")
        st.markdown("Comprehensive weekly lecture scheduling across department lecture halls and labs.")

        schedule_table = [
            {"Time Slot": "09:00 AM - 10:00 AM", "Monday": "ECE301 (Lab A)", "Tuesday": "ECE501 (Hall 2)", "Wednesday": "ECE301 (Hall 1)", "Thursday": "ECE502 (Hall 2)", "Friday": "ECE701 (Hall 1)"},
            {"Time Slot": "10:00 AM - 11:00 AM", "Monday": "ECE302 (Hall 1)", "Tuesday": "ECE502 (Hall 2)", "Wednesday": "ECE303 (Hall 1)", "Thursday": "ECE501 (Hall 2)", "Friday": "ECE702 (Hall 1)"},
            {"Time Slot": "11:30 AM - 12:30 PM", "Monday": "ECE503 (Hall 2)", "Tuesday": "ECE301 (Lab B)", "Wednesday": "ECE501 (Hall 2)", "Thursday": "ECE303 (Hall 1)", "Friday": "ECE302 (Hall 2)"},
            {"Time Slot": "02:00 PM - 04:00 PM", "Monday": "Department Research Colloquium", "Tuesday": "Faculty Board Meeting", "Wednesday": "VLSI Lab Practical", "Thursday": "Embedded Systems Lab", "Friday": "Project Mentorship"}
        ]
        st.dataframe(schedule_table, use_container_width=True)

    # --- TAB 4: ALLOCATE SUBJECT & ADHOC CLASS TO FACULTIES ---
    with tab_alloc:
        st.markdown("### ⚡ Subject Allocation & Extra / Adhoc Class Assignment")
        st.markdown("Allocate regular semester subjects or assign extra/adhoc makeup lecture duties to department faculty.")

        alloc_mode = st.radio("Select Allocation Mode", ["📖 Allocate Regular Subject", "⚡ Allocate Extra / Adhoc Class"], horizontal=True)

        department_faculty_list = [f["faculty_name"] for f in PragyanDatabase.get_department_faculty()]

        if "Regular Subject" in alloc_mode:
            with st.form("hod_dept_regular_alloc_form"):
                st.markdown("#### 📖 Regular Subject-to-Faculty Assignment")
                
                ac1, ac2 = st.columns(2)
                with ac1:
                    target_faculty = st.selectbox("Select Faculty Member", department_faculty_list)
                    subject_input = st.text_input("Subject Code & Title", value="ECE305 - Advanced Computer Architecture")
                with ac2:
                    target_semester = st.selectbox("Assign to Semester", ["Semester 3", "Semester 5", "Semester 7"])
                    academic_term = st.selectbox("Academic Term", ["Fall 2026", "Spring 2027"])

                if st.form_submit_button("🚀 Confirm Regular Subject Assignment"):
                    new_alloc = {
                        "course_code": subject_input.split(" - ")[0],
                        "subject_name": subject_input.split(" - ")[1] if " - " in subject_input else subject_input,
                        "semester": target_semester,
                        "faculty_in_charge": target_faculty,
                        "enrolled": 45
                    }
                    PragyanDatabase.assign_course(new_alloc)
                    st.success(f"🎉 Subject **{subject_input}** successfully assigned to **{target_faculty}** for **{target_semester}**!")
                    st.rerun()
        
        else:
            with st.form("hod_dept_adhoc_alloc_form"):
                st.markdown("#### ⚡ Extra / Adhoc Class Allocation Form")
                st.markdown("Assign substitute lectures, make-up sessions, or adhoc tutorial duties.")
                
                ax1, ax2 = st.columns(2)
                with ax1:
                    adhoc_faculty = st.selectbox("Select Faculty for Adhoc Duty", department_faculty_list)
                    adhoc_subject = st.text_input("Course Code / Topic", value="ECE301 - Digital Logic Design (Makeup Lecture)")
                    adhoc_date = st.date_input("Scheduled Date", value=datetime.date.today() + datetime.timedelta(days=1))
                with ax2:
                    adhoc_slot = st.selectbox("Time Slot", ["09:00 AM - 10:00 AM", "11:30 AM - 12:30 PM", "03:00 PM - 04:00 PM"])
                    adhoc_venue = st.text_input("Lecture Hall / Lab", value="Lecture Hall 102")
                    adhoc_reason = st.text_area("Reason / Objective", placeholder="Substitute for faculty sabbatical / curriculum pacing makeup...")

                if st.form_submit_button("⚡ Authorize & Dispatch Adhoc Class Assignment"):
                    new_adhoc = {
                        "faculty": adhoc_faculty,
                        "topic": adhoc_subject,
                        "date": str(adhoc_date),
                        "slot": adhoc_slot,
                        "venue": adhoc_venue
                    }
                    PragyanDatabase.assign_adhoc_class(new_adhoc)
                    st.success(f"🎉 Adhoc class for **{adhoc_subject}** successfully assigned to **{adhoc_faculty}** on **{adhoc_date}** at **{adhoc_slot}** in **{adhoc_venue}**!")
                    st.rerun()
