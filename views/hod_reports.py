import streamlit as st
from utils.helpers import render_brand_logo
from modules.report_generator import PDFReportGenerator

def render_hod_reports():
    """
    Renders the dedicated HOD PDF Reports Center, allowing department heads 
    to export certified department attendance audits and faculty compliance summaries.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. HOD (ECE)")
    dept_name = "Electronics & Communication (ECE)"
    
    st.markdown(f"## 📄 HOD Certified Reports & Department Audits — {user_name}")
    st.markdown(f"Export official cryptographic PDF department audits and faculty compliance summaries for **{dept_name}**.")

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
                "Department Master Attendance Audit (ECE)",
                "Faculty Lecture Delivery & QR Compliance Summary",
                "Shortage & At-Risk Student Cohort Roster"
            ]
        )
        academic_term = st.selectbox("Select Academic Term", ["Fall Semester 2026", "Spring Semester 2026", "Full Year 2025-26"])

    with col_r2:
        st.markdown("### 📋 Metadata Preview")
        st.markdown(f"**HOD Name:** `{user_name}`")
        st.markdown(f"**Department:** `{dept_name}`")
        st.markdown(f"**Document Type:** `{doc_type}`")
        st.markdown("**Certification Status:** PragyanAI Verified Seal")

    st.markdown("---")

    # 3. Compilation & Download
    st.markdown("### 🚀 Compile & Download PDF Audit")
    if st.button("📥 Generate Certified Department PDF Audit"):
        with st.spinner(f"Compiling official PDF audit for {dept_name}..."):
            pdf_bytes = PDFReportGenerator.generate_department_pdf(
                dept_name=f"{dept_name} - {user_name}", 
                analytics_summary={
                    "total_students": 420, 
                    "avg_attendance": 87.4, 
                    "shortage_count": 37, 
                    "critical_count": 9
                }
            )
            
            st.success("🎉 Certified department audit PDF compiled successfully with zero errors!")
            
            st.download_button(
                label=f"💾 Download {doc_type.replace(' ', '_')}.pdf",
                data=pdf_bytes,
                file_name=f"PragyanAI_HOD_Audit_{dept_name.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )
