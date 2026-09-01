import streamlit as st
from modules.database import PragyanDatabase
from utils.helpers import render_brand_logo

def render_hod_profile():
    """
    Renders the dedicated HOD Profile & Database Management view, allowing department heads 
    to manage deanery office credentials, department records, and automated policy preferences.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. HOD (ECE)")
    
    # Initialize Database State
    PragyanDatabase.initialize_database()
    
    st.markdown(f"## 🏛️ HOD Administrative Profile & Database Hub — {user_name}")
    st.markdown(
        f"Manage your department head profile, administrative office credentials, "
        f"departmental compliance bylaws, and database records."
    )
    
    st.info(
        "💡 **HOD Portal Security:** Updates made here synchronize with principal executive "
        "dashboards and dictate automated department leave approval workflows."
    )

    st.markdown("---")

    # 2. HOD Database Entry & Profile Form
    with st.form("hod_profile_management_form"):
        st.markdown("### 📋 Department Head Credentials & Database Entry")
        
        c1, c2 = st.columns(2)
        
        with c1:
            hod_name_input = st.text_input("Full Name & Title", value=user_name)
            email_input = st.text_input("Institutional Email", value="hod.ece@pragyan.edu")
            emp_id_input = st.text_input("Administrative Employee ID", value="HOD_ECE_2026_01")
            
        with c2:
            dept_input = st.text_input("Managed Department", value="Electronics & Communication (ECE)")
            office_input = st.text_input("Deanery Office Location", value="Block A, Room 102 (Administrative Wing)")
            status_input = st.selectbox("Campus Availability Status", ["🟢 Available in Deanery", "🟢 Available on Campus", "🔴 On Official Leave", "🟡 In Executive Meetings"])
            
        st.text_area(
            "Executive Department Statement", 
            value="Directing department-wide academic rigor, faculty lecture audits, attendance compliance, and student shortage counseling programs."
        )

        st.markdown("---")
        st.markdown("### ⚙️ Departmental Policy & Notification Preferences")
        
        nc1, nc2 = st.columns(2)
        with nc1:
            st.checkbox("Receive Instant Alerts for Pending Leave Approvals", value=True)
            st.checkbox("Receive Weekly Department Attendance Audit Summaries", value=True)
        with nc2:
            st.checkbox("Automated Dispatch of Shortage Warnings (<75%)", value=True)
            st.checkbox("Executive Principal Broadcast Integration", value=True)

        st.markdown("---")
        
        if st.form_submit_button("💾 Save & Insert HOD Record into Database"):
            new_hod_record = {
                "employee_id": emp_id_input,
                "hod_name": hod_name_input,
                "department": dept_input,
                "deanery_office": office_input,
                "availability_status": status_input
            }
            if "db_hod_records" not in st.session_state:
                st.session_state.db_hod_records = []
            st.session_state.db_hod_records.insert(0, new_hod_record)
            st.success(f"🎉 Administrative profile and database records for **{hod_name_input}** updated successfully!")

    st.markdown("---")

    # 3. Active HOD Database Table Ledger
    st.markdown("### 🗄️ Active HOD Database Records Ledger")
    st.markdown("Review all department head records currently persisted in the local database session.")
    st.dataframe(PragyanDatabase.get_hod_records(), use_container_width=True)
