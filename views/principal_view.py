import streamlit as st
import pandas as pd
import plotly.express as px
from modules.sample_data import SampleDataGenerator

def render_principal_dashboard():
    """
    Renders the Principal Institute-Wide Analytics Hub with cross-department comparisons,
    semester-wise performance trends, and institute-level shortage audits.
    """
    st.image("PragyanAI_Transparent.png", width=220)
    user_name = st.session_state.get("user_name", "Dr. Principal")
    
    st.markdown("# 🏢 Principal Institute-Wide Analytics Hub")
    st.markdown(f"### *Welcome, {user_name} | Cross-Department Comparisons & Institutional Oversight*")

    # Ensure mock data is initialized from sample_data module
    SampleDataGenerator.initialize_institutional_data()
    df_stud = st.session_state.students_df

    # Compute institute-wide aggregate metrics
    total_students = len(df_stud)
    avg_inst_att = round(df_stud["overall_attendance"].mean(), 1)
    shortage_count = len(df_stud[df_stud["overall_attendance"] < 75.0])
    critical_count = len(df_stud[df_stud["overall_attendance"] < 65.0])

    # 1. Top Institute Metric Summary Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(f'<div class="metric-card"><h3>{total_students:,}</h3><p>Total Active Students</p></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="metric-card"><h3>{avg_inst_att}%</h3><p>Institute Average Turnout</p></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="metric-card" style="border-color:#EF4444;"><h3>{shortage_count}</h3><p>Shortage Students (<75%)</p></div>', unsafe_allow_html=True)
    c4.markdown(f'<div class="metric-card" style="border-color:#DC2626;"><h3>{critical_count}</h3><p>Critical Absentees (<65%)</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 2. Department-Wise Aggregation & Table
    st.markdown("### 🏛️ Department-Wise Comparison & Ranking")
    
    dept_summary = df_stud.groupby("department").agg(
        Total_Students=("student_id", "count"),
        Average_Attendance=("overall_attendance", "mean")
    ).reset_index()
    dept_summary["Average_Attendance"] = dept_summary["Average_Attendance"].round(1)
    dept_summary = dept_summary.sort_values(by="Average_Attendance", ascending=False).reset_index(drop=True)

    st.dataframe(dept_summary, use_container_width=True)

    st.markdown("---")

    # 3. Interactive Plotly Bar Chart for Department Performance
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("### 📊 Department Ranking Visualization")
        fig_dept = px.bar(
            dept_summary, 
            x="department", 
            y="Average_Attendance", 
            color="Average_Attendance", 
            color_continuous_scale="Viridis", 
            title="Average Attendance % Across 6 Institutes"
        )
        fig_dept.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="#F3F4F6")
        st.plotly_chart(fig_dept, use_container_width=True)

    with col_chart2:
        st.markdown("### 📈 Semester Attendance Distribution")
        sem_summary = df_stud.groupby("semester").agg(
            Average_Attendance=("overall_attendance", "mean")
        ).reset_index()
        sem_summary["Average_Attendance"] = sem_summary["Average_Attendance"].round(1)
        
        fig_sem = px.line(
            sem_summary, 
            x="semester", 
            y="Average_Attendance", 
            markers=True,
            title="Attendance Trajectory by Semester (1 to 8)",
            color_discrete_sequence=["#3B82F6"]
        )
        fig_sem.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="#F3F4F6")
        st.plotly_chart(fig_sem, use_container_width=True)

    st.markdown("---")

    # 4. Institute-Wide Advanced Filters & Audit
    st.markdown("### 🔍 Advanced Institutional Filter & Audit Panel")
    
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        filter_dept = st.selectbox("Filter by Department", ["All Departments"] + list(SampleDataGenerator.DEPARTMENTS))
    with col_f2:
        filter_sem = st.selectbox("Filter by Semester", ["All Semesters", 1, 2, 3, 4, 5, 6, 7, 8])
    with col_f3:
        filter_risk = st.selectbox("Filter by Risk Category", ["All Students", "Shortage (<75%)", "Critical Risk (<65%)"])

    # Apply filters dynamically on mock data dataframe
    filtered_df = df_stud.copy()
    if filter_dept != "All Departments":
        filtered_df = filtered_df[filtered_df["department"] == filter_dept]
    if filter_sem != "All Semesters":
        filtered_df = filtered_df[filtered_df["semester"] == filter_sem]
    if filter_risk == "Shortage (<75%)":
        filtered_df = filtered_df[filtered_df["overall_attendance"] < 75.0]
    elif filter_risk == "Critical Risk (<65%)":
        filtered_df = filtered_df[filtered_df["overall_attendance"] < 65.0]

    st.markdown(f"**Showing {len(filtered_df):,} matching student records:**")
    st.dataframe(filtered_df.head(50), use_container_width=True)
    st.caption("Displaying top 50 filtered records for high performance rendering. Export full institutional audit reports via the **PDF Reports Center** tab.")
