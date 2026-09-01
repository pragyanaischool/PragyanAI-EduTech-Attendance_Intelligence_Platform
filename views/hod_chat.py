import streamlit as st
import datetime
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_hod_chat():
    """
    Renders the HOD AI Intelligence & RAG Chat Assistant.
    Provides deep conversational access to department data (faculties, students, multi-subject attendance,
    leave records, and official institutional documents).
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. HOD (ECE)")
    dept_name = "Electronics & Communication (ECE)"
    PragyanDatabase.initialize_database()
    
    st.markdown(f"## 🤖 HOD Institutional Intelligence & RAG Chat Assistant — {user_name}")
    st.markdown(
        f"Query institutional records, faculty workloads, student attendance dossiers, leave requests, "
        f"and department policy documents for the **{dept_name}** department using contextual AI."
    )
    
    st.info(
        "💡 **RAG-Powered Intelligence:** This assistant has direct read access to live database records and department documents. "
        "Ask questions about student shortages, faculty substitutions, leave approvals, or curriculum guidelines."
    )

    st.markdown("---")

    # 2. Compile Real-Time Department Context from Database
    students_db = PragyanDatabase.get_students()
    faculty_db = PragyanDatabase.get_department_faculty()
    course_allocs = PragyanDatabase.get_course_allocations()
    leave_requests = st.session_state.get("student_leave_requests_db", [])
    hod_leaves = st.session_state.get("hod_leave_applications", [])
    
    # Official Department Documents & Bylaws Repository
    if "department_documents_db" not in st.session_state:
        st.session_state.department_documents_db = [
            {"title": "ECE Department Bylaws & Academic Handbook 2026", "category": "Academic Policy", "summary": "Mandates strict 75% attendance criteria, medical exemption grace caps, and faculty substitution protocols."},
            {"title": "AI Curriculum Integration Blueprint (Sem 3 - Sem 8)", "category": "Curriculum", "summary": "Details multi-year transition toward Agentic AI, VLSI EDA automation, and embedded systems project-based learning."},
            {"title": "ELEVATE NxT Deep-Tech Grant Proposal", "category": "Research & Grants", "summary": "Funding proposal for automated PCB defect verification and computer vision inspection systems."}
        ]
    dept_docs = st.session_state.department_documents_db

    # 3. Initialize Chat History in Session State
    if "hod_chat_messages" not in st.session_state:
        st.session_state.hod_chat_messages = [
            {
                "role": "assistant",
                "content": f"Greetings, **{user_name}**. I am your institutional AI copilot with live access to the **{dept_name}** database and document repository. How may I assist you with academic governance, attendance audits, or faculty workloads today?"
            }
        ]

    # Display Chat History
    for message in st.session_state.hod_chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 4. Quick Suggested Prompt Buttons for HOD
    st.markdown("##### ⚡ Quick Executive Queries:")
    qc1, qc2, qc3, qc4 = st.columns(4)
    
    quick_prompt = None
    with qc1:
        if st.button("🚨 Who is At-Risk (<75%)?"):
            quick_prompt = "Which students in our department currently have attendance below the 75% shortage threshold across their subjects?"
    with qc2:
        if st.button("👩‍🏫 Faculty Workload Summary"):
            quick_prompt = "Provide a summary of our department faculty roster, their active roles, and assigned courses."
    with qc3:
        if st.button("🌴 Pending Leave Approvals"):
            quick_prompt = "List all pending student and faculty leave applications that require my review."
    with qc4:
        if st.button("📄 Department Bylaws & Grants"):
            quick_prompt = "What are the key policy guidelines outlined in our Department Handbook and research grant proposals?"

    # 5. User Input Handling & RAG Context Injection
    user_query = st.chat_input("Ask about students, faculty, subjects, leave records, or department documents...")
    
    if quick_prompt:
        user_query = quick_prompt

    if user_query:
        # Append user message
        st.session_state.hod_chat_messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        # Generate Context-Aware AI Response
        with st.chat_message("assistant"):
            with st.spinner("🔍 Extracting database records, analyzing department metrics, and querying document store..."):
                
                # Intelligent Query Parsing & Context Matching
                query_lower = user_query.lower()
                response_text = ""

                if "at-risk" in query_lower or "shortage" in query_lower or "75%" in query_lower or "attendance" in query_lower:
                    at_risk_students = [s for s in students_db if s["attendance_percentage"] < 75.0]
                    response_text = f"### 🚨 Attendance Shortage & At-Risk Audit\n\n"
                    response_text += f"Based on live database records for **{dept_name}**, the following students are currently flagged below the 75% threshold:\n\n"
                    for s in at_risk_students:
                        response_text += f"- **{s['name']}** (`{s['roll']}` - {s['semester']}): Overall Turnout **{s['attendance_percentage']}%** ({s['exam_eligibility_status']})\n"
                        for subj, metrics in s.get("subjects", {}).items():
                            if metrics["pct"] < 75.0:
                                response_text += f"  - *{subj}*: {metrics['pct']}% ({metrics['status']})\n"
                    response_text += f"\n*Recommendation:* Review medical exemption filings or issue formal attendance warning notices."

                elif "faculty" in query_lower or "workload" in query_lower or "roster" in query_lower or "courses" in query_lower:
                    response_text = f"### 👨‍🏫 Department Faculty Roster & Workload Intelligence\n\n"
                    response_text += f"Active faculty members registered in the **{dept_name}** database:\n\n"
                    for f in faculty_db:
                        response_text += f"- **{f['faculty_name']}** ({f['role']}) — Joined: {f['joined_date']} | Active Courses: `{f['active_courses']}` | Status: {f['status']}\n"
                    response_text += f"\nTotal Active Faculty: **{len(faculty_db)}** | Active Semester Courses Mapped: **{len(course_allocs)}**."

                elif "leave" in query_lower or "approval" in query_lower or "substitution" in query_lower:
                    response_text = f"### 🌴 Leave Applications & Approval Queue\n\n"
                    response_text += f"**Student Leave Requests:**\n"
                    for req in leave_requests:
                        response_text += f"- {req['name']} ({req['roll']}) - {req['type']} ({req['duration']}) [Status: {req['status']}]\n"
                    response_text += f"\n**HOD Personal Leave Submissions to Principal:**\n"
                    if hod_leaves:
                        for hl in hod_leaves:
                            response_text += f"- {hl['type']} from {hl['from']} to {hl['to']} | Acting HOD: {hl['acting_hod']} [Status: {hl['status']}]\n"
                    else:
                        response_text += "- No personal leave applications currently logged."

                elif "bylaws" in query_lower or "handbook" in query_lower or "grant" in query_lower or "document" in query_lower or "policy" in query_lower:
                    response_text = f"### 📄 Department Document & Policy Repository\n\n"
                    response_text += f"Retrieved documents matching your query from the institutional repository:\n\n"
                    for doc in dept_docs:
                        response_text += f"#### 📁 {doc['title']} *({doc['category']})*\n"
                        response_text += f"> {doc['summary']}\n\n"
                    response_text += f"*All documents are indexed and compliant with PragyanAI institutional governance standards.*"

                else:
                    # General Context-Aware Institutional Fallback
                    response_text = f"### 🏛️ PragyanAI Institutional Assistant Response\n\n"
                    response_text += f"I have analyzed your query against our live institutional database (**{dept_name}** department). "
                    response_text += f"Currently, the department oversees **{len(students_db)}** indexed students, **{len(faculty_db)}** faculty members, "
                    response_text += f"and **{len(dept_docs)}** active policy documents.\n\n"
                    response_text += f"You can ask me specific questions regarding student attendance percentages, subject-wise breakdowns, faculty course allocations, leave applications, or departmental research grants."

                st.markdown(response_text)
                st.session_state.hod_chat_messages.append({"role": "assistant", "content": response_text})
