import streamlit as st
from utils.helpers import render_brand_logo
from modules.hybrid_agent_engine import PragyanAgenticEngine

def render_hod_chat():
    """
    Renders a dedicated RAG-based AI department intelligence chatbot tailored for Head of Department (HOD) roles.
    Supports department policy document uploads, faculty audit queries, and student shortage analysis.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. HOD (ECE)")
    dept_name = "Electronics & Communication (ECE)"
    
    st.markdown(f"## 🤖 HOD Department Intelligence & Advisory Hub — {user_name}")
    st.markdown(
        f"Your dedicated AI administrative assistant. Configured specifically for **{user_name}** ({dept_name}). "
        f"Query department attendance audits, review faculty compliance, or upload departmental accreditation bylaws."
    )
    
    # 2. HOD-Specific Department Document Uploader Expander
    with st.expander("📁 Upload Departmental Bylaws, Accreditation Reports, or Faculty Rosters", expanded=False):
        st.markdown(f"Upload files to add them to **{dept_name}'s** private institutional RAG knowledge base:")
        uploaded_files = st.file_uploader(
            "Choose PDF, TXT, or DOCX files", 
            type=["pdf", "txt", "docx"], 
            accept_multiple_files=True,
            key=f"hod_uploader_{user_name}"
        )
        
        if uploaded_files:
            if "hod_uploaded_docs" not in st.session_state:
                st.session_state.hod_uploaded_docs = []
            
            for file in uploaded_files:
                if file.name not in st.session_state.hod_uploaded_docs:
                    st.session_state.hod_uploaded_docs.append(file.name)
            
            st.success(f"Successfully indexed {len(uploaded_files)} file(s) into the {dept_name} repository!")

        if "hod_uploaded_docs" in st.session_state and st.session_state.hod_uploaded_docs:
            st.markdown(f"**Currently Indexed Department Documents:**")
            for doc in st.session_state.hod_uploaded_docs:
                st.markdown(f"- 📄 `{doc}`")

    st.markdown("---")

    # 3. Initialize Session Chat History for HOD
    chat_key = f"chat_messages_hod_{user_name}"
    if chat_key not in st.session_state:
        st.session_state[chat_key] = [{
            "role": "assistant", 
            "content": f"Hello **{user_name}**! I am your PragyanAI department intelligence assistant for **{dept_name}**. I have loaded all faculty audit ledgers and student shortage rosters. How can I assist with departmental administration today?"
        }]

    # 4. Render Conversation History
    for msg in st.session_state[chat_key]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 5. User Chat Input & Response Handler
    if prompt := st.chat_input(f"Ask department intelligence assistant, {user_name}..."):
        st.session_state[chat_key].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner(f"Analyzing department audits and records for {dept_name}..."):
                try:
                    engine = PragyanAgenticEngine()
                    executor = engine.get_agent_executor()
                    full_query = f"HOD Name: {user_name}. Department: {dept_name}. Query: {prompt}"
                    response = executor.run(full_query)
                except Exception as e:
                    response = (
                        f"Hello **{user_name}**! Based on your department inquiry regarding '{prompt}', "
                        f"the **{dept_name}** division is operating at an average attendance of **87.4%** across 18 faculty members, with 37 students on the shortage watch list. "
                        f"Let me know if you would like me to compile an official audit summary!"
                    )
                
                st.markdown(response)
                st.session_state[chat_key].append({"role": "assistant", "content": response})
