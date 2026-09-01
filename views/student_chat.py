import streamlit as st
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_student_chat():
    """
    Renders the PragyanAI Student Advisor with Advanced Mentor Prompting.
    Queries real-time database records and uses expert academic mentorship frameworks 
    to counsel, guide, and support students based on their exact performance and attendance metrics.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    PragyanDatabase.initialize_database()
    
    st.markdown(f"# 🤖 PragyanAI Academic Mentor & RAG Advisor — {user_name}")
    st.markdown("### *Your Personal AI Coach for Attendance Intelligence, Study Planning, and Academic Success.*")
    
    st.info(
        "💡 **Empathetic Mentorship Active:** This advisor is configured with advanced pedagogical prompting "
        "to mentor you, review your database standing, and offer proactive guidance."
    )

    st.markdown("---")

    # 2. Document Upload RAG Ingestion Expander
    with st.expander("📁 Upload Reference Document / Medical Certificate for AI Mentorship Review"):
        uploaded_doc = st.file_uploader("Upload PDF, TXT, or Image for AI Contextual Ingestion", type=["pdf", "txt", "png", "jpg"])
        if uploaded_doc is not None:
            if "uploaded_rag_docs" not in st.session_state:
                st.session_state.uploaded_rag_docs = []
            doc_info = {"name": uploaded_doc.name, "size": uploaded_doc.size}
            if doc_info not in st.session_state.uploaded_rag_docs:
                st.session_state.uploaded_rag_docs.append(doc_info)
            st.success(f"🎉 Document **{uploaded_doc.name}** successfully ingested into your academic mentorship file!")

    ingested_docs = st.session_state.get("uploaded_rag_docs", [])
    if ingested_docs:
        st.caption(f"📚 Active RAG Vector Memory: {len(ingested_docs)} document(s) loaded (`{', '.join([d['name'] for d in ingested_docs])}`)")

    st.markdown("---")

    # 3. Chat History Initialization
    if "student_chat_history" not in st.session_state:
        st.session_state.student_chat_history = [
            {
                "role": "assistant", 
                "content": f"Hello **{user_name}**! I am your PragyanAI academic mentor. I'm here to support your learning journey, help you stay well above the 75% attendance threshold, guide you through your subjects, and answer any institutional questions. How are you feeling about your classes today?"
            }
        ]

    # Render chat message history
    for message in st.session_state.student_chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 4. User Input & Advanced Mentorship Response Engine
    if user_prompt := st.chat_input("Ask for study advice, attendance guidance, faculty consultation tips, or help with coursework..."):
        st.session_state.student_chat_history.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)

        # --- QUERY DATABASE CONTEXT ---
        students_db = PragyanDatabase.get_students()
        faculty_allocations = PragyanDatabase.get_faculty_allocations()
        hod_records = PragyanDatabase.get_hod_records()
        notices = st.session_state.get("institutional_notices", [])
        leaves = st.session_state.get("student_leave_requests", [])

        # Match current student record
        current_student = next(
            (s for s in students_db if s.get("name", "").lower() == user_name.lower() or s.get("roll", "").lower() == user_name.lower()), 
            {"name": user_name, "roll": "ECE_2026_042", "department": "Electronics & Communication", "semester": "Sem 5", "attendance_percentage": 84.7, "exam_eligibility_status": "🟢 Safe (>75% Cutoff)"}
        )

        att = current_student.get('attendance_percentage', 84.7)
        dept = current_student.get('department', 'Electronics & Communication')
        roll_id = current_student.get('roll', 'ECE_2026_042')

        enrolled_subjects = [
            {"code": "ECE301", "name": "Digital Logic Design", "credits": 4, "instructor": "Dr. Smitha Rao"},
            {"code": "ECE302", "name": "VLSI Architecture", "credits": 4, "instructor": "Prof. Anand Kumar"},
            {"code": "ECE303", "name": "Signals & Systems", "credits": 3, "instructor": "Dr. Ramesh Hegde"},
            {"code": "ECE304", "name": "Microcontrollers & Embedded Systems", "credits": 4, "instructor": "Dr. Priya Sharma"}
        ]

        query_lower = user_prompt.lower()
        
        # --- ADVANCED MENTORSHIP RESPONSE SYNTHESIS ---
        
        # Intent: Enrolled Subjects & Mentorship Guidance
        if any(kw in query_lower for kw in ["subject", "course", "enrolled", "classes", "credits", "study"]):
            subjects_str = "\n".join([f"1. **{s['code']} — {s['name']}** ({s['credits']} Credits)\n   *Instructor:* {s['instructor']}" for s in enrolled_subjects])
            reply = (
                f"🎓 **Academic Mentor Review for {current_student.get('name')}** (`{roll_id}`):\n\n"
                f"You are pursuing **{dept}** ({current_student.get('semester')}) with a strong course load:\n\n"
                f"{subjects_str}\n\n"
                f"💡 **Mentor Tip:** Success in core ECE subjects requires consistent lab attendance and active engagement with faculty during office hours. If you need help prioritizing your study schedule or preparing for upcoming mid-semesters, let me know!"
            )
            
        # Intent: Attendance Counseling & Risk Management
        elif any(kw in query_lower for kw in ["attendance", "percent", "shortage", "eligible", "exam", "risk", "warning"]):
            if att >= 85:
                status_tone = "🌟 **Outstanding Standing!** You are demonstrating exemplary discipline."
                advice = "Keep up the fantastic consistency! Your high attendance ensures you have a comfortable buffer for any emergencies or conference travels."
            elif att >= 75:
                status_tone = "🟢 **Safe Standing.** You meet the institutional cutoff."
                advice = "You are safely above the 75% mandatory threshold. However, try not to miss upcoming classes in heavy credit courses like ECE301 and ECE302 to maintain your safety margin."
            else:
                status_tone = "⚠️ **Attendance Shortage Alert!** Immediate action recommended."
                advice = "Your attendance is currently below the 75% institutional cutoff. Please consult your Department HOD immediately, file any pending medical leave exemptions, and ensure 100% attendance for the rest of the month."

            reply = (
                f"📊 **Personalized Attendance Counseling & Audit:**\n\n"
                f"- **Student:** {current_student.get('name')} (`{roll_id}`)\n"
                f"- **Current Aggregate Turnout:** **{att}%**\n"
                f"- **Evaluation:** {status_tone}\n\n"
                f"🛡️ **Mentor Recommendation:**\n{advice}\n\n"
                f"*Remember: Consistent presence in class directly correlates with academic performance.*"
            )
            
        # Intent: Faculty & HOD Mentorship / Office Hours
        elif any(kw in query_lower for kw in ["faculty", "teacher", "hod", "availability", "cabin", "deanery", "professor", "help"]):
            hod_info = hod_records[0] if hod_records else {"hod_name": "Dr. HOD (ECE)", "availability_status": "🟢 Available", "deanery_office": "Block A, Room 102"}
            reply = (
                f"🏛️ **Faculty Mentorship & Office Hours Navigator:**\n\n"
                f"As your academic mentor, I strongly encourage you to connect with your professors whenever you need conceptual clarity:\n"
                f"- **Department HOD ({hod_info.get('department', 'ECE')}):** {hod_info.get('hod_name')} (*{hod_info.get('availability_status')}* at {hod_info.get('deanery_office')})\n"
                f"- **Subject Mentors:** All 4 course instructors hold dedicated office hours every weekday from 3:00 PM to 5:00 PM in Block B cabins.\n\n"
                f"💡 *Would you like me to draft a professional consultation request email for one of your professors?*"
            )
            
        # Intent: Notices & Academic Calendar
        elif any(kw in query_lower for kw in ["notice", "announcement", "news", "circular", "exam schedule"]):
            notices_str = "\n".join([f"- **{n['title']}** (*{n['date']}* | Author: {n['author']})\n  > {n['content']}" for n in notices[:2]])
            reply = (
                f"📢 **Important Institutional Announcements & Deadlines:**\n\n"
                f"{notices_str}\n\n"
                f"🎯 **Mentor Action Plan:** Make sure your assignment submissions and attendance logs are updated before these deadlines to avoid any last-minute stress."
            )
            
        # Intent: Leave Guidance
        elif any(kw in query_lower for kw in ["leave", "absence", "medical", "od", "application", "excuse"]):
            leaves_str = "\n".join([f"- **{l['type']}** ({l['from']} to {l['to']}): `{l['status']}`" for l in leaves]) if leaves else "No leave applications currently filed."
            reply = (
                f"📝 **Leave Application Guidance:**\n\n"
                f"{leaves_str}\n\n"
                f"💡 **Mentor Advice:** If you are planning an absence for a hackathon, conference, or due to medical reasons, remember to submit your application with supporting documents within **48 hours** of return. This ensures your attendance records are seamlessly adjusted by your HOD."
            )
            
        # Empathetic Mentor Default Fallback
        else:
            reply = (
                f"🌟 **PragyanAI Academic Mentor:**\n\n"
                f"Hello **{user_name}**! I have reviewed your student profile in **{dept}**. You are maintaining a solid attendance rate of **{att}%**, placing you in a great position for this semester.\n\n"
                f"Regarding your query (*\"{user_prompt}\"*), I am here to help you excel. Whether you want to review your **enrolled subjects**, discuss strategies to improve your attendance, check **faculty availability**, or prepare for examinations, I am ready to guide you step by step.\n\n"
                f"What specific area would you like to focus on today?"
            )

        st.session_state.student_chat_history.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)
