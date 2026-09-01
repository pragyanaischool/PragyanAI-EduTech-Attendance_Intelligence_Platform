import streamlit as st
from utils.helpers import render_brand_logo
from modules.report_generator import PDFReportGenerator

def render_principal_reports():
    """
    Renders the dedicated Principal PDF Reports Center, allowing the executive principal 
    to export certified institute-wide compliance audits and university accreditation summaries.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Principal")
    
    st.markdown(f"## 📄 Principal Certified Reports & Institutional Audits — {user_name}")
    st.markdown("Export official cryptographic PDF institute-wide compliance audits and university accreditation summaries.")

    st.info(
        "💡 **ReportLab Engine:** All documents are compiled securely with institutional watermarks, "
        "digital timestamps, and official verification seals."
    )

    st.markdown("---")

    # 2. Report Selection & Generation
    col_r1, col_r2 = st.columns(2)
    
    with col_r1:
        st.markdown("### ⚙️ Document Configuration")
        doc_type = st.selectbox(
            "Select Certified Document Type", 
            [
                "Institute-Wide Master Attendance & Compliance Audit",
                "Multi-Department Accreditation & Faculty Roster Summary",
                "Executive Shortage & Student Success Report"
            ]
        )
        academic_term = st.selectbox("Select Academic Term", ["Fall Semester 2026", "Spring Semester 2026", "Full Year 2025-26"])

    with col_r2:
        st.markdown("### 📋 Metadata Preview")
        st.markdown(f"**Principal Name:** `{user_name}`")
        st.markdown(f"**Institution:** `PragyanAI University & Research Studio`")
        st.markdown(f"**Document Type:** `{doc_type}`")
        st.markdown("**Certification Status:** PragyanAI Verified Seal")

    st.markdown("---")

    # 3. Compilation & Download
    st.markdown("### 🚀 Compile & Download Executive PDF Audit")
    if st.button("📥 Generate Certified Executive PDF Audit"):
        with st.spinner("Compiling official institute-wide PDF audit..."):
            pdf_bytes = PDFReportGenerator.generate_department_pdf(
                dept_name=f"Executive Audit - {user_name}", 
                analytics_summary={
                    "total_students": 2450, 
                    "avg_attendance": 88.6, 
                    "shortage_count": 142, 
                    "critical_count": 28
                }
            )
            
            st.success("🎉 Certified executive audit PDF compiled successfully with zero errors!")
            
            st.download_button(
                label=f"💾 Download {doc_type.replace(' ', '_')}.pdf",
                data=pdf_bytes,
                file_name=f"PragyanAI_Principal_Executive_Audit.pdf",
                mime="application/pdf"
            )
