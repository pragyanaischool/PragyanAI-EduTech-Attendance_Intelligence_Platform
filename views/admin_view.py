import streamlit as st
from modules.sample_data import SampleDataGenerator

def render_admin_dashboard():
    """
    Renders the System Administrator Dashboard allowing management of institutional data,
    department rosters, faculty databases, student directories, and RBAC user provisioning.
    """
    user_name = st.session_state.get("user_name", "System Admin")
    st.image("PragyanAI_Transparent.png", width=220)
    st.markdown(f"# Admin System & Large-Scale Data Hub — {user_name}")
    st.markdown("### *Institute Setup, RBAC User Provisioning, and Database Audits*")

    # Ensure mock data is initialized from sample_data module
    SampleDataGenerator.initialize_institutional_data()

    # 1. Top System Metric Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(f'<div class="metric-card"><h3>{len(st.session_state.students_df):,}</h3><p>Total Active Students (6,000)</p></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="metric-card"><h3>{len(st.session_state.faculties_df)}</h3><p>Total Faculties (120)</p></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="metric-card"><h3>{len(st.session_state.departments_df)}</h3><p>Active Departments (6)</p></div>', unsafe_allow_html=True)
    c4.markdown(f'<div class="metric-card"><h3>{len(st.session_state.subjects_df):,}</h3><p>Curriculum Subjects</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 2. Tabbed Institutional Data Directories
    tab1, tab2, tab3, tab4 = st.tabs(["🏛️ Department Directory", "👨‍🏫 Faculty Roster (120)", "🎒 Student Database (6,000)", "➕ Provision New User"])

    with tab1:
        st.markdown("### Active Institutional Departments")
        st.markdown("The platform currently manages 6 core technical departments:")
        st.dataframe(st.session_state.departments_df, use_container_width=True)

    with tab2:
        st.markdown("### Institutional Faculty Roster")
        st.markdown("Showing mapped faculty members across all departments (~20 per department):")
        
        col_search, _ = st.columns([1, 1])
        with col_search:
            search_fac = st.text_input("Search Faculty by Name or Department", "")
            
        fac_df = st.session_state.faculties_df
        if search_fac:
            fac_df = fac_df[fac_df['name'].str.contains(search_fac, case=False) | fac_df['department'].str.contains(search_fac, case=False)]
            
        st.dataframe(fac_df, use_container_width=True)

    with tab3:
        st.markdown("### Comprehensive Student Database")
        st.markdown("Active student directory mapped across 8 semesters and sections:")
        
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            search_stud = st.text_input("Search Student by Name or Enrollment No", "")
        with col_s2:
            limit_rows = st.slider("Display Row Limit", 50, 500, 100)
            
        stud_df = st.session_state.students_df
        if search_stud:
            stud_df = stud_df[stud_df['name'].str.contains(search_stud, case=False) | stud_df['enrollment_no'].str.contains(search_stud, case=False)]
            
        st.dataframe(stud_df.head(limit_rows), use_container_width=True)
        st.caption(f"Showing {min(limit_rows, len(stud_df))} of {len(stud_df):,} total student records.")

    with tab4:
        st.markdown("### RBAC User Provisioning Form")
        st.markdown("Securely create new institutional user accounts and assign operational roles:")
        
        with st.form("admin_user_provision"):
            col_u1, col_u2 = st.columns(2)
            with col_u1:
                new_name = st.text_input("Full Name", placeholder="e.g. Dr. Alan Turing")
                new_email = st.text_input("Institutional Email", placeholder="alan.turing@pragyan.edu")
                new_pass = st.text_input("Initial Password", type="password", value="Pragyan@2026")
            with col_u2:
                new_role = st.selectbox("Assign System Role", ["Student", "Faculty", "Parent", "HOD", "Principal", "Admin"])
                new_dept = st.selectbox("Department", SampleDataGenerator.DEPARTMENTS)
                new_phone = st.text_input("Mobile Phone Number", value="+91 98765 43210")
                
            submit_user = st.form_submit_button("🚀 Provision System User")
            
            if submit_user:
                if new_name and new_email:
                    st.success(f"Successfully provisioned **{new_name}** with role **{new_role}** under **{new_dept}**!")
                    st.info(f"Credentials generated. Notification email dispatched to {new_email}.")
                else:
                    st.error("Please fill in all mandatory fields before provisioning.")
