import streamlit as st
import json
import os

class PragyanDatabase:
    """
    Central database controller managing role-specific tables, JSON file loading from data/,
    fallback dummy data, and persistence for students, faculty subject allocations,
    HOD records, and QR code session ledgers.
    """
    
    @staticmethod
    def _load_json_file(file_path: str, default_data: list) -> list:
        """Helper to safely load a JSON sample data file or return default fallback data."""
        try:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    content = json.load(f)
                    # Extract specific table lists based on keys
                    if "students" in content:
                        return content["students"]
                    elif "faculty_members" in content:
                        return content["faculty_members"]
                    elif "hod_records" in content:
                        return content["hod_records"]
                    elif "guardian_profiles" in content:
                        return content["guardian_profiles"]
                    elif isinstance(content, list):
                        return content
        except Exception:
            pass
        return default_data

    @staticmethod
    def initialize_database():
        """Initializes all database tables in Streamlit session state from JSON files or fallbacks."""
        
        # 1. Students Table
        if "db_students" not in st.session_state:
            default_students = [
                {"roll": "ECE_2026_01", "name": "Aarav Sharma", "department": "Electronics & Communication", "semester": "Sem 5", "email": "aarav.sharma@pragyan.edu", "attendance_percentage": 92.0, "exam_eligibility_status": "🟢 Optimal (Safe)"},
                {"roll": "ECE_2026_02", "name": "Priya Patel", "department": "Electronics & Communication", "semester": "Sem 5", "email": "priya.patel@pragyan.edu", "attendance_percentage": 84.0, "exam_eligibility_status": "🟢 Good"},
                {"roll": "ECE_2026_042", "name": "Sateesh Ambesange", "department": "Electronics & Communication", "semester": "Sem 5", "email": "sateesh.ambesange@pragyan.edu", "attendance_percentage": 84.7, "exam_eligibility_status": "🟢 Safe (>75% Cutoff)"}
            ]
            st.session_state.db_students = PragyanDatabase._load_json_file("data/student_sample_data.json", default_students)

        # 2. Faculty Allocations Table
        if "db_faculty_allocations" not in st.session_state:
            default_faculty = [
                {"employee_id": "FAC_ECE_101", "faculty_name": "Dr. Smitha Rao", "department": "Electronics & Communication (ECE)", "subject": "ECE301 - Digital Logic Design", "semester": "Sem 5", "cabin_location": "Block B, Room 304", "availability_status": "🟢 Available in Cabin"},
                {"employee_id": "FAC_ECE_101", "faculty_name": "Dr. Smitha Rao", "department": "Electronics & Communication (ECE)", "subject": "ECE402 - VLSI Architecture", "semester": "Sem 7", "cabin_location": "Block B, Room 304", "availability_status": "🟢 Available in Cabin"},
                {"employee_id": "FAC_ECE_102", "faculty_name": "Prof. Anand Kumar", "department": "Electronics & Communication (ECE)", "subject": "ECE302 - Signals & Systems", "semester": "Sem 5", "cabin_location": "Block B, Room 210", "availability_status": "🔴 On Leave"},
                {"employee_id": "FAC_ECE_103", "faculty_name": "Dr. Rajeshwari", "department": "Electronics & Communication (ECE)", "subject": "ECE305 - Microcontrollers", "semester": "Sem 5", "cabin_location": "Block C, Room 115", "availability_status": "🟢 Available in Lab"}
            ]
            raw_faculty_json = PragyanDatabase._load_json_file("data/faculty_sample_data.json", [])
            # Flatten faculty objects with allocated subjects for easy table viewing
            flattened_allocations = []
            if raw_faculty_json and isinstance(raw_faculty_json, list):
                for fac in raw_faculty_json:
                    fac_name = fac.get("faculty_name", "Unknown Faculty")
                    emp_id = fac.get("employee_id", "FAC_00")
                    dept = fac.get("department", "ECE")
                    cabin = fac.get("cabin_location", "Block B")
                    status = fac.get("availability_status", "Available")
                    for subj in fac.get("allocated_subjects", []):
                        flattened_allocations.append({
                            "employee_id": emp_id,
                            "faculty_name": fac_name,
                            "department": dept,
                            "subject": f"{subj.get('subject_code')} - {subj.get('subject_name')}",
                            "semester": subj.get("semester", "Sem 5"),
                            "cabin_location": cabin,
                            "availability_status": status
                        })
            st.session_state.db_faculty_allocations = flattened_allocations if flattened_allocations else default_faculty

        # 3. HOD Records Table
        if "db_hod_records" not in st.session_state:
            default_hod = [
                {"employee_id": "HOD_ECE_2026_01", "hod_name": "Dr. HOD (ECE)", "department": "Electronics & Communication Engineering (ECE)", "deanery_office": "Block A, Room 102", "availability_status": "🟢 Available in Deanery"}
            ]
            st.session_state.db_hod_records = PragyanDatabase._load_json_file("data/hod_sample_data.json", default_hod)

        # 4. QR Session Database Ledger
        if "qr_session_database" not in st.session_state:
            st.session_state.qr_session_database = [
                {"date": "2026-09-01", "dept": "Electronics & Communication (ECE)", "semester": "Sem 5", "subject": "ECE301 - Digital Logic Design", "file_link": "qr_sessions/ece301_2026_09_01.png", "scans": 44},
                {"date": "2026-09-01", "dept": "Electronics & Communication (ECE)", "semester": "Sem 7", "subject": "ECE402 - VLSI Architecture", "file_link": "qr_sessions/ece402_2026_09_01.png", "scans": 46}
            ]

    @staticmethod
    def get_students():
        PragyanDatabase.initialize_database()
        return st.session_state.db_students

    @staticmethod
    def add_student(student_data: dict):
        PragyanDatabase.initialize_database()
        st.session_state.db_students.append(student_data)

    @staticmethod
    def get_faculty_allocations(faculty_name=None):
        PragyanDatabase.initialize_database()
        if faculty_name:
            return [f for f in st.session_state.db_faculty_allocations if faculty_name.lower() in f.get("faculty_name", "").lower()]
        return st.session_state.db_faculty_allocations

    @staticmethod
    def add_faculty_allocation(allocation_data: dict):
        PragyanDatabase.initialize_database()
        st.session_state.db_faculty_allocations.append(allocation_data)

    @staticmethod
    def get_hod_records():
        PragyanDatabase.initialize_database()
        return st.session_state.db_hod_records
