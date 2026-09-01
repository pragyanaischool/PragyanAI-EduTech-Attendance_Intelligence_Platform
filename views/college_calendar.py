import streamlit as st
import pandas as pd
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_college_calendar():
    """
    Renders the Institution-Wide Academic & Holiday Calendar Hub.
    Displays gazetted breaks, examination schedules, and institutional events managed by the Principal Deanery.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal Dean")
    college_name = "PragyanAI Institute of Technology & Venture Studio"
    PragyanDatabase.initialize_database()
    
    st.markdown(f"## 📅 Campus Academic & Holiday Master Calendar — {user_name}")
    st.markdown(
        f"Master schedule of gazetted holidays, institutional breaks, examination windows, "
        f"and academic milestones across all departments at **{college_name}**."
    )
    
    st.info(
        "💡 **Institutional Scheduling:** Calendar entries scheduled here automatically synchronize with department timetables, "
        "faculty leave calendars, and student attendance ledger calculations."
    )

    st.markdown("---")

    # 2. Fetch Holiday Calendar from Database
    holiday_data = PragyanDatabase.get_holiday_calendar()
    holiday_df = pd.DataFrame(holiday_data)

    # 3. Comprehensive Multi-Tab Master Calendar Navigation
    tab_holidays, tab_exams, tab_events = st.tabs([
        "🔴 Gazetted & National Holidays",
        "📝 Examination & Assessment Windows",
        "🎓 Institutional Events & Symposia"
    ])

    # --- TAB 1: HOLIDAYS ---
    with tab_holidays:
        st.markdown("### 🔴 Official Gazetted, National & Restricted Holidays (2026)")
        st.markdown("Synchronized directly with the central institutional database repository.")

        if not holiday_df.empty:
            st.dataframe(holiday_df, use_container_width=True)
        else:
            st.info("No holiday records found in database.")

    # --- TAB 2: EXAMS ---
    with tab_exams:
        st.markdown("### 📝 Semester Examination & Mid-Term Assessment Schedule")
        st.markdown("Mandatory evaluation windows managed by the Controller of Examinations and Principal Deanery.")

        exam_schedule = [
            {"Term": "Semester 3, 5, 7", "Event": "Mid-Term Continuous Assessments (CA-1)", "Dates": "Sep 22, 2026 - Sep 26, 2026", "Status": "🔒 Locked"},
            {"Term": "Semester 3, 5, 7", "Event": "Practical & Lab Viva Examinations", "Dates": "Oct 12, 2026 - Oct 17, 2026", "Status": "⏳ Scheduled"},
            {"Term": "Semester 3, 5, 7", "Event": "End-Semester Terminal Examinations", "Dates": "Nov 23, 2026 - Dec 10, 2026", "Status": "⏳ Scheduled"},
            {"Term": "All Semesters", "Event": "Makeup & Exemption Examination Board", "Dates": "Dec 15, 2026 - Dec 18, 2026", "Status": "⏳ Scheduled"}
        ]
        
        exam_df = pd.DataFrame(exam_schedule)
        st.dataframe(exam_df, use_container_width=True)

    # --- TAB 3: EVENTS ---
    with tab_events:
        st.markdown("### 🎓 Campus Symposia, Research Colloquia & Cultural Fests")
        st.markdown("Official campus-wide academic events, deep-tech hackathons, and research conferences.")

        events_schedule = [
            {"Event Title": "PragyanAI Annual Deep-Tech Hackathon 2026", "Category": "Innovation & AI", "Date": "Oct 05, 2026", "Venue": "Main Auditorium"},
            {"Event Title": "IEEE International Conference on VLSI & AI", "Category": "Research Colloquium", "Date": "Oct 18, 2026", "Venue": "Convention Center Wing A"},
            {"Event Title": "Annual Inter-Collegiate Cultural Fest 'Vanya 2026'", "Category": "Cultural & Arts", "Date": "Nov 12, 2026", "Venue": "Open Air Amphitheatre"},
            {"Event Title": "ELEVATE NxT Deep-Tech Startup Showcase", "Category": "Venture Studio", "Date": "Dec 02, 2026", "Venue": "Incubation Center Boardroom"}
        ]

        events_df = pd.DataFrame(events_schedule)
        st.dataframe(events_df, use_container_width=True)
