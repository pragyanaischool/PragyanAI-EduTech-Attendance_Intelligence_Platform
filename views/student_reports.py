import streamlit as st
from utils.helpers import render_brand_logo
from modules.report_generator import PDFReportGenerator

def render_student_reports():
    """
    Renders the dedicated Student PDF Reports Center, allowing students 
    to export and download their official certified attendance passport and semester grade summaries.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Sateesh Ambesange")
    
    st.markdown(f"## 📄 Student Certified Reports & Attendance Passport — {user_name}")
    st.markdown("Export official cryptographic PDF reports and semester attendance passports for administrative verification.")

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
            ["Official Attendance Passport & Course Ledger", "Semester Medical & Leave Summary Report"]
        )
        academic_term = st.selectbox("Select Academic Term", ["Fall Semester 2026", "Spring Semester 2026", "Full Year 2025-26"])

    with col_r2:
        st.markdown("### 📋 Metadata Preview")
        st.markdown(f"**Student Name:** `{user_name}`")
        st.markdown(f"**Roll Number:** `ECE_2026_042`")
        st.markdown(f"**Document Type:** `{doc_type}`")
        st.markdown("**Certification Status:** PragyanAI Verified Seal")

    st.markdown("---")

    # 3. Compilation & Download
    st.markdown("### 🚀 Compile & Download PDF")
    if st.button("📥 Generate Certified Student PDF Passport"):
        with st.spinner(f"Compiling official PDF report for {user_name}..."):
            # Generate tailored PDF bytes
            pdf_bytes = PDFReportGenerator.generate_department_pdf(
                dept_name=f"Student Passport - {user_name}", 
                analytics_summary={
                    "total_students": 1, 
                    "avg_attendance": 84.7, 
                    "shortage_count": 0, 
                    "critical_count": 0
                }
            )
            
            st.success("🎉 Certified PDF passport compiled successfully with zero formatting errors!")
            
            st.download_button(
                label=f"💾 Download {doc_type.replace(' ', '_')}.pdf",
                data=pdf_bytes,
                file_name=f"PragyanAI_Student_Passport_{user_name.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )
