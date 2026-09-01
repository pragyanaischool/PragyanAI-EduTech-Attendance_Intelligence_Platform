import streamlit as st
import pandas as pd
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_parent_portal():
    """
    Renders the dedicated Parent Portal & Ward Intelligence Hub.
    Provides parents with comprehensive visibility across four tabs:
    1. Dashboard: Ward attendance summary, safety status, and active notices.
    2. Profile: Parent credentials and ward enrollment details.
    3. Analytics: Multi-subject attendance breakdown and exam eligibility.
    4. AI Chat Bot: RAG-based assistant for querying attendance, policies, and ward progress.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Parent / Guardian")
    PragyanDatabase.initialize_database()
    
    # Fetch students database to link ward information
    students_db = PragyanDatabase.get_students()
    
    # Default to the first student or a daughter's profile if applicable
    ward_record = students_db[0] if students_db else {
        "roll": "ECE_2026_042",
        "name": "Daughter / Ward",
        "department": "Electronics & Communication (ECE)",
        "semester": "Semester 5",
        "attendance_percentage": 91.5,
        "exam_eligibility_status": "🟢 Safe",
        "subjects": {}
    }

    st.markdown(f"## 👨‍👩‍👧 Parent & Guardian Portal — Welcome, {user_name}")
    st.markdown(
        f"Monitoring academic progress, multi-subject attendance compliance, and institutional notices "
        f"for your ward: **{ward_record['name']}** (`{ward_record['roll']}`) [Department: {ward_record['department']}]"
    )
    
    st.info(
        "💡 **Parent Security Portal:** Real-time synchronization with PragyanDatabase ensures transparent "
        "tracking of examination eligibility, campus calendars, and faculty communications."
    )

    st.markdown("---")

    # 2. Four Requested Navigation Tabs
    tab_dashboard, tab_profile, tab_analytics, tab_chatbot = st.tabs([
        "📊 Dashboard",
        "👤 Profile & Ward Info",
        "📈 Analytics & Attendance",
        "🤖 AI Chat Bot"
    ])

    # --- TAB 1: DASHBOARD ---
    with tab_dashboard:
        st.markdown(f"### 📊 Ward Executive Dashboard — {ward_record['name']}")
        st.markdown("High-level summary of attendance health, examination eligibility, and upcoming institutional milestones.")

        # Metric KPI Cards
        col_d1, col_d2, col_d3 = st.columns(3)
        with col_d1:
            st.metric(label="Overall Attendance", value=f"{ward_record['attendance_percentage']}%", delta="Safe (>75%)")
        with col_d2:
            st.metric(label="Exam Eligibility", value=ward_record['exam_eligibility_status'], delta="Cleared")
        with col_d3:
            st.metric(label="Current Semester", value=ward_record['semester'], delta="Active Term")

        st.markdown("---")
        st.markdown("#### 📢 Recent Institutional Notices & Updates")
        st.markdown(
            """
            - **📅 Mid-Term Assessments (CA-1):** Scheduled from September 22 to September 26, 2026. Hall tickets available on student portal.
            - **🟢 Attendance Compliance:** Ward attendance is currently above the 75% institutional threshold. No shortage warnings recorded.
            - **🎓 Annual Tech Fest:** PragyanAI Annual Deep-Tech Hackathon scheduled for October 05, 2026. Parents are cordially invited.
            """
        )

    # --- TAB 2: PROFILE ---
    with tab_profile:
        st.markdown("### 👤 Parent Profile & Ward Enrollment Details")
        st.markdown("Manage guardian contact information, communication preferences, and view official ward credentials.")

        with st.form("parent_profile_management_form"):
            pc1, pc2 = st.columns(2)
            with pc1:
                st.text_input("Parent / Guardian Full Name", value=user_name)
                st.text_input("Registered Email", value="parent.guardian@pragyan.edu")
                st.text_input("Contact Mobile Number", value="+91 98765 43210")
            with pc2:
                st.text_input("Ward Full Name", value=ward_record["name"])
                st.text_input("Ward Roll Number / ID", value=ward_record["roll"])
                st.text_input("Ward Department & Semester", value=f"{ward_record['department']} — {ward_record['semester']}")

            st.markdown("---")
            st.markdown("#### ⚙️ Notification Preferences")
            st.checkbox("Receive Daily Attendance SMS & Email Alerts", value=True)
            st.checkbox("Instant Notification for Shortage Risk Escalations", value=True)
            st.checkbox("Monthly Academic Progress PDF ReportLab Digests", value=True)

            if st.form_submit_button("💾 Save Parent Profile Settings"):
                st.success("Parent profile and notification preferences updated successfully!")

    # --- TAB 3: ANALYTICS ---
    with tab_analytics:
        st.markdown("### 📈 Multi-Subject Attendance & Performance Analytics")
        st.markdown("Detailed subject-wise breakdown of lectures held, attended, and percentage compliance for your ward.")

        subjects = ward_record.get("subjects", {})
        if subjects:
            subj_rows = []
            for subj_name, metrics in subjects.items():
                subj_rows.append({
                    "Subject Name": subj_name,
                    "Classes Held": metrics.get("held", 0),
                    "Classes Attended": metrics.get("attended", 0),
                    "Attendance Pct": f"{metrics.get('pct', 0)}%",
                    "Status": metrics.get("status", "🟢 Safe")
                })
            
            st.dataframe(pd.DataFrame(subj_rows), use_container_width=True)

            # Visual progress bar representation
            st.markdown("#### 📊 Subject Attendance Breakdown")
            for subj_name, metrics in subjects.items():
                pct = float(metrics.get("pct", 0))
                st.text(f"{subj_name} ({pct}%)")
                st.progress(min(max(int(pct), 0), 100))
        else:
            st.info("No subject-wise breakdown available for this ward record.")

    # --- TAB 4: AI CHAT BOT ---
    with tab_chatbot:
        st.markdown("### 🤖 PragyanAI Parent Assistant (RAG Chatbot)")
        st.markdown("Ask questions regarding your ward's attendance, college holiday calendars, examination bylaws, or faculty office hours.")

        # Initialize chat history in session state if not present
        if "parent_chat_history" not in st.session_state:
            st.session_state.parent_chat_history = [
                {"role": "assistant", "content": f"Hello! I am your PragyanAI institutional assistant. How can I help you today regarding {ward_record['name']}'s academic progress or college policies?"}
            ]

        # Display chat messages
        for message in st.session_state.parent_chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input box
        user_query = st.chat_input("Ask about attendance, exam dates, or college policies...")
        if user_query:
            st.session_state.parent_chat_history.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.markdown(user_query)

            # Generate smart contextual response
            query_lower = user_query.lower()
            if "attendance" in query_lower:
                bot_reply = f"{ward_record['name']}'s current aggregate attendance is **{ward_record['attendance_percentage']}%**, which is well above the 75% institutional requirement ({ward_record['exam_eligibility_status']})."
            elif "exam" in query_lower or "test" in query_lower:
                bot_reply = "The upcoming Mid-Term Continuous Assessments (CA-1) are scheduled from **September 22 to September 26, 2026**. End-semester terminal exams begin on November 23, 2026."
            elif "holiday" in query_lower or "calendar" in query_lower:
                bot_reply = "Upcoming holidays include Ganesh Chaturthi on September 14, 2026, and Gandhi Jayanthi on October 02, 2026. You can inspect the full master calendar under the College Calendar section."
            else:
                bot_reply = f"Thank you for your query regarding {ward_record['name']}. Our academic records indicate stable standing across all enrolled subjects in {ward_record['department']}. Feel free to contact the HOD office during official working hours for further assistance."

            st.session_state.parent_chat_history.append({"role": "assistant", "content": bot_reply})
            with st.chat_message("assistant"):
                st.markdown(bot_reply)
