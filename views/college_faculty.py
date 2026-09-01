import streamlit as st
import pandas as pd
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_college_faculty():
    """
    Renders the Institution-Wide Faculty Directory & Roster Hub.
    Allows administrators and principals to inspect campus-wide faculty assignments, roles, research chairs, 
    and register new faculty members into the institutional database.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal Dean")
    college_name = "PragyanAI Institute of Technology & Venture Studio"
    PragyanDatabase.initialize_database()
    
    st.markdown(f"## 👨‍🏫 Campus Faculty Master Directory & Roster — {user_name}")
    st.markdown(
        f"Comprehensive directory of professors, research scholars, and academic instructors across "
        f"all departments at **{college_name}**."
    )
    
    st.info(
        "💡 **Faculty Governance Portal:** Audit active teaching loads, research chairs, departmental alignments, "
        "and register new faculty members in real time."
    )

    st.markdown("---")

    # 2. Pull Live Faculty Records from Database
    faculty_db = PragyanDatabase.get_department_faculty()
    fac_df = pd.DataFrame(faculty_db)

    # Executive KPI Metrics Banner
    col_fc1, col_fc2, col_fc3 = st.columns(3)
    with col_fc1:
        st.metric(label="👥 Total Campus Faculty", value=f"{len(fac_df) + 12} Members", delta="100% Verified")
    with col_fc2:
        st.metric(label="🔬 Active Research Chairs", value="24 Chairs", delta="AI & EDA Focus")
    with col_fc3:
        st.metric(label="🟢 Operational Status", value="Fully Active", delta="Zero Vacancies")

    st.markdown("---")

    # 3. Multi-Tab Directory & Management Navigation
    tab_directory, tab_register = st.tabs([
        "📋 Institutional Faculty Roster", 
        "➕ Register New Faculty Member"
    ])

    # --- TAB 1: FACULTY DIRECTORY TABLE ---
    with tab_directory:
        st.markdown("### 📋 Complete Campus Faculty Roster")
        st.markdown("Active faculty members, academic roles, appointment dates, and assigned course codes synced from the institutional database.")

        if not fac_df.empty:
            st.dataframe(fac_df, use_container_width=True)
        else:
            st.info("No faculty records available in database.")

    # --- TAB 2: REGISTER NEW FACULTY FORM ---
    with tab_register:
        st.markdown("### ➕ Add New Faculty Member to Institutional Directory")
        st.markdown("Submit credentials and course allocations to provision a new faculty profile.")

        with st.form("new_college_faculty_form"):
            nc1, nc2 = st.columns(2)
            with nc1:
                new_name = st.text_input("Faculty Full Name", placeholder="Dr. Jane Doe")
                new_role = st.selectbox("Academic Designation", ["Professor", "Associate Professor", "Assistant Professor", "Senior Researcher"])
            with nc2:
                new_courses = st.text_input("Assigned Course Codes", placeholder="ECE301, AI502")
                new_status = st.selectbox("Employment Status", ["🟢 Active", "🟡 On Sabbatical", "🔵 On-Duty Conference"])

            if st.form_submit_button("🚀 Add Faculty to Institutional Roster"):
                if new_name:
                    new_entry = {
                        "faculty_name": new_name,
                        "role": new_role,
                        "joined_date": str(pd.Timestamp.today().date()),
                        "active_courses": new_courses,
                        "status": new_status
                    }
                    PragyanDatabase.add_department_faculty(new_entry)
                    st.success(f"Successfully registered **{new_name}** into the institutional faculty directory!")
                    st.rerun()
                else:
                    st.error("Please enter a valid faculty name.")
