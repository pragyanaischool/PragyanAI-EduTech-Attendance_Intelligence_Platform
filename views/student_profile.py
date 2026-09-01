import streamlit as st
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_student_profile():
    """
    Renders the Student Profile & Database Management view, allowing students 
    to review academic credentials and administrators to add new student records.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    
    # Initialize Database State
    PragyanDatabase.initialize_database()
    
    st.markdown(f"## 🎒 Student Academic Passport & Database Hub — {user_name}")
    st.markdown(
        f"Manage your personal student profile, review academic credentials, "
        f"and register new student records into the institutional database."
    )
    
    st.info(
        "💡 **Academic Passport:** Data displayed here reflects real-time attendance thresholds "
        "and examination eligibility statuses."
    )

    st.markdown("---")

    # 2. Add New Student Record Form
    with st.form("add_student_database_form"):
        st.markdown("### 📋 Add New Student Record to Database")
        
        c1, c2 = st.columns(2)
        with c1:
            s_name = st.text_input("Student Full Name", value=user_name)
            s_roll = st.text_input("Roll Number / ID", value="ECE_2026_042")
            s_email = st.text_input("Email Address", value="sateesh.ambesange@pragyan.edu")
        with c2:
            s_dept = st.text_input("Department", value="Electronics & Communication (ECE)")
            s_term = st.selectbox("Semester / Term", ["Sem 3", "Sem 5", "Sem 7"])
            s_att = st.slider("Initial Attendance Percentage", min_value=0.0, max_value=100.0, value=84.7)

        st.markdown("---")
        
        if st.form_submit_button("💾 Insert Student Record into Database"):
            status_str = "🟢 Safe (>75% Cutoff)" if s_att >= 75 else "🔴 At-Risk (Shortage Warning)"
            new_student = {
                "roll": s_roll,
                "name": s_name,
                "department": s_dept,
                "semester": s_term,
                "email": s_email,
                "attendance_percentage": s_att,
                "exam_eligibility_status": status_str
            }
            PragyanDatabase.add_student(new_student)
            st.success(f"🎉 Student **{s_name}** ({s_roll}) successfully added to the institutional database!")

    st.markdown("---")

    # 3. Live Student Database Ledger
    st.markdown("### 🗄️ Active Student Database Ledger")
    st.markdown("Review all student profiles and attendance records currently persisted in the local database session.")
    st.dataframe(PragyanDatabase.get_students(), use_container_width=True)
