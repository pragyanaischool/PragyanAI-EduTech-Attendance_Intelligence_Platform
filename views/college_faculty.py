import streamlit as st
import pandas as pd
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_college_faculty():
    """
    Renders the Institution-Wide Faculty Directory & Roster Hub.
    Allows administrators and principals to inspect campus-wide faculty assignments, degrees, designations,
    joining dates, total professional experience, and register new faculty members into the institutional database.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal Dean")
    college_name = "PragyanAI Institute of Technology & Venture Studio"
    PragyanDatabase.initialize_database()
    
    st.markdown(f"## 👨‍🏫 Campus Faculty Master Directory & Roster — {user_name}")
    st.markdown(
        f"Comprehensive directory of professors, research scholars, and academic instructors across "
        f"all departments at **{college_name}**, detailing joining tenure and professional experience metrics."
    )
    
    st.info(
        "💡 **Faculty Governance Portal:** Audit active teaching loads, research chairs, departmental alignments, "
        "joining dates, experience records, and register new faculty members in real time."
    )

    st.markdown("---")

    # 2. Pull Live Faculty Records from Database
    faculty_db = PragyanDatabase.get_department_faculty()
    fac_df = pd.DataFrame(faculty_db)

    # Executive KPI Metrics Banner
    col_fc1, col_fc2, col_fc3 = st.columns(3)
    with col_fc1:
        st.metric(label="👥 Total Campus Faculty", value=f"{len(fac_df)} Members", delta="100% Verified")
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
        st.markdown("### 📋 Complete Campus Faculty Roster & Experience Audit")
        st.markdown("Active faculty members, academic degrees, designations, joining dates, and total experience metrics synced from the institutional database.")

        if not fac_df.empty:
            # Format and prepare display columns including Joining Date and Experience metrics
            display_rows = []
            for _, row in fac_df.iterrows():
                total_exp = row.get("total_experience_years", 10)
                college_exp = row.get("college_experience_years", 4)
                exp_at_joining = max(0, total_exp - college_exp)
                
                display_rows.append({
                    "Department": row.get("department", "Electronics & Communication (ECE)"),
                    "Faculty Name": row.get("faculty_name", "Unknown"),
                    "Degree": row.get("degree", "Ph.D."),
                    "Designation": row.get("designation", "Assistant Professor"),
                    "Joining Date": row.get("joined_date", "2022-01-01"),
                    "Exp at Joining (Yrs)": f"{exp_at_joining} Yrs",
                    "Total Exp (Yrs)": f"{total_exp} Yrs",
                    "Active Courses": row.get("active_courses", "ECE301"),
                    "Status": row.get("status", "🟢 Active")
                })
            
            display_faculty_df = pd.DataFrame(display_rows)
            st.dataframe(display_faculty_df, use_container_width=True)
        else:
            st.info("No faculty records available in database.")

    # --- TAB 2: REGISTER NEW FACULTY FORM ---
    with tab_register:
        st.markdown("### ➕ Add New Faculty Member to Institutional Directory")
        st.markdown("Submit credentials, department affiliation, joining date, and experience metrics to provision a new faculty profile.")

        with st.form("new_college_faculty_form"):
            nc1, nc2 = st.columns(2)
            with nc1:
                new_name = st.text_input("Faculty Full Name", placeholder="Dr. Jane Doe")
                new_dept = st.selectbox("Department Affiliation", [
                    "Electronics & Communication (ECE)", 
                    "Artificial Intelligence & Data Science", 
                    "Computer Science & Engineering", 
                    "Electrical & Electronics Engineering"
                ])
                new_degree = st.text_input("Highest Degree & University", placeholder="Ph.D. in Computer Science (IIT Delhi)")
                new_designation = st.selectbox("Academic Designation", ["Professor", "Associate Professor", "Assistant Professor", "Senior Researcher"])
            with nc2:
                new_join_date = st.date_input("Joining Date in College", value=datetime.date(2023, 6, 1))
                new_total_exp = st.number_input("Total Professional Experience (Years)", min_value=0, max_value=40, value=8)
                new_courses = st.text_input("Assigned Course Codes", placeholder="ECE301, AI502")
                new_status = st.selectbox("Employment Status", ["🟢 Active", "🟡 On Sabbatical", "🔵 On-Duty Conference"])

            if st.form_submit_button("🚀 Add Faculty to Institutional Roster"):
                if new_name:
                    today_date = datetime.date.today()
                    college_exp_yrs = max(1, (today_date - new_join_date).days // 365)
                    
                    new_entry = {
                        "department": new_dept,
                        "faculty_name": new_name,
                        "degree": new_degree,
                        "designation": new_designation,
                        "joined_date": str(new_join_date),
                        "college_experience_years": college_exp_yrs,
                        "total_experience_years": int(new_total_exp),
                        "active_courses": new_courses,
                        "status": new_status
                    }
                    PragyanDatabase.add_department_faculty(new_entry)
                    st.success(f"Successfully registered **{new_name}** into the institutional faculty directory with joining date `{new_join_date}`!")
                    st.rerun()
                else:
                    st.error("Please enter a valid faculty name.")
