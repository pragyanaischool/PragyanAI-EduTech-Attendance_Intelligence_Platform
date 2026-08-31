import streamlit as st
from utils.helpers import render_brand_logo
from modules.report_generator import PDFReportGenerator

def render_reports_view():
    """
    Renders the dedicated One-Click Institutional PDF Reports Center with safe brand watermark logo,
    scope selection, and ReportLab PDF compilation and download handlers.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "User")
    user_role = st.session_state.get("role", "Admin")
    
    st.markdown("## 📄 One-Click Institutional PDF Reports Center")
    st.markdown(
        f"Welcome, **{user_name}** (*{user_role}*). Generate and export official compliance attendance "
        "reports, departmental audit summaries, and shortage lists formatted professionally via ReportLab."
    )
    
    st.info(
        "💡 **Compliance Note:** All generated PDF documents are time-stamped and certified for "
        "university examination eligibility audits and parent counseling sessions."
    )

    st.markdown("---")

    # 2. Report Configuration and Scope Selection
    col_config1, col_config2 = st.columns(2)
    
    with col_config1:
        st.markdown("### ⚙️ Report Parameters")
        report_scope = st.selectbox(
            "Select Report Scope", 
            [
                "Faculty Attendance Summary", 
                "HOD Department Attendance Audit (ECE)", 
                "Principal Institute-Wide Compliance Report",
                "Critical Shortage & At-Risk Student Roster"
            ]
        )
        
        academic_term = st.selectbox("Select Academic Term", ["Fall Semester 2026", "Spring Semester 2026", "Full Academic Year 2025-26"])
        include_charts = st.checkbox("Include Statistical Summary Tables", value=True)

    with col_config2:
        st.markdown("### 📋 Preview Summary Metadata")
        st.markdown(f"**Target Scope:** `{report_scope}`")
        st.markdown(f"**Selected Term:** `{academic_term}`")
        st.markdown("**Format Engine:** ReportLab PDF Compiler")
        st.markdown("**Security Signature:** PragyanAI Institutional Seal")

    st.markdown("---")

    # 3. Compilation and Download Trigger
    st.markdown("### 🚀 Compile & Download PDF Document")
    
    if st.button("📥 Generate Official PDF Report"):
        with st.spinner("Compiling ReportLab document structure and rendering tables..."):
            # Generate PDF bytes using PDFReportGenerator module
            pdf_bytes = PDFReportGenerator.generate_department_pdf(
                dept_name="Electronics & Communication (ECE)", 
                analytics_summary={
                    "total_students": 420, 
                    "avg_attendance": 86.4, 
                    "shortage_count": 37, 
                    "critical_count": 12
                }
            )
            
            st.success("🎉 PDF document compiled and formatted successfully!")
            
            # Render Download Button
            st.download_button(
                label="💾 Click here to download compiled PDF",
                data=pdf_bytes,
                file_name=f"PragyanAI_{report_scope.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )
