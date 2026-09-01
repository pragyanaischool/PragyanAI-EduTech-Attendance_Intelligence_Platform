import streamlit as st
import pandas as pd
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_faculty_marks():
    """
    Renders the Faculty Students Internal Assessment Marks Hub.
    Allows faculty to select a subject, view student mark sheets across Internal 1, 2, and 3,
    calculate the best-of-two average, and input/update student scores persistently in PragyanDatabase.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Smitha Rao")
    college_name = "PragyanAI Institute of Technology & Venture Studio"
    PragyanDatabase.initialize_database()
    
    st.markdown(f"## 📝 Faculty Internal Assessment Marks Portal — {user_name}")
    st.markdown(
        f"Manage student internal assessments (Internal 1, 2, 3), compute best-of-two averages, "
        f"and record grades across assigned courses at **{college_name}**."
    )
    
    st.info(
        "💡 **Academic Grading Portal:** Marks entered here update student performance ledgers and eligibility analytics in real time."
    )

    st.markdown("---")

    # 2. Fetch Data from Database
    marks_db = PragyanDatabase.get_student_marks()
    students_db = PragyanDatabase.get_students()
    allocations_db = PragyanDatabase.get_faculty_allocations()

    # Extract subjects taught by current faculty or fallback to default list
    faculty_subjects = [a["subject"] for a in allocations_db if a.get("faculty") == user_name]
    if not faculty_subjects:
        faculty_subjects = ["ECE501 - VLSI Architecture", "ECE301 - Digital Logic Design", "ECE502 - Microcontrollers"]

    # 3. Multi-Tab Navigation
    tab_view, tab_entry = st.tabs([
        "📋 Subject Mark Sheet & Best-of-Two",
        "➕ Enter / Update Student Marks"
    ])

    # --- TAB 1: VIEW MARK SHEET ---
    with tab_view:
        st.markdown("### 📋 Subject-Wise Internal Assessment Mark Sheet")
        
        selected_subject = st.selectbox("🎯 Select Subject to View Mark Sheet", faculty_subjects, key="marks_subj_view")
        
        filtered_marks = [m for m in marks_db if m["subject"] == selected_subject]
        
        st.markdown(f"#### 📊 Performance Summary for: `{selected_subject}`")

        if filtered_marks:
            df_marks = pd.DataFrame(filtered_marks)
            display_marks_df = df_marks[[
                "roll", "name", "internal_1", "internal_2", "internal_3", "best_avg", "status"
            ]].rename(columns={
                "roll": "Roll Number",
                "name": "Student Name",
                "internal_1": "Internal 1 (Max 25)",
                "internal_2": "Internal 2 (Max 25)",
                "internal_3": "Internal 3 (Max 25)",
                "best_avg": "Best of Two Avg",
                "status": "Academic Standing"
            })
            st.dataframe(display_marks_df, use_container_width=True)

            # Summary Metrics
            avg_score = round(df_marks["best_avg"].mean(), 2)
            max_score = df_marks["best_avg"].max()
            min_score = df_marks["best_avg"].min()

            mc1, mc2, mc3 = st.columns(3)
            with mc1:
                st.metric(label="Class Average (Best of Two)", value=f"{avg_score} / 25")
            with mc2:
                st.metric(label="Highest Score", value=f"{max_score} / 25")
            with mc3:
                st.metric(label="Lowest Score", value=f"{min_score} / 25")
        else:
            st.info(f"No internal marks recorded yet for **{selected_subject}**.")

    # --- TAB 2: ENTER / UPDATE MARKS FORM ---
    with tab_entry:
        st.markdown("### ➕ Input or Update Student Internal Scores")
        st.markdown("Select a student and subject, input marks for Internal 1, 2, and 3. The system will automatically compute the best-of-two average.")

        with st.form("faculty_marks_entry_form"):
            mc1, mc2 = st.columns(2)
            with mc1:
                entry_subject = st.selectbox("Select Subject for Grading", faculty_subjects, key="marks_subj_entry")
                student_options = {f"{s['name']} ({s['roll']})": s for s in students_db}
                selected_student_key = st.selectbox("Select Student", list(student_options.keys()))
                selected_student = student_options.get(selected_student_key, {})
            
            with mc2:
                i1 = st.number_input("Internal Assessment 1 (Max 25)", min_value=0.0, max_value=25.0, value=20.0, step=0.5)
                i2 = st.number_input("Internal Assessment 2 (Max 25)", min_value=0.0, max_value=25.0, value=21.0, step=0.5)
                i3 = st.number_input("Internal Assessment 3 (Max 25)", min_value=0.0, max_value=25.0, value=22.0, step=0.5)

            if st.form_submit_button("🚀 Calculate & Save Student Marks"):
                if selected_student:
                    # Calculate Best of Two Average
                    scores = sorted([i1, i2, i3], reverse=True)
                    best_two_avg = round((scores[0] + scores[1]) / 2.0, 2)

                    # Determine standing
                    if best_two_avg >= 21.0:
                        status = "🟢 Distinction"
                    elif best_two_avg >= 16.0:
                        status = "🟢 First Class"
                    elif best_two_avg >= 12.5:
                        status = "🟡 Pass / Average"
                    else:
                        status = "🔴 Remedial Required"

                    mark_record = {
                        "roll": selected_student.get("roll", "ECE_2026_001"),
                        "name": selected_student.get("name", "Student"),
                        "subject": entry_subject,
                        "internal_1": i1,
                        "internal_2": i2,
                        "internal_3": i3,
                        "best_avg": best_two_avg,
                        "status": status
                    }

                    PragyanDatabase.save_student_mark(mark_record)
                    st.success(f"Successfully recorded marks for **{selected_student.get('name')}** in `{entry_subject}`! Best of Two Average: **{best_two_avg} / 25** ({status}).")
                    st.rerun()
                else:
                    st.error("Please select a valid student.")
