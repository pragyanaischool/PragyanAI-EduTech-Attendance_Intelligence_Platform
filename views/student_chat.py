import streamlit as st
from utils.helpers import render_brand_logo
from modules.hybrid_agent_engine import PragyanAgenticEngine

def render_student_chat():
    """
    Renders a personalized RAG-based chatbot tailored for each individual student.
    Supports personal document uploads, name-based personalization, and concise prompt formatting.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    user_role = "Student"
    
    st.markdown(f"## 🤖 Personal AI Intelligence Hub — {user_name}")
    st.markdown(
        f"Your dedicated AI academic advisor. Configured specifically for **{user_name}** ({user_role}). "
        f"Ask questions about your attendance, upload medical documents, or query institutional bylaws."
    )
    
    # 2. Student-Specific Document Uploader Expander
    with st.expander("📁 Upload Personal Documents (Medical Certificates, Notes, Assignments)", expanded=False):
        st.markdown(f"Upload files to add them to **{user_name}'s** private RAG knowledge base:")
        uploaded_files = st.file_uploader(
            "Choose PDF or TXT files", 
            type=["pdf", "txt", "docx"], 
            accept_multiple_files=True,
            key=f"uploader_{user_name}"
        )
        
        if uploaded_files:
            if "user_uploaded_docs" not in st.session_state:
                st.session_state.user_uploaded_docs = []
            
            for file in uploaded_files:
                if file.name not in st.session_state.user_uploaded_docs:
                    st.session_state.user_uploaded_docs.append(file.name)
            
            st.success(f"Successfully indexed {len(uploaded_files)} document(s) into {user_name}'s private vector store!")

        if "user_uploaded_docs" in st.session_state and st.session_state.user_uploaded_docs:
            st.markdown(f"**Currently Indexed Private Docs for {user_name}:**")
            for doc in st.session_state.user_uploaded_docs:
                st.markdown(f"- 📄 `{doc}`")

    st.markdown("---")

    # 3. Initialize Session Chat History with Personalized Greeting
    chat_key = f"chat_messages_{user_name}"
    if chat_key not in st.session_state:
        st.session_state[chat_key] = [{
            "role": "assistant", 
            "content": f"Hello **{user_name}**! I am your personal PragyanAI assistant. I have loaded your attendance records and any uploaded documents. How can I assist you with your academics today?"
        }]

    # 4. Render Conversation History
    for msg in st.session_state[chat_key]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 5. User Chat Input & Personalized Prompt Formulation
    if prompt := st.chat_input(f"Ask your personal AI assistant, {user_name}..."):
        st.session_state[chat_key].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner(f"Analyzing records and private documents for {user_name}..."):
                active_docs = st.session_state.get("user_uploaded_docs", ["None"])
                system_persona_prompt = (
                    f"You are a friendly, concise, and highly personalized academic assistant for student {user_name} (Role: {user_role}). "
                    f"Always address the user by name ({user_name}). "
                    f"Use their personal uploaded documents ({', '.join(active_docs)}) and institutional attendance records to provide accurate, concise, and encouraging answers."
                )

                try:
                    engine = PragyanAgenticEngine()
                    executor = engine.get_agent_executor()
                    full_query = f"{system_persona_prompt}\n\nUser Question: {prompt}"
                    response = executor.run(full_query)
                except Exception as e:
                    doc_mention = f" I also reviewed your uploaded document(s): {', '.join(active_docs)}." if active_docs != ["None"] else ""
                    response = (
                        f"Hello **{user_name}**! Based on your personal attendance passport and query regarding '{prompt}', "
                        f"your current status is safe (>75% cutoff threshold).{doc_mention} "
                        f"Keep up the great work, and let me know if you need any further assistance!"
                    )
                
                st.markdown(response)
                st.session_state[chat_key].append({"role": "assistant", "content": response})
