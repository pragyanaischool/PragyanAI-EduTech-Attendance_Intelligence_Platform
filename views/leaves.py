import streamlit as st
import datetime
from utils.helpers import render_brand_logo

def render_leave_portal():
    """
    Renders the dedicated Leave Application & Approval Portal with safe brand watermark logo,
    submission forms, and multi-tier approval workflows supporting Student, Faculty, and Parent roles.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    user_role = st.session_state.get("role", "Student")
    
    st.markdown("### 📝 Leave Application & Multi-Tier Approval Portal")
    st.info(
        "💡 **Multi-Tier Workflow:** Students, Parents, and **even Faculty members** can submit official leave "
        "applications below. Department HODs, Principals, and Admins review and action them in real time."
    )

    # 2. Initialize global mock leave database in session state if not present
    if "global_leaves" not in st.session_state:
        st.session_state.global_leaves = [
            {"id": 1, "applicant": "Aarav Sharma", "role": "Student", "dept": "Electronics & Communication (ECE)", "from": "2026-09-02", "to": "2026-09-04", "reason": "Viral fever / Medical recovery certificate attached", "status": "Pending"},
            {"id": 2, "applicant": "Dr. Smitha Rao", "role": "Faculty", "dept": "Electronics & Communication (ECE)", "from": "2026-09-05", "to": "2026-09-06", "reason": "IEEE Technical Conference Presentation & Session Duties", "status": "Pending"},
            {"id": 3, "applicant": "Priya Patel", "role": "Student", "dept": "Computer Science (CSE)", "from": "2026-08-28", "to": "2026-08-30", "reason": "Family emergency travel", "status": "Approved"}
        ]

    # 3. Modular Tabs for Application vs. Approval Queue
    tab1, tab2 = st.tabs(["📤 Submit Leave Form", "📥 Review & Approval Queue"])

    with tab1:
        st.markdown("#### Fill Official Leave Application")
        with st.form("leave_submission_form"):
            col1, col2 = st.columns(2)
            with col1:
                from_d = st.date_input("From Date", datetime.date.today())
            with col2:
                to_d = st.date_input("To Date", datetime.date.today())
            
            leave_category = st.selectbox("Leave Category", ["Medical Leave", "Academic / Conference Leave", "Personal / Family Emergency", "Official Duty (OD)"])
            reason = st.text_area("Detailed Reason for Leave", placeholder="Provide clear medical justification or official academic reason...")
            
            submit_btn = st.form_submit_button("🚀 Submit Leave Application")
            
            if submit_btn:
                if reason.strip():
                    new_req = {
                        "id": len(st.session_state.global_leaves) + 1,
                        "applicant": user_name,
                        "role": user_role,
                        "dept": "Electronics & Communication (ECE)",
                        "from": str(from_d),
                        "to": str(to_d),
                        "reason": f"[{leave_category}] {reason}",
                        "status": "Pending"
                    }
                    st.session_state.global_leaves.append(new_req)
                    st.success("Leave application successfully submitted for institutional authority review!")
                else:
                    st.error("Please provide a valid reason before submitting your application.")

    with tab2:
        st.markdown("#### Leave Tracking & Processing Queue")
        
        # Student & Parent view: View personal request statuses
        if user_role in ["Student", "Parent"]:
            st.markdown("##### Your Personal Submitted Leave Status Tracker")
            my_reqs = [l for l in st.session_state.global_leaves if l['applicant'] == user_name or (user_role == "Parent" and "Sateesh" in l['applicant'])]
            
            if not my_reqs:
                st.info("No leave applications found for your account.")
            
            for req in my_reqs:
                color = "orange" if req['status']=="Pending" else ("green" if req['status']=="Approved" else "red")
                st.markdown(f"- **{req['from']} to {req['to']}** | Reason: *{req['reason']}* | Status: :{color}[**{req['status']}**]")
        
        # Approver view (Faculty, HOD, Principal, Admin): Manage pending queue
        else:
            st.markdown("##### Pending Approval Queue (Department / Institution)")
            pending_items = [l for l in st.session_state.global_leaves if l['status'] == "Pending"]
            
            if not pending_items:
                st.success("🎉 No pending leave applications requiring your review right now.")
            
            for req in st.session_state.global_leaves:
                if req['status'] == "Pending":
                    with st.expander(f"Review Leave: {req['applicant']} ({req['role']} - {req['dept']}) | {req['from']} to {req['to']} ⏳"):
                        st.write(f"**Applicant:** {req['applicant']} ({req['role']})")
                        st.write(f"**Department:** {req['dept']}")
                        st.write(f"**Duration:** {req['from']} to {req['to']}")
                        st.write(f"**Reason:** {req['reason']}")
                        
                        ca, cb = st.columns(2)
                        if ca.button("✅ Approve Request", key=f"app_{req['id']}"):
                            req['status'] = "Approved"
                            st.success(f"Leave request for {req['applicant']} approved successfully!")
                            st.rerun()
                        if cb.button("❌ Reject Request", key=f"rej_{req['id']}"):
                            req['status'] = "Rejected"
                            st.warning(f"Leave request for {req['applicant']} rejected.")
                            st.rerun()
                else:
                    st.caption(f"Archived Request: {req['applicant']} ({req['role']}) -> Status: {req['status']}")
