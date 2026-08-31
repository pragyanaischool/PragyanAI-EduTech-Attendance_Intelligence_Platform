import streamlit as st
import os

def render_brand_logo(width=200, is_sidebar=True):
    """
    Safely renders the institutional brand logo if present in the root directory,
    else gracefully renders a clean text and emoji header.
    """
    logo_path = "PragyanAI_Transparent.png"
    target = st.sidebar if is_sidebar else st
    
    if os.path.exists(logo_path):
        try:
            target.image(logo_path, width=width)
            return
        except Exception:
            pass
            
    # Fallback header if image is missing or fails to decode
    target.markdown("### 🎓 **PragyanAI Intelligence Hub**")
