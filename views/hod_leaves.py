import streamlit as st
from utils.helpers import render_brand_logo

def render_hod_leaves():
    """
    Renders the dedicated HOD Department Leave & Exemption Approval Hub,
    allowing department heads to review, endorse, or approve faculty and student leave applications.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. HOD (ECE)")
    dept_name = "Electronics & Communication (ECE)"
    
    st.markdown(f"## 📝 Department Leave & Disciplinary Approval Hub — {user_name}")
    st.markdown(
        f"Review, endorse, and action faculty leave requests and student medical exemptions "
        f"for the **{dept_name}** department."
    )
    
    st.info(
        "💡 **HOD Approval Governance:** Approvals granted here immediately update student attendance passports "
        "and credit medical grace days across the institutional ledger."
    )

    st.markdown("---")

    # 2. Split Tab / Section for Student vs Faculty Leave Approvals
    tab1, tab2 = st.tabs(["🎓 Student Medical & Leave Requests", "👨‍🏫 Faculty Leave Applications"])

    with tab1:
        st.markdown("### 📋 Pending Student Leave & Exemption Queue")
        
        # Mock Pending Student Requests
        st.markdown(
            """
            <div style="padding: 15px; border-radius: 8px; background-color: #1e293b; border-left: 5px solid #f59e0b; margin-bottom: 15px;">
                <h4 style="margin: 0; color: #f8fafc;">Aarav Sharma (Roll: ECE_2026_01) — Sem 5</h4>
                <p style="margin: 5px 0; font-size: 0.85rem; color: #94a3b8;">
                    <b>Duration:</b> Sep 3, 2026 to Sep 5, 2026 &nbsp;|&nbsp; <b>Type:</b> Medical Leave (Viral Fever Recovery)
                </p>
                <p style="margin: 0; color: #e2e8f0; font-size: 0.95rem;"><b>Attached Document:</b> 📄 <code>Medical_Certificate_Aarav.pdf</code> (Verified by Faculty Advisor)</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        col_s1, col_s2 = st.columns(2)
        if col_s1.button("✅ Approve Student Medical Leave & Grant Exemption", key="approve_student_leave_1"):
            st.success("Student leave request approved! Attendance passport updated with 3 days medical exemption grace.")
        if col_s2.button("❌ Reject / Request Further Proof", key="reject_student_leave_1"):
            st.warning("Rejection notification dispatched to student.")

    with tab2:
        st.markdown("### 📋 Pending Faculty Leave & Adjustment Queue")
        
        # Mock Pending Faculty Requests
        st.markdown(
            """
            <div style="padding: 15px; border-radius: 8px; background-color: #1e293b; border-left: 5px solid #3b82f6; margin-bottom: 15px;">
                <h4 style="margin: 0; color: #f8fafc;">Dr. Smitha Rao (VLSI Design Chair)</h4>
                <p style="margin: 5px 0; font-size: 0.85rem; color: #94a3b8;">
                    <b>Duration:</b> Sep 10, 2026 to Sep 11, 2026 &nbsp;|&nbsp; <b>Type:</b> IEEE National Conference Presentation
                </p>
                <p style="margin: 0; color: #e2e8f0; font-size: 0.95rem;"><b>Lecture Adjustment:</b> Covered by Prof. Anand Kumar (Digital Systems)</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        col_f1, col_f2 = st.columns(2)
        if col_f1.button("✅ Sanction Faculty Leave & Confirm Adjustment", key="approve_faculty_leave_1"):
            st.success("Faculty leave sanctioned successfully and logged to principal deanery audit!")
        if col_f2.button("❌ Return for Schedule Revision", key="reject_faculty_leave_1"):
            st.warning("Leave application returned to faculty for timetable adjustment.")
