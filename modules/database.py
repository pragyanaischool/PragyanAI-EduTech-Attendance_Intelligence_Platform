import streamlit as st

class PragyanDatabase:
    """
    Core Database & Session State Management for PragyanAI Institutional Platform.
    Handles persistent storage for students with comprehensive multi-subject attendance tracking, 
    faculty portfolios, department rosters, semester course allocations, leave records, and adhoc duties.
    """

    @staticmethod
    def initialize_database():
        """Initializes default database tables in st.session_state if not already present."""
        if "db_initialized" in st.session_state and st.session_state.db_initialized:
            return

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

        # 4. Department Faculty Roster (Joined Date, Role, Active Courses)
        if "department_faculty_db" not in st.session_state:
            st.session_state.department_faculty_db = [
                {"faculty_name": "Dr. Smitha Rao", "role": "Professor & Senior Researcher", "joined_date": "2018-06-15", "active_courses": "ECE301, ECE302", "status": "🟢 Active"},
                {"faculty_name": "Dr. Anand Kumar", "role": "Associate Professor", "joined_date": "2020-07-01", "active_courses": "ECE303, ECE401", "status": "🟢 Active"},
                {"faculty_name": "Prof. Meena Hegde", "role": "Assistant Professor", "joined_date": "2021-08-10", "active_courses": "ECE304, ECE305", "status": "🟢 Active"},
                {"faculty_name": "Dr. Rajesh Sharma", "role": "Senior Lecturer", "joined_date": "2022-01-15", "active_courses": "ECE201, ECE202", "status": "🟢 Active"},
                {"faculty_name": "Prof. Sneha Patil", "role": "Assistant Professor", "joined_date": "2023-07-20", "active_courses": "ECE203, ECE306", "status": "🟡 On Sabbatical"}
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

    @staticmethod
    def get_holiday_calendar():
        """Retrieves the official institutional holiday calendar from database, seeding defaults if empty."""
        PragyanDatabase.initialize_database()
        if "holiday_calendar_db" not in st.session_state:
            st.session_state.holiday_calendar_db = [
                {"Year": "2026", "Month": "January", "Holiday Name": "Republic Day", "Date": "2026-01-26", "Type": "🔴 National Holiday"},
                {"Year": "2026", "Month": "March", "Holiday Name": "Holi", "Date": "2026-03-04", "Type": "🔵 Gazetted Holiday"},
                {"Year": "2026", "Month": "March", "Holiday Name": "Ugadi / Gudi Padwa", "Date": "2026-03-19", "Type": "🟡 Restricted Holiday"},
                {"Year": "2026", "Month": "April", "Holiday Name": "Good Friday", "Date": "2026-04-03", "Type": "🔵 Gazetted Holiday"},
                {"Year": "2026", "Month": "August", "Holiday Name": "Independence Day", "Date": "2026-08-15", "Type": "🔴 National Holiday"},
                {"Year": "2026", "Month": "August", "Holiday Name": "Varalakshmi Vratha", "Date": "2026-08-21", "Type": "🟡 Restricted Holiday"},
                {"Year": "2026", "Month": "September", "Holiday Name": "Ganesh Chaturthi", "Date": "2026-09-14", "Type": "🔵 Gazetted Holiday"},
                {"Year": "2026", "Month": "October", "Holiday Name": "Gandhi Jayanthi", "Date": "2026-10-02", "Type": "🔴 National Holiday"},
                {"Year": "2026", "Month": "October", "Holiday Name": "Vijayadashami (Dasara)", "Date": "2026-10-20", "Type": "🔵 Gazetted Holiday"},
                {"Year": "2026", "Month": "November", "Holiday Name": "Deepavali", "Date": "2026-11-08", "Type": "🔵 Gazetted Holiday"},
                {"Year": "2026", "Month": "December", "Holiday Name": "Christmas Day", "Date": "2026-12-25", "Type": "🔵 Gazetted Holiday"}
            ]
        return st.session_state.holiday_calendar_db
