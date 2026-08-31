import streamlit as st

class NotificationEngine:
    @staticmethod
    def send_shortage_alert(student_name, parent_email, phone_number, subjects_in_shortage):
        """Simulates sending WhatsApp & Email alerts to parents regarding low attendance."""
        message = (
            f"⚠️ PRAGYAN-AI ATTENDANCE ALERT\n"
            f"Dear Parent, your ward {student_name} has fallen below the safety cutoff "
            f"in the following subjects: {', '.join(subjects_in_shortage)}. "
            f"Please ensure regular attendance to avoid examination detention."
        )
        
        st.success(f"📧 Email dispatched successfully to: {parent_email}")
        st.success(f"📱 WhatsApp notification triggered successfully to: {phone_number}")
        st.code(message, language="text")
