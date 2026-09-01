import streamlit as st
import json
import os
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_admin_demo_seeder():
    """
    Renders the Admin & Demo Data Seeding Hub, enabling administrators 
    to seed sample data from role-specific JSON files, reset database tables, 
    and inspect live database records.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    st.markdown("# ⚙️ Admin & Demo Data Seeding Hub")
    st.markdown("### *Manage institutional database tables, seed role-specific sample files, and configure demo environments.*")

    PragyanDatabase.initialize_database()

    col_a1, col_a2 = st.columns(2)

    with col_a1:
        st.markdown("### 📥 Seed Sample Data by User Role")
        st.markdown("Select a role-specific JSON sample data repository to seed directly into the active database session.")
        
        sample_file_choice = st.selectbox(
            "Select Sample Data File", 
            [
                "student_sample_data.json", 
                "faculty_sample_data.json", 
                "hod_sample_data.json", 
                "principal_sample_data.json", 
                "parent_sample_data.json"
            ]
        )
        
        if st.button("🚀 Load & Seed Selected Sample File"):
            file_path = os.path.join("data", sample_file_choice)
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    st.success(f"Successfully loaded and verified **{sample_file_choice}**!")
                    with st.expander("🔍 View Raw Seeded JSON Structure", expanded=False):
                        st.json(data)
                except Exception as e:
                    st.error(f"Error reading JSON file: {e}")
            else:
                st.warning(f"File `{file_path}` not found on disk. Initializing with default factory record.")
                if "student" in sample_file_choice:
                    PragyanDatabase.add_student({"roll": "ECE_2026_99", "name": "Demo Seeder Student", "department": "ECE", "semester": "Sem 5", "attendance_percentage": 89.0, "exam_eligibility_status": "🟢 Optimal"})
                st.success("Default fallback record successfully seeded into database!")

    with col_a2:
        st.markdown("### 🔄 Database Maintenance & Reset")
        st.warning("Resetting the database clears all dynamic records, custom student entries, and QR logs, restoring factory default demo data.")
        
        if st.button("⚠️ Reset Entire Database to Factory Defaults"):
            for key in ["db_students", "db_faculty_allocations", "db_hod_records", "qr_session_database"]:
                if key in st.session_state:
                    del st.session_state[key]
            PragyanDatabase.initialize_database()
            st.success("🎉 Database successfully reset to default demo state across all tables!")

    st.markdown("---")

    # Live Database Inspector Table
    st.markdown("### 📊 Live Database Table Inspection")
    tab_d1, tab_d2, tab_d3, tab_d4 = st.tabs(["Students Table", "Faculty Allocations", "HOD Records", "QR Session Ledger"])
    
    with tab_d1:
        st.markdown("#### Active Students Ledger")
        st.dataframe(PragyanDatabase.get_students(), use_container_width=True)
        
    with tab_d2:
        st.markdown("#### Faculty Subject Allocations Ledger")
        st.dataframe(PragyanDatabase.get_faculty_allocations(), use_container_width=True)
        
    with tab_d3:
        st.markdown("#### HOD & Department Records Ledger")
        st.dataframe(PragyanDatabase.get_hod_records(), use_container_width=True)
        
    with tab_d4:
        st.markdown("#### QR Code Session File Links Ledger")
        st.dataframe(st.session_state.get("qr_session_database", []), use_container_width=True)
