import streamlit as st
import pandas as pd
import random

class SampleDataGenerator:
    DEPARTMENTS = [
        "Computer Science & Engineering (CSE)",
        "Electronics & Communication (ECE)",
        "Mechanical Engineering (MECH)",
        "Civil Engineering (CIVIL)",
        "Electrical & Electronics (EEE)",
        "Information Technology (IT)"
    ]

    SUBJECT_POOL = {
        "Computer Science & Engineering (CSE)": ["Data Structures", "Algorithms", "Operating Systems", "Database Management", "Artificial Intelligence", "Computer Networks", "Software Engineering", "Cyber Security"],
        "Electronics & Communication (ECE)": ["Digital Electronics", "Signals & Systems", "VLSI Design", "Microprocessors", "Control Systems", "Analog Circuits", "Electromagnetics", "Communication Engineering"],
        "Mechanical Engineering (MECH)": ["Thermodynamics", "Fluid Mechanics", "Machine Design", "Kinematics", "Heat Transfer", "Manufacturing Processes", "Robotics", "Automobile Engineering"],
        "Civil Engineering (CIVIL)": ["Structural Analysis", "Geotechnical Engineering", "Surveying", "Concrete Technology", "Transportation Engineering", "Hydraulics", "Environmental Engg", "Estimation"],
        "Electrical & Electronics (EEE)": ["Circuit Theory", "Electrical Machines", "Power Systems", "Control Systems", "Power Electronics", "Electromagnetic Fields", "Measurements", "Renewable Energy"],
        "Information Technology (IT)": ["Web Technologies", "Object Oriented Programming", "Cloud Computing", "Data Warehousing", "Information Security", "Mobile App Development", "UI/UX Design", "DevOps"]
    }

    @staticmethod
    def initialize_institutional_data():
        """Generates large-scale dataset matching: 6 Depts, 120 Faculty, 8 Semesters, 6,000 Students."""
        if "data_initialized" in st.session_state and st.session_state.data_initialized:
            return

        departments = SampleDataGenerator.DEPARTMENTS

        faculties = []
        faculty_id_counter = 1
        for dept in departments:
            for i in range(1, 21):
                faculties.append({
                    "faculty_id": faculty_id_counter,
                    "name": f"Dr./Prof. Faculty {faculty_id_counter} ({dept.split()[0]})",
                    "department": dept,
                    "email": f"faculty.{faculty_id_counter}@pragyan.edu"
                })
                faculty_id_counter += 1

        subjects = []
        subject_id_counter = 1
        for fac in faculties:
            dept_pool = SampleDataGenerator.SUBJECT_POOL[fac["department"]]
            assigned_subs = random.sample(dept_pool, k=min(4, len(dept_pool)))
            for sem in range(1, 9):
                for sub_name in assigned_subs:
                    subjects.append({
                        "subject_id": subject_id_counter,
                        "subject_code": f"{fac['department'][:3].upper()}{100 + subject_id_counter}",
                        "subject_name": f"{sub_name} (Sem {sem})",
                        "semester": sem,
                        "department": fac["department"],
                        "assigned_faculty": fac["name"]
                    })
                    subject_id_counter += 1

        students = []
        student_id_counter = 1
        for dept in departments:
            dept_code = dept[:3].upper()
            for s_idx in range(1, 1001):
                sem = random.randint(1, 8)
                section = random.choice(["A", "B", "C", "D"])
                students.append({
                    "student_id": student_id_counter,
                    "name": f"Student {student_id_counter} ({dept_code})",
                    "enrollment_no": f"PRG2026{dept_code}{s_idx:04d}",
                    "department": dept,
                    "semester": sem,
                    "section": section,
                    "overall_attendance": round(random.uniform(60.0, 98.5), 1),
                    "parent_email": f"parent.s{student_id_counter}@domain.com"
                })
                student_id_counter += 1

        st.session_state.departments_df = pd.DataFrame(departments, columns=["Department Name"])
        st.session_state.faculties_df = pd.DataFrame(faculties)
        st.session_state.subjects_df = pd.DataFrame(subjects)
        st.session_state.students_df = pd.DataFrame(students)
        st.session_state.data_initialized = True
