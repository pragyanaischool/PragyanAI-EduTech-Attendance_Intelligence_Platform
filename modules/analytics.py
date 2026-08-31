import streamlit as st
import pandas as pd
import plotly.express as px

class AttendanceAnalytics:
    @staticmethod
    def render_hod_subject_sessions_dashboard():
        """Renders HOD Department Subject-wise Session and Turnout audit metrics."""
        st.markdown("### 📊 HOD Intelligence: Subject-wise Number of Sessions & Metrics")
        st.markdown("Detailed audit of total lectures conducted, session frequencies, and average turnout by subject.")

        df_sessions = pd.DataFrame({
            "Subject Name": ["Digital Electronics", "Signals & Systems", "VLSI Design", "Microprocessors", "Control Systems"],
            "Semester": [5, 5, 6, 6, 5],
            "Total Sessions Conducted": [42, 38, 45, 40, 36],
            "Average Attendance (%)": [89.2, 78.5, 91.0, 84.4, 81.2],
            "Faculty Assigned": ["Dr. ABC", "Prof. XYZ", "Dr. Smitha Rao", "Prof. John Doe", "Dr. Alan Turing"]
        })

        st.dataframe(df_sessions, use_container_width=True)

        fig = px.bar(
            df_sessions, 
            x="Subject Name", 
            y="Total Sessions Conducted", 
            color="Average Attendance (%)",
            color_continuous_scale="Blues",
            title="Total Sessions Conducted vs Subject Attendance Rate"
        )
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="#F3F4F6")
        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def render_student_trend_chart():
        """Renders student attendance progression chart over weeks."""
        df = pd.DataFrame({
            "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
            "Attendance (%)": [91, 88, 76, 84]
        })
        fig = px.line(df, x="Week", y="Attendance (%)", markers=True, 
                      title="Monthly Attendance Trajectory",
                      color_discrete_sequence=["#3B82F6"])
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="#F3F4F6")
        return fig
