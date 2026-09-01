import streamlit as st
import datetime

class PragyanDatabase:
    """
    Core Database & Session State Management for PragyanAI Institutional Platform.
    Handles persistent storage for students with comprehensive multi-subject attendance tracking, 
    faculty portfolios with departments, degrees, designations, experience metrics, leave applications,
    semester course allocations, internal student assessment marks, adhoc duties, master calendars, and principal executive profiles.
    """

    @staticmethod
    def initialize_database():
        """Initializes default database tables in st.session_state if not already present."""
        if "db_initialized" not in st.session_state:
            st.session_state.db_initialized = False

        # 1. Expanded Students Database with Multi-Subject Tracking Across Semesters 3, 5, and 7
        if "students_db" not in st.session_state:
            st.session_state.students_db = [
                # --- SEMESTER 5 STUDENTS ---
                {
                    "roll": "ECE_2026_042", 
                    "name": "Sateesh Ambesange", 
                    "department": "Electronics & Communication (ECE)", 
                    "semester": "Semester 5", 
                    "attendance_percentage": 91.5, 
                    "exam_eligibility_status": "🟢 Safe",
                    "subjects": {
                        "ECE501 - VLSI Architecture": {"held": 38, "attended": 36, "pct": 94.7, "status": "🟢 Safe"},
                        "ECE502 - Microcontrollers": {"held": 40, "attended": 37, "pct": 92.5, "status": "🟢 Safe"},
                        "ECE503 - Digital Signal Processing": {"held": 35, "attended": 31, "pct": 88.5, "status": "🟢 Safe"},
                        "ECE504 - Control Systems": {"held": 32, "attended": 29, "pct": 90.6, "status": "🟢 Safe"}
                    }
                },
                {
                    "roll": "ECE_2026_010", 
                    "name": "Aarav Sharma", 
                    "department": "Electronics & Communication (ECE)", 
                    "semester": "Semester 5", 
                    "attendance_percentage": 88.2, 
                    "exam_eligibility_status": "🟢 Safe",
                    "subjects": {
                        "ECE501 - VLSI Architecture": {"held": 38, "attended": 34, "pct": 89.4, "status": "🟢 Safe"},
                        "ECE502 - Microcontrollers": {"held": 40, "attended": 35, "pct": 87.5, "status": "🟢 Safe"},
                        "ECE503 - Digital Signal Processing": {"held": 35, "attended": 30, "pct": 85.7, "status": "🟢 Safe"},
                        "ECE504 - Control Systems": {"held": 32, "attended": 28, "pct": 87.5, "status": "🟢 Safe"}
                    }
                },
                {
                    "roll": "ECE_2026_088", 
                    "name": "Priya Patel", 
                    "department": "Electronics & Communication (ECE)", 
                    "semester": "Semester 5", 
                    "attendance_percentage": 72.0, 
                    "exam_eligibility_status": "🟡 At-Risk (<75%)",
                    "subjects": {
                        "ECE501 - VLSI Architecture": {"held": 38, "attended": 29, "pct": 76.3, "status": "🟡 Warning"},
                        "ECE502 - Microcontrollers": {"held": 40, "attended": 28, "pct": 70.0, "status": "🔴 Shortage Risk"},
                        "ECE503 - Digital Signal Processing": {"held": 35, "attended": 25, "pct": 71.4, "status": "🔴 Shortage Risk"},
                        "ECE504 - Control Systems": {"held": 32, "attended": 23, "pct": 71.8, "status": "🔴 Shortage Risk"}
                    }
                },
                {
                    "roll": "ECE_2026_055", 
                    "name": "Kiran Kumar", 
                    "department": "Electronics & Communication (ECE)", 
                    "semester": "Semester 5", 
                    "attendance_percentage": 94.0, 
                    "exam_eligibility_status": "🟢 Safe",
                    "subjects": {
                        "ECE501 - VLSI Architecture": {"held": 38, "attended": 36, "pct": 94.7, "status": "🟢 Safe"},
                        "ECE502 - Microcontrollers": {"held": 40, "attended": 38, "pct": 95.0, "status": "🟢 Safe"},
                        "ECE503 - Digital Signal Processing": {"held": 35, "attended": 33, "pct": 94.2, "status": "🟢 Safe"},
                        "ECE504 - Control Systems": {"held": 32, "attended": 30, "pct": 93.7, "status": "🟢 Safe"}
                    }
                },
                {
                    "roll": "ECE_2026_071", 
                    "name": "Neha Gupta", 
                    "department": "Electronics & Communication (ECE)", 
                    "semester": "Semester 5", 
                    "attendance_percentage": 69.5, 
                    "exam_eligibility_status": "🔴 Shortage Risk",
                    "subjects": {
                        "ECE501 - VLSI Architecture": {"held": 38, "attended": 26, "pct": 68.4, "status": "🔴 Shortage Risk"},
                        "ECE502 - Microcontrollers": {"held": 40, "attended": 28, "pct": 70.0, "status": "🔴 Shortage Risk"},
                        "ECE503 - Digital Signal Processing": {"held": 35, "attended": 24, "pct": 68.5, "status": "🔴 Shortage Risk"},
                        "ECE504 - Control Systems": {"held": 32, "attended": 22, "pct": 68.7, "status": "🔴 Shortage Risk"}
                    }
                },

                # --- SEMESTER 3 STUDENTS ---
                {
                    "roll": "ECE_2026_102", 
                    "name": "Rohan Verma", 
                    "department": "Electronics & Communication (ECE)", 
                    "semester": "Semester 3", 
                    "attendance_percentage": 84.5, 
                    "exam_eligibility_status": "🟢 Safe",
                    "subjects": {
                        "ECE301 - Digital Logic Design": {"held": 36, "attended": 31, "pct": 86.1, "status": "🟢 Safe"},
                        "ECE302 - Signals & Systems": {"held": 34, "attended": 29, "pct": 85.2, "status": "🟢 Safe"},
                        "ECE303 - Network Theory": {"held": 32, "attended": 26, "pct": 81.2, "status": "🟢 Safe"},
                        "ECE304 - Electronic Devices": {"held": 30, "attended": 26, "pct": 86.6, "status": "🟢 Safe"}
                    }
                },
                {
                    "roll": "ECE_2026_108", 
                    "name": "Divya Swaminathan", 
                    "department": "Electronics & Communication (ECE)", 
                    "semester": "Semester 3", 
                    "attendance_percentage": 92.1, 
                    "exam_eligibility_status": "🟢 Safe",
                    "subjects": {
                        "ECE301 - Digital Logic Design": {"held": 36, "attended": 34, "pct": 94.4, "status": "🟢 Safe"},
                        "ECE302 - Signals & Systems": {"held": 34, "attended": 31, "pct": 91.1, "status": "🟢 Safe"},
                        "ECE303 - Network Theory": {"held": 32, "attended": 29, "pct": 90.6, "status": "🟢 Safe"},
                        "ECE304 - Electronic Devices": {"held": 30, "attended": 28, "pct": 93.3, "status": "🟢 Safe"}
                    }
                },
                {
                    "roll": "ECE_2026_120", 
                    "name": "Aditya Rao", 
                    "department": "Electronics & Communication (ECE)", 
                    "semester": "Semester 3", 
                    "attendance_percentage": 74.0, 
                    "exam_eligibility_status": "🟡 At-Risk (<75%)",
                    "subjects": {
                        "ECE301 - Digital Logic Design": {"held": 36, "attended": 28, "pct": 77.7, "status": "🟡 Warning"},
                        "ECE302 - Signals & Systems": {"held": 34, "attended": 25, "pct": 73.5, "status": "🔴 Shortage Risk"},
                        "ECE303 - Network Theory": {"held": 32, "attended": 23, "pct": 71.8, "status": "🔴 Shortage Risk"},
                        "ECE304 - Electronic Devices": {"held": 30, "attended": 24, "pct": 80.0, "status": "🟢 Safe"}
                    }
                },

                # --- SEMESTER 7 STUDENTS ---
                {
                    "roll": "ECE_2026_115", 
                    "name": "Ananya Iyer", 
                    "department": "Electronics & Communication (ECE)", 
                    "semester": "Semester 7", 
                    "attendance_percentage": 68.0, 
                    "exam_eligibility_status": "🔴 Shortage Risk",
                    "subjects": {
                        "ECE701 - Wireless Communications": {"held": 30, "attended": 21, "pct": 70.0, "status": "🔴 Shortage Risk"},
                        "ECE702 - AI in EDA": {"held": 28, "attended": 18, "pct": 64.2, "status": "🔴 Shortage Risk"},
                        "ECE703 - RF Circuit Design": {"held": 32, "attended": 23, "pct": 71.8, "status": "🔴 Shortage Risk"}
                    }
                },
                {
                    "roll": "ECE_2026_130", 
                    "name": "Karthik Hegde", 
                    "department": "Electronics & Communication (ECE)", 
                    "semester": "Semester 7", 
                    "attendance_percentage": 89.5, 
                    "exam_eligibility_status": "🟢 Safe",
                    "subjects": {
                        "ECE701 - Wireless Communications": {"held": 30, "attended": 27, "pct": 90.0, "status": "🟢 Safe"},
                        "ECE702 - AI in EDA": {"held": 28, "attended": 25, "pct": 89.2, "status": "🟢 Safe"},
                        "ECE703 - RF Circuit Design": {"held": 32, "attended": 28, "pct": 87.5, "status": "🟢 Safe"}
                    }
                }
            ]

        # 2. Faculty Allocations Database
        if "faculty_allocations_db" not in st.session_state:
            st.session_state.faculty_allocations_db = [
                {"faculty": "Dr. Smitha Rao", "subject": "ECE301 - Digital Logic Design", "semester": "Semester 3", "enrolled": 48},
                {"faculty": "Dr. Smitha Rao", "subject": "ECE501 - VLSI Architecture", "semester": "Semester 5", "enrolled": 52},
                {"faculty": "Dr. Anand Kumar", "subject": "ECE303 - Signals & Systems", "semester": "Semester 3", "enrolled": 48}
            ]

        # 3. HOD Governance Records
        if "hod_records_db" not in st.session_state:
            st.session_state.hod_records_db = [
                {
                    "hod_name": "Dr. HOD (ECE)",
                    "department": "Electronics & Communication (ECE)",
                    "college": "PragyanAI Institute of Technology & Venture Studio",
                    "availability_status": "Available in Office Block A",
                    "active_policy": "Strict 75% Shortage Threshold & Mandatory Medical Exemption Filings"
                }
            ]

        # 4. Department Faculty Roster
        if "department_faculty_db" not in st.session_state:
            st.session_state.department_faculty_db = [
                {
                    "department": "Electronics & Communication (ECE)",
                    "faculty_name": "Dr. Smitha Rao",
                    "degree": "Ph.D. in VLSI Design (IISc Bangalore)",
                    "designation": "Professor & Senior Researcher",
                    "joined_date": "2018-06-15",
                    "college_experience_years": 8,
                    "total_experience_years": 16,
                    "active_courses": "ECE301, ECE501",
                    "status": "🟢 Active"
                },
                {
                    "department": "Electronics & Communication (ECE)",
                    "faculty_name": "Dr. Anand Kumar",
                    "degree": "Ph.D. in Signal Processing (IIT Madras)",
                    "designation": "Associate Professor",
                    "joined_date": "2020-07-01",
                    "college_experience_years": 6,
                    "total_experience_years": 12,
                    "active_courses": "ECE302, ECE303",
                    "status": "🟢 Active"
                },
                {
                    "department": "Electronics & Communication (ECE)",
                    "faculty_name": "Prof. Meena Hegde",
                    "degree": "M.Tech in Embedded Systems (NITK Surathkal)",
                    "designation": "Assistant Professor",
                    "joined_date": "2021-08-10",
                    "college_experience_years": 5,
                    "total_experience_years": 9,
                    "active_courses": "ECE502, ECE504",
                    "status": "🟢 Active"
                },
                {
                    "department": "Artificial Intelligence & Data Science",
                    "faculty_name": "Dr. Kavitha Murthy",
                    "degree": "Ph.D. in Machine Learning (IIT Bombay)",
                    "designation": "Professor & HOD (AI & DS)",
                    "joined_date": "2019-05-10",
                    "college_experience_years": 7,
                    "total_experience_years": 15,
                    "active_courses": "AI501, AI502",
                    "status": "🟢 Active"
                },
                {
                    "department": "Artificial Intelligence & Data Science",
                    "faculty_name": "Prof. Raghavendra Swamy",
                    "degree": "M.Tech in Data Engineering (BITS Pilani)",
                    "designation": "Assistant Professor",
                    "joined_date": "2022-01-15",
                    "college_experience_years": 4,
                    "total_experience_years": 8,
                    "active_courses": "AI301, AI402",
                    "status": "🟢 Active"
                },
                {
                    "department": "Computer Science & Engineering",
                    "faculty_name": "Dr. Rajesh Hegde",
                    "degree": "Ph.D. in Distributed Systems (Stanford University)",
                    "designation": "Professor & HOD (CSE)",
                    "joined_date": "2017-08-01",
                    "college_experience_years": 9,
                    "total_experience_years": 18,
                    "active_courses": "CSE401, CSE502",
                    "status": "🟢 Active"
                },
                {
                    "department": "Electrical & Electronics Engineering",
                    "faculty_name": "Prof. Anand Rao",
                    "degree": "M.Tech in Power Electronics (IIT Roorkee)",
                    "designation": "Associate Professor & HOD (EEE)",
                    "joined_date": "2020-09-01",
                    "college_experience_years": 6,
                    "total_experience_years": 14,
                    "active_courses": "EEE301, EEE402",
                    "status": "🟢 Active"
                }
            ]

        # 5. Semester Course Allocations
        if "course_allocations_db" not in st.session_state:
            st.session_state.course_allocations_db = [
                {"course_code": "ECE301", "subject_name": "Digital Logic Design", "semester": "Semester 3", "faculty_in_charge": "Dr. Smitha Rao", "enrolled": 48},
                {"course_code": "ECE302", "subject_name": "Signals & Systems", "semester": "Semester 3", "faculty_in_charge": "Dr. Anand Kumar", "enrolled": 48},
                {"course_code": "ECE501", "subject_name": "VLSI Architecture", "semester": "Semester 5", "faculty_in_charge": "Dr. Smitha Rao", "enrolled": 52},
                {"course_code": "ECE502", "subject_name": "Microcontrollers & Embedded Systems", "semester": "Semester 5", "faculty_in_charge": "Prof. Meena Hegde", "enrolled": 52}
            ]

        # 6. Adhoc Class Allocations
        if "adhoc_classes_db" not in st.session_state:
            st.session_state.adhoc_classes_db = [
                {"faculty": "Dr. Smitha Rao", "topic": "ECE301 - Digital Logic Design (Makeup Lecture)", "date": "2026-09-03", "slot": "11:30 AM - 12:30 PM", "venue": "Lecture Hall 102"}
            ]

        # 7. Principal Executive Profile Database
        if "principal_executive_profile_db" not in st.session_state:
            st.session_state.principal_executive_profile_db = {
                "full_name": "Dr. Principal Dean",
                "email": "principal@pragyan.edu",
                "employee_id": "EXEC_PRINCIPAL_2026_01",
                "admin_office": "Main Block - Executive Deanery & Council",
                "office_location": "Block A, Suite 101 (Central Administration)",
                "office_hours": "Mon, Wed, Fri: 11:00 AM - 2:00 PM",
                "position_start_date": datetime.date(2022, 7, 15),
                "resume_link": "https://pragyanai.edu/resumes/principal_cv.pdf",
                "linkedin_link": "https://linkedin.com/in/principal-dean-pragyanai",
                "research_profile": "https://scholar.google.com/citations?user=principal_sample",
                "keen_interests": "Agentic AI in Higher Education Governance, Automated EDA Verification, Institutional Scalability Models",
                "bio": "Principal & Chief Academic Officer. Directing institutional digital transformation, attendance intelligence compliance, and multi-department student success frameworks.",
                "digest_alerts": True,
                "sms_alerts": True,
                "broadcast_privilege": True,
                "pdf_logging": True
            }

        # 8. Faculty Leave Records Database (Connected to HOD & Principal Leave Portals)
        if "faculty_leaves_db" not in st.session_state:
            st.session_state.faculty_leaves_db = [
                {"id": 1, "faculty_name": "Dr. Smitha Rao", "department": "Electronics & Communication (ECE)", "start_date": "2026-10-01", "end_date": "2026-10-15", "reason": "International IEEE VLSI Summit Keynote Sabbatical", "status": "Pending"},
                {"id": 2, "faculty_name": "Prof. Meena Hegde", "department": "Electronics & Communication (ECE)", "start_date": "2026-09-15", "end_date": "2026-09-16", "reason": "Medical Leave", "status": "Pending"},
                {"id": 3, "faculty_name": "Dr. Anand Kumar", "department": "Electronics & Communication (ECE)", "start_date": "2026-08-01", "end_date": "2026-08-03", "reason": "Personal Travel", "status": "Approved"},
                {"id": 4, "faculty_name": "Prof. Sneha Patil", "department": "Electronics & Communication (ECE)", "start_date": "2026-09-20", "end_date": "2026-09-25", "reason": "Sabbatical Research", "status": "Approved"}
            ]

        # 9. Institutional Master Calendar Database
        if "holiday_calendar_db" not in st.session_state:
            st.session_state.holiday_calendar_db = [
                # January 2026
                {"date": "2026-01-26", "year": 2026, "month": "January", "title": "Republic Day", "category": "🔴 National Holiday", "badge_color": "#ef4444"},
                # March 2026
                {"date": "2026-03-04", "year": 2026, "month": "March", "title": "Holi Festival", "category": "🔵 Gazetted Holiday", "badge_color": "#3b82f6"},
                {"date": "2026-03-19", "year": 2026, "month": "March", "title": "Ugadi / Gudi Padwa", "category": "🟡 Restricted Holiday", "badge_color": "#f59e0b"},
                # April 2026
                {"date": "2026-04-03", "year": 2026, "month": "April", "title": "Good Friday", "category": "🔵 Gazetted Holiday", "badge_color": "#3b82f6"},
                # June 2026 (Semester Break)
                {"date": "2026-06-01 to 2026-06-15", "year": 2026, "month": "June", "title": "Summer Semester In-Between Break", "category": "🏖️ Semester Break", "badge_color": "#10b981"},
                # August 2026
                {"date": "2026-08-15", "year": 2026, "month": "August", "title": "Independence Day", "category": "🔴 National Holiday", "badge_color": "#ef4444"},
                {"date": "2026-08-21", "year": 2026, "month": "August", "title": "Varalakshmi Vratha", "category": "🟡 Restricted Holiday", "badge_color": "#f59e0b"},
                # September 2026
                {"date": "2026-09-14", "year": 2026, "month": "September", "title": "Ganesh Chaturthi", "category": "🔵 Gazetted Holiday", "badge_color": "#3b82f6"},
                {"date": "2026-09-22 to 2026-09-26", "year": 2026, "month": "September", "title": "Mid-Term Continuous Assessments (CA-1)", "category": "📝 Examination Window", "badge_color": "#6366f1"},
                # October 2026
                {"date": "2026-10-02", "year": 2026, "month": "October", "title": "Gandhi Jayanthi", "category": "🔴 National Holiday", "badge_color": "#ef4444"},
                {"date": "2026-10-05", "year": 2026, "month": "October", "title": "PragyanAI Annual Deep-Tech Hackathon", "category": "🎓 Institutional Event", "badge_color": "#8b5cf6"},
                {"date": "2026-10-12 to 2026-10-17", "year": 2026, "month": "October", "title": "Practical & Lab Viva Examinations", "category": "📝 Examination Window", "badge_color": "#6366f1"},
                {"date": "2026-10-18", "year": 2026, "month": "October", "title": "IEEE International Conference on VLSI & AI", "category": "🎓 Institutional Event", "badge_color": "#8b5cf6"},
                {"date": "2026-10-20", "year": 2026, "month": "October", "title": "Vijayadashami (Dasara)", "category": "🔵 Gazetted Holiday", "badge_color": "#3b82f6"},
                # November 2026
                {"date": "2026-11-08", "year": 2026, "month": "November", "title": "Deepavali Festival", "category": "🔵 Gazetted Holiday", "badge_color": "#3b82f6"},
                {"date": "2026-11-12", "year": 2026, "month": "November", "title": "Inter-Collegiate Cultural Fest 'Vanya 2026'", "category": "🎓 Institutional Event", "badge_color": "#8b5cf6"},
                {"date": "2026-11-23 to 2026-12-10", "year": 2026, "month": "November", "title": "End-Semester Terminal Examinations", "category": "📝 Examination Window", "badge_color": "#6366f1"},
                # December 2026
                {"date": "2026-12-11 to 2026-12-31", "year": 2026, "month": "December", "title": "Winter Semester Between Break", "category": "🏖️ Semester Break", "badge_color": "#10b981"},
                {"date": "2026-12-25", "year": 2026, "month": "December", "title": "Christmas Day", "category": "🔵 Gazetted Holiday", "badge_color": "#3b82f6"}
            ]

        # 10. Student Internal Marks Database (Assessments 1, 2, 3 & Best of Two Average)
        if "student_marks_db" not in st.session_state:
            st.session_state.student_marks_db = [
                {"roll": "ECE_2026_042", "name": "Sateesh Ambesange", "subject": "ECE501 - VLSI Architecture", "internal_1": 22.0, "internal_2": 24.5, "internal_3": 23.0, "best_avg": 23.75, "status": "🟢 Distinction"},
                {"roll": "ECE_2026_010", "name": "Aarav Sharma", "subject": "ECE501 - VLSI Architecture", "internal_1": 19.0, "internal_2": 21.0, "internal_3": 20.5, "best_avg": 20.75, "status": "🟢 First Class"},
                {"roll": "ECE_2026_088", "name": "Priya Patel", "subject": "ECE501 - VLSI Architecture", "internal_1": 14.0, "internal_2": 15.5, "internal_3": 16.0, "best_avg": 15.75, "status": "🟡 Remedial Required"},
                {"roll": "ECE_2026_055", "name": "Kiran Kumar", "subject": "ECE501 - VLSI Architecture", "internal_1": 24.0, "internal_2": 25.0, "internal_3": 24.5, "best_avg": 24.75, "status": "🟢 Distinction"},
                {"roll": "ECE_2026_102", "name": "Rohan Verma", "subject": "ECE301 - Digital Logic Design", "internal_1": 18.0, "internal_2": 20.0, "internal_3": 19.5, "best_avg": 19.75, "status": "🟢 First Class"}
            ]

        st.session_state.db_initialized = True

    # --- Student Database Accessors ---
    @staticmethod
    def get_students():
        PragyanDatabase.initialize_database()
        return st.session_state.students_db

    @staticmethod
    def add_student(student_data):
        PragyanDatabase.initialize_database()
        st.session_state.students_db.insert(0, student_data)

    # --- Faculty Allocation Accessors ---
    @staticmethod
    def get_faculty_allocations():
        PragyanDatabase.initialize_database()
        return st.session_state.faculty_allocations_db

    @staticmethod
    def add_faculty_allocation(allocation_data):
        PragyanDatabase.initialize_database()
        st.session_state.faculty_allocations_db.insert(0, allocation_data)

    # --- HOD Record Accessors ---
    @staticmethod
    def get_hod_records():
        PragyanDatabase.initialize_database()
        return st.session_state.hod_records_db

    # --- Department Faculty Roster Accessors & CRUD ---
    @staticmethod
    def get_department_faculty():
        PragyanDatabase.initialize_database()
        return st.session_state.department_faculty_db

    @staticmethod
    def add_department_faculty(faculty_data):
        PragyanDatabase.initialize_database()
        st.session_state.department_faculty_db.insert(0, faculty_data)

    # --- Semester Course Allocation Accessors & CRUD ---
    @staticmethod
    def get_course_allocations():
        PragyanDatabase.initialize_database()
        return st.session_state.course_allocations_db

    @staticmethod
    def assign_course(allocation_data):
        PragyanDatabase.initialize_database()
        st.session_state.course_allocations_db.insert(0, allocation_data)

    # --- Adhoc Class Allocation Accessors & CRUD ---
    @staticmethod
    def get_adhoc_classes():
        PragyanDatabase.initialize_database()
        return st.session_state.adhoc_classes_db

    @staticmethod
    def assign_adhoc_class(adhoc_data):
        PragyanDatabase.initialize_database()
        st.session_state.adhoc_classes_db.insert(0, adhoc_data)

    # --- Faculty Leave Accessors & Persistence ---
    @staticmethod
    def get_faculty_leaves():
        """Retrieves faculty and HOD leave/sabbatical requests from database, auto-seeding if missing."""
        PragyanDatabase.initialize_database()
        if "faculty_leaves_db" not in st.session_state:
            st.session_state.faculty_leaves_db = [
                {"id": 1, "faculty_name": "Dr. Smitha Rao", "department": "Electronics & Communication (ECE)", "start_date": "2026-10-01", "end_date": "2026-10-15", "reason": "International IEEE VLSI Summit Keynote Sabbatical", "status": "Pending"},
                {"id": 2, "faculty_name": "Prof. Meena Hegde", "department": "Electronics & Communication (ECE)", "start_date": "2026-09-15", "end_date": "2026-09-16", "reason": "Medical Leave", "status": "Pending"},
                {"id": 3, "faculty_name": "Dr. Anand Kumar", "department": "Electronics & Communication (ECE)", "start_date": "2026-08-01", "end_date": "2026-08-03", "reason": "Personal Travel", "status": "Approved"},
                {"id": 4, "faculty_name": "Prof. Sneha Patil", "department": "Electronics & Communication (ECE)", "start_date": "2026-09-20", "end_date": "2026-09-25", "reason": "Sabbatical Research", "status": "Approved"}
            ]
        return st.session_state.faculty_leaves_db

    @staticmethod
    def update_faculty_leave_status(leave_id, new_status):
        """Updates the approval status of a faculty/HOD leave request in database."""
        PragyanDatabase.initialize_database()
        leaves = PragyanDatabase.get_faculty_leaves()
        for leave in leaves:
            if leave["id"] == leave_id:
                leave["status"] = new_status
                break

    # --- Student Marks Accessors & CRUD ---
    @staticmethod
    def get_student_marks():
        """Retrieves student internal assessment marks from database."""
        PragyanDatabase.initialize_database()
        if "student_marks_db" not in st.session_state:
            PragyanDatabase.initialize_database()
        return st.session_state.student_marks_db

    @staticmethod
    def save_student_mark(mark_record):
        """Adds or updates a student internal mark entry in database."""
        PragyanDatabase.initialize_database()
        marks = PragyanDatabase.get_student_marks()
        existing = next((m for m in marks if m["roll"] == mark_record["roll"] and m["subject"] == mark_record["subject"]), None)
        if existing:
            existing["internal_1"] = mark_record["internal_1"]
            existing["internal_2"] = mark_record["internal_2"]
            existing["internal_3"] = mark_record["internal_3"]
            existing["best_avg"] = mark_record["best_avg"]
            existing["status"] = mark_record["status"]
        else:
            marks.insert(0, mark_record)

    # --- Principal Profile Database Accessors & Persistence ---
    @staticmethod
    def get_principal_profile():
        """Retrieves the principal's executive profile from session state, seeding defaults if empty."""
        PragyanDatabase.initialize_database()
        return st.session_state.principal_executive_profile_db

    @staticmethod
    def save_principal_profile(profile_data):
        """Saves and updates the principal's executive profile in session state database."""
        PragyanDatabase.initialize_database()
        st.session_state.principal_executive_profile_db = profile_data
        st.session_state["user_name"] = profile_data.get("full_name", "Dr. Principal Dean")

    # --- Institutional Calendar Accessor ---
    @staticmethod
    def get_holiday_calendar():
        """Retrieves the official institutional master calendar (holidays, exams, events, breaks) from database."""
        PragyanDatabase.initialize_database()
        if "holiday_calendar_db" not in st.session_state:
            PragyanDatabase.initialize_database()
        return st.session_state.holiday_calendar_db
