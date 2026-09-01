import streamlit as st
from utils.helpers import render_brand_logo

def render_principal_leaves():
    """
    Renders the dedicated Principal's Institutional Leave & Sabbatical Governance Hub,
    allowing the principal to review escalated departmental leaves, sabbaticals, and attendance policy bylaws.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal")
    
    st.markdown(f"## 📝 Institutional Leave Governance & Sabbatical Hub — {user_name}")
    st.markdown("Review escalated departmental leave requests, faculty sabbaticals, and institute-wide attendance policy bylaws.")

    st.info(
        "💡 **Executive Governance:** Approvals granted at this level apply institution-wide "
        "and synchronize with state university compliance records."
    )

    st.markdown("---")

    # 2. Escalated Leave & Sabbatical Review Section
    st.markdown("### 🏛️ Escalated Department Head & Faculty Sabbatical Requests")
    
    st.markdown(
        """
        <div style="padding: 15px; border-radius: 8px; background-color: #1e293b; border-left: 5px solid #3b82f6; margin-bottom: 15px;">
            <h4 style="margin: 0; color: #f8fafc;">Dr. HOD (ECE) — Sabbatical & Research Deputation</h4>
            <p style="margin: 5px 0; font-size: 0.85rem; color: #94a3b8;">
                <b>Duration:</b> Oct 1, 2026 to Oct 15, 2026 &nbsp;|&nbsp; <b>Type:</b> International IEEE VLSI Summit Keynote
            </p>
            <p style="margin: 0; color: #e2e8f0; font-size: 0.95rem;"><b>Interim HOD Charge:</b> Assigned to Dr. Smitha Rao (Senior Chair)</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_p1, col_p2 = st.columns(2)
    if col_p1.button("✅ Sanction Executive Sabbatical", key="approve_princ_leave_1"):
        st.success("Sabbatical sanctioned successfully and interim charge notification dispatched to faculty council!")
    if col_p2.button("❌ Request Administrative Review", key="reject_princ_leave_1"):
        st.warning("Administrative review request dispatched to HOD.")
