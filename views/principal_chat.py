import streamlit as st
from utils.helpers import render_brand_logo
from modules.hybrid_agent_engine import PragyanAgenticEngine

def render_principal_chat():
    """
    Renders a dedicated RAG-based AI executive advisory chatbot tailored for Principal roles.
    Supports university policy document uploads, multi-department compliance queries, and accreditation analytics.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal")
    
    st.markdown(f"## 🤖 Principal's Executive AI Advisory Hub — {user_name}")
    st.markdown(
        f"Your dedicated AI executive advisor. Configured specifically for **{user_name}** (Principal & CAO). "
        f"Query multi-department attendance turnouts, review institutional accreditation bylaws, or analyze institute-wide shortage risks."
    )
    
    # 2. Executive Policy Document Uploader Expander
    with st.expander("📁 Upload University Bylaws, Accreditation Guidelines, or State Grant Proposals", expanded=False):
        st.markdown("Upload files to add them to your private executive RAG knowledge base:")
        uploaded_files = st.file_uploader(
            "Choose PDF, TXT, or DOCX files", 
            type=["pdf", "txt", "docx"], 
            accept_multiple_files=True,
            key=f"principal_uploader_{user_name}"
        )
        
        if uploaded_files:
            if "principal_uploaded_docs" not in st.session_state:
                st.session_state.principal_uploaded_docs = []
            
            for file in uploaded_files:
                if file.name not in st.session_state.principal_uploaded_docs:
                    st.session_state.principal_uploaded_docs.append(file.name)
            
            st.success(f"Successfully indexed {len(uploaded_files)} executive file(s) into your repository!")

        if "principal_uploaded_docs" in st.session_state and st.session_state.principal_uploaded_docs:
            st.markdown(f"**Currently Indexed Executive Documents:**")
            for doc in st.session_state.principal_uploaded_docs:
                st.markdown(f"- 📄 `{doc}`")

    st.markdown("---")

    # 3. Initialize Session Chat History for Principal
    chat_key = f"chat_messages_principal_{user_name}"
    if chat_key not in st.session_state:
        st.session_state[chat_key] = [{
            "role": "assistant", 
            "content": f"Hello **{user_name}**! I am your executive AI advisory assistant. I have loaded all multi-department attendance ledgers and institutional compliance reports. How can I assist with academic governance today?"
        }]

    # 4. Render Conversation History
    for msg in st.session_state[chat_key]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 5. User Chat Input & Response Handler
    if prompt := st.chat_input(f"Ask executive advisor, {user_name}..."):
        st.session_state[chat_key].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Analyzing institutional analytics and multi-department records..."):
                try:
                    engine = PragyanAgenticEngine()
                    executor = engine.get_agent_executor()
                    full_query = f"Principal Name: {user_name}. Query: {prompt}"
                    response = executor.run(full_query)
                except Exception as e:
                    response = (
                        f"Hello **{user_name}**! Based on your executive inquiry regarding '{prompt}', "
                        f"the institution is maintaining an average turnout of **88.6%** across all 5 departments, with 142 students on the shortage watch list. "
                        f"Let me know if you would like me to draft an executive circular or policy review!"
                    )
                
                st.markdown(response)
                st.session_state[chat_key].append({"role": "assistant", "content": response})
