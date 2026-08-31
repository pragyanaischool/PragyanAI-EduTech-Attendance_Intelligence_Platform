import streamlit as st

def load_custom_css():
    """
    Loads sleek, enterprise-grade dark-mode custom CSS for Streamlit 
    to create a modern dashboard experience.
    """
    st.markdown("""
        <style>
        /* Global App Theme */
        .stApp {
            background-color: #0B0F19;
            color: #F3F4F6;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #111827;
            border-right: 1px solid #1F2937;
        }
        [data-testid="stSidebar"] .stRadio label {
            color: #E5E7EB;
            font-weight: 500;
        }

        /* Metric Cards Styling */
        .metric-card {
            background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
            border: 1px solid #374151;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2), 0 2px 4px -1px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .metric-card:hover {
            border-color: #3B82F6;
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.1);
        }
        .metric-card h3 {
            color: #F9FAFB;
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 4px;
        }
        .metric-card p {
            color: #9CA3AF;
            font-size: 0.9rem;
            margin: 0;
            font-weight: 500;
        }

        /* Buttons & Interactions */
        .stButton>button {
            background-color: #2563EB;
            color: white;
            border-radius: 6px;
            border: none;
            font-weight: 600;
            padding: 0.5rem 1rem;
            transition: background-color 0.2s ease, transform 0.1s ease;
        }
        .stButton>button:hover {
            background-color: #1D4ED8;
            color: #FFFFFF;
        }
        .stButton>button:active {
            transform: scale(0.98);
        }

        /* Dataframes & Tables */
        [data-testid="stDataFrame"] {
            border: 1px solid #374151;
            border-radius: 8px;
            overflow: hidden;
            background-color: #111827;
        }

        /* Input Fields & Selectboxes */
        .stTextInput>div>div>input, .stSelectbox>div>div>div {
            background-color: #1F2937;
            color: #F3F4F6;
            border: 1px solid #374151;
            border-radius: 6px;
        }
        .stTextInput>div>div>input:focus, .stSelectbox>div>div>div:focus {
            border-color: #3B82F6;
            box-shadow: 0 0 0 1px #3B82F6;
        }

        /* Headers & Typography */
        h1, h2, h3 {
            color: #F9FAFB;
            font-weight: 700;
            letter-spacing: -0.025em;
        }
        p {
            color: #D1D5DB;
        }

        /* Expander Styling */
        .streamlit-expanderHeader {
            background-color: #1F2937;
            border: 1px solid #374151;
            border-radius: 6px;
            color: #F3F4F6;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)
