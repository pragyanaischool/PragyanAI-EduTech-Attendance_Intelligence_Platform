import streamlit as st
import os

def render_brand_logo(width=220, is_sidebar=False):
    """
    Safely renders the PragyanAI brand watermark logo, catching any missing 
    file errors to prevent st.runtime.media_file_storage.MediaFileStorageError crashes.
    
    Parameters:
    - width (int): Display width of the logo image in pixels.
    - is_sidebar (bool): If True, renders in st.sidebar; otherwise renders in main body.
    """
    logo_path = "assets/PragyanAI_Transparent.png"
    try:
        if os.path.exists(logo_path):
            if is_sidebar:
                st.sidebar.image(logo_path, width=width)
            else:
                st.image(logo_path, width=width)
        else:
            # Fallback styled text watermark if the image file is not found on disk
            fallback_html = """
                <div style="padding: 5px 0; margin-bottom: 10px;">
                    <h3 style="color: #3b82f6; margin: 0; font-family: sans-serif;">⚡ PragyanAI</h3>
                    <p style="color: #94a3b8; font-size: 0.8rem; margin: 0;">Attendance Intelligence</p>
                </div>
            """
            if is_sidebar:
                st.sidebar.markdown(fallback_html, unsafe_allow_html=True)
            else:
                st.markdown(fallback_html, unsafe_allow_html=True)
    except Exception:
        # Failsafe fallback to ensure UI never crashes due to rendering exceptions
        fallback_text = "⚡ PragyanAI Attendance Intelligence"
        if is_sidebar:
            st.sidebar.markdown(f"### {fallback_text}")
        else:
            st.markdown(f"### {fallback_text}")
