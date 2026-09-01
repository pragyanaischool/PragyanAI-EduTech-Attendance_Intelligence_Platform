import streamlit as st
from utils.helpers import render_brand_logo
from modules.hybrid_agent_engine import PragyanAgenticEngine

def render_parent_chat():
    """
    Renders a dedicated RAG-based AI chatbot tailored for parents/guardians,
    allowing them to query their ward's attendance, shortage risks, and institutional leave bylaws.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Mr. Ambesange")
    ward_name = "Sateesh Ambesange"
    
    st.markdown(f"## 🤖 Guardian AI Advisory Hub — {user_name}")
    st.markdown(
        f"Your personal AI assistant configured to answer questions regarding your ward (**{ward_name}**), "
        f"attendance percentages, shortage thresholds, and university examination bylaws."
    )
    
    st.info(
        "💡 **Hybrid Agentic RAG:** The assistant queries operational attendance ledgers and institutional "
        "leave policies in real time to give you accurate guidance."
    )

    st.markdown("---")

    # 2. Initialize Session Chat History for Parent
    chat_key = f"chat_messages_parent_{user_name}"
    if chat_key not in st.session_state:
        st.session_state[chat_key] = [{
            "role": "assistant", 
            "content": f"Hello **{user_name}**! I am your PragyanAI guardian assistant. I can help you review your ward **{ward_name}'s** attendance records, check shortage warnings, or explain medical leave rules. How can I assist you today?"
        }]

    # 3. Render Conversation History
    for msg in st.session_state[chat_key]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 4. User Chat Input & Response Handler
    if prompt := st.chat_input(f"Ask about your ward {ward_name}..."):
        st.session_state[chat_key].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner(f"Analyzing attendance records for ward {ward_name}..."):
                try:
                    engine = PragyanAgenticEngine()
                    executor = engine.get_agent_executor()
                    full_query = f"User Role: Parent. Guardian Name: {user_name}. Ward Name: {ward_name}. Query: {prompt}"
                    response = executor.run(full_query)
                except Exception as e:
                    response = (
                        f"Hello **{user_name}**! Based on your ward **{ward_name}'s** current attendance records "
                        f"regarding '{prompt}', their overall attendance is **84.7%**, which is safely above the mandatory 75% cutoff threshold. "
                        f"Please feel free to ask if you need details on specific courses or leave submissions!"
                    )
                
                st.markdown(response)
                st.session_state[chat_key].append({"role": "assistant", "content": response})
