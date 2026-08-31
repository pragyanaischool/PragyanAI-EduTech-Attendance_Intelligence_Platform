import streamlit as st
from modules.qr_engine import QREngine

def render_faculty_dashboard():
    """
    Renders the dedicated faculty control center with live session QR generation,
    session timers, and real-time student attendance monitoring streams.
    """
    user_name = st.session_state.get("user_name", "Dr. Faculty 1 (Comp)")
    
    st.markdown(f"# 👨‍🏫 Faculty Control Center — {user_name}")
    st.markdown("### *Manage Assigned Classes & Secure Session Tokens*")

    # Tabs for QR Generation and Live Turnout Stream
    tab1, tab2, tab3 = st.tabs(["🚀 Generate Live QR Session", "📊 Live Attendance Stream", "📚 Assigned Subjects & Classes"])

    with tab1:
        st.markdown("#### Initialize Secure Time-Limited Attendance Session")
        st.info("💡 **Security Feature:** Generated QR codes contain expiring token hashes to prevent proxy attendance and student sharing.")

        col1, col2 = st.columns(2)
        
        with col1:
            with st.form("qr_session_form"):
                subject = st.selectbox(
                    "Select Assigned Subject & Class", 
                    [
                        "Digital Electronics (ECE - Semester 5 - Section A)", 
                        "VLSI Design (ECE - Semester 6 - Section B)", 
                        "Microprocessors (ECE - Semester 6 - Section A)"
                    ]
                )
                duration = st.slider("QR Session Validity Window (Minutes)", min_value=5, max_value=30, value=10)
                generate_btn = st.form_submit_button("🚀 GENERATE SECURE QR")
                
                if generate_btn:
                    # Generate secure token using QREngine module
                    token, expiry = QREngine.generate_session_token(faculty_id=1, subject_id=101, duration_minutes=duration)
                    st.session_state.active_qr_token = token
                    st.session_state.qr_expiry = expiry
                    st.session_state.active_subject = subject

        with col2:
            st.markdown("#### Active QR Code Preview")
            if "active_qr_token" in st.session_state:
                qr_io = QREngine.create_qr_image(st.session_state.active_qr_token)
                st.image(qr_io, caption=f"Session Active for: {st.session_state.active_subject}", width=240)
                st.caption(alignment="center", body=f"⏳ Expires at: {st.session_state.qr_expiry.strftime('%H:%M:%S UTC')}")
            else:
                st.warning("No active session initialized. Configure parameters and click 'Generate Secure QR'.")

    with tab2:
        st.markdown("#### Real-Time Attendance Stream (Current Session)")
        st.markdown("Students scanning the active session QR code appear instantly below:")
        
        st.dataframe({
            "Student Name": ["Aarav Sharma", "Priya Patel", "Rahul Verma", "Sneha Reddy", "Vikram Malhotra"],
            "Enrollment No": ["PRG2026ECE001", "PRG2026ECE002", "PRG2026ECE003", "PRG2026ECE004", "PRG2026ECE005"],
            "Timestamp": ["10:00:12 AM", "10:00:15 AM", "10:01:04 AM", "10:01:45 AM", "10:02:10 AM"],
            "Verification Method": ["QR Scan + Device Token", "QR Scan + Device Token", "QR Scan (Late)", "QR Scan + Device Token", "QR Scan + Device Token"],
            "Status": ["PRESENT", "PRESENT", "LATE", "PRESENT", "PRESENT"]
        }, use_container_width=True)

    with tab3:
        st.markdown("#### Your Assigned Curriculum & Teaching Schedule")
        st.dataframe({
            "Subject Code": ["ECE501", "ECE502", "ECE601"],
            "Subject Name": ["Digital Electronics", "Signals & Systems", "VLSI Design"],
            "Semester": [5, 5, 6],
            "Assigned Sections": ["ECE-A & ECE-B", "ECE-C", "ECE-A"],
            "Average Turnout": ["89.2%", "78.5%", "91.0%"]
        }, use_container_width=True)
