import streamlit as st
import pandas as pd
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_college_calendar():
    """
    Renders the Institution-Wide Academic & Holiday Calendar Hub.
    Displays gazetted breaks, examination schedules, institutional events managed by the Principal Deanery,
    and an interactive year/month color-coded calendar explorer.
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

    # 2. Fetch Holiday Calendar & Master Events from Database
    holiday_data = PragyanDatabase.get_holiday_calendar()
    
    # Unified Master Events Store (Holidays, Exams, Events, Semester Breaks)
    master_events_store = [
        # January 2026
        {"date": "2026-01-26", "year": 2026, "month": "January", "title": "Republic Day", "category": "🔴 National Holiday", "badge_color": "#ef4444"},
        # March 2026
        {"date": "2026-03-04", "year": 2026, "month": "March", "title": "Holi Festival", "category": "🔵 Gazetted Holiday", "badge_color": "#3b82f6"},
        {"date": "2026-03-19", "year": 2026, "month": "March", "title": "Ugadi / Gudi Padwa", "category": "🟡 Restricted Holiday", "badge_color": "#f59e0b"},
        # April 2026
        {"date": "2026-04-03", "year": 2026, "month": "April", "title": "Good Friday", "category": "🔵 Gazetted Holiday", "badge_color": "#3b82f6"},
        # June 2026 (Semester Break)
        {"date": "2026-06-01 to 2026-06-15", "year": 2026, "month": "June", "title": "Summer Semester In-Between Break", "category": "🏖️ Semester Break", "badge_color": "#10b981"},
        # August 2026
        {"date": "2026-08-15", "year": 2026, "month": "August", "title": "Independence Day", "category": "🔴 National Holiday", "badge_color": "#ef4444"},
        {"date": "2026-08-21", "year": 2026, "month": "August", "title": "Varalakshmi Vratha", "category": "🟡 Restricted Holiday", "badge_color": "#f59e0b"},
        # September 2026
        {"date": "2026-09-14", "year": 2026, "month": "September", "title": "Ganesh Chaturthi", "category": "🔵 Gazetted Holiday", "badge_color": "#3b82f6"},
        {"date": "2026-09-22 to 2026-09-26", "year": 2026, "month": "September", "title": "Mid-Term Continuous Assessments (CA-1)", "category": "📝 Examination Window", "badge_color": "#6366f1"},
        # October 2026
        {"date": "2026-10-02", "year": 2026, "month": "October", "title": "Gandhi Jayanthi", "category": "🔴 National Holiday", "badge_color": "#ef4444"},
        {"date": "2026-10-05", "year": 2026, "month": "October", "title": "PragyanAI Annual Deep-Tech Hackathon", "category": "🎓 Institutional Event", "badge_color": "#8b5cf6"},
        {"date": "2026-10-12 to 2026-10-17", "year": 2026, "month": "October", "title": "Practical & Lab Viva Examinations", "category": "📝 Examination Window", "badge_color": "#6366f1"},
        {"date": "2026-10-18", "year": 2026, "month": "October", "title": "IEEE International Conference on VLSI & AI", "category": "🎓 Institutional Event", "badge_color": "#8b5cf6"},
        {"date": "2026-10-20", "year": 2026, "month": "October", "title": "Vijayadashami (Dasara)", "category": "🔵 Gazetted Holiday", "badge_color": "#3b82f6"},
        # November 2026
        {"date": "2026-11-08", "year": 2026, "month": "November", "title": "Deepavali Festival", "category": "🔵 Gazetted Holiday", "badge_color": "#3b82f6"},
        {"date": "2026-11-12", "year": 2026, "month": "November", "title": "Inter-Collegiate Cultural Fest 'Vanya 2026'", "category": "🎓 Institutional Event", "badge_color": "#8b5cf6"},
        {"date": "2026-11-23 to 2026-12-10", "year": 2026, "month": "November", "title": "End-Semester Terminal Examinations", "category": "📝 Examination Window", "badge_color": "#6366f1"},
        # December 2026
        {"date": "2026-12-11 to 2026-12-31", "year": 2026, "month": "December", "title": "Winter Semester Between Break", "category": "🏖️ Semester Break", "badge_color": "#10b981"},
        {"date": "2026-12-25", "year": 2026, "month": "December", "title": "Christmas Day", "category": "🔵 Gazetted Holiday", "badge_color": "#3b82f6"}
    ]

    # 3. Comprehensive Multi-Tab Master Calendar Navigation (Including Interactive View)
    tab_interactive, tab_holidays, tab_exams, tab_events = st.tabs([
        "🗓️ Interactive Month Calendar View",
        "🔴 Gazetted & National Holidays",
        "📝 Examination & Assessment Windows",
        "🎓 Institutional Events & Symposia"
    ])

    # --- TAB 1: INTERACTIVE MONTH CALENDAR VIEWER ---
    with tab_interactive:
        st.markdown("### 🗓️ Interactive Color-Coded Calendar Explorer")
        st.markdown("Select a year and month to inspect color-coded holidays, examinations, institutional events, and semester breaks.")

        col_sel1, col_sel2 = st.columns(2)
        with col_sel1:
            selected_year = st.selectbox("Select Year", [2026, 2027], key="cal_year_sel")
        with col_sel2:
            all_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            selected_month = st.selectbox("Select Month", all_months, index=8, key="cal_month_sel") # Default September 2026

        st.markdown("---")

        # Filter events for selected year and month
        filtered_events = [e for e in master_events_store if e["year"] == selected_year and e["month"] == selected_month]

        # Legend Guide
        st.markdown(
            """
            <div style="display: flex; gap: 15px; margin-bottom: 20px; font-size: 13px; flex-wrap: wrap;">
                <span style="background-color: rgba(239, 68, 68, 0.2); color: #f87171; padding: 4px 10px; border-radius: 6px; border: 1px solid #ef4444;">🔴 Holidays</span>
                <span style="background-color: rgba(99, 102, 241, 0.2); color: #818cf8; padding: 4px 10px; border-radius: 6px; border: 1px solid #6366f1;">📝 Examinations</span>
                <span style="background-color: rgba(139, 92, 246, 0.2); color: #a78bfa; padding: 4px 10px; border-radius: 6px; border: 1px solid #8b5cf6;">🎓 Events</span>
                <span style="background-color: rgba(16, 185, 129, 0.2); color: #34d399; padding: 4px 10px; border-radius: 6px; border: 1px solid #10b981;">🏖️ Semester Breaks</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(f"#### 📌 Schedule for `{selected_month} {selected_year}`")

        if filtered_events:
            for ev in filtered_events:
                st.markdown(
                    f"""
                    <div style="padding: 14px 18px; background-color: #1e293b; border-radius: 8px; border-left: 6px solid {ev['badge_color']}; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <h4 style="margin: 0; color: #f8fafc; font-size: 16px;">{ev['title']}</h4>
                            <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 13px;">📅 Date(s): <b>{ev['date']}</b></p>
                        </div>
                        <div>
                            <span style="background-color: {ev['badge_color']}; color: #ffffff; padding: 5px 12px; border-radius: 6px; font-size: 12px; font-weight: bold;">{ev['category']}</span>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.info(f"No scheduled holidays, exams, or events recorded for **{selected_month} {selected_year}**.")

    # --- TAB 2: HOLIDAYS ---
    with tab_holidays:
        st.markdown("### 🔴 Official Gazetted, National & Restricted Holidays (2026)")
        st.markdown("Synchronized directly with the central institutional database repository.")

        holiday_df = pd.DataFrame(holiday_data)
        if not holiday_df.empty:
            st.dataframe(holiday_df, use_container_width=True)
        else:
            st.info("No holiday records found in database.")

    # --- TAB 3: EXAMS ---
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

    # --- TAB 4: EVENTS ---
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
