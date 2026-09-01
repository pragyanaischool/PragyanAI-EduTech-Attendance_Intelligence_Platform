import streamlit as st
from utils.helpers import render_brand_logo
from modules.report_generator import PDFReportGenerator

def render_faculty_reports():
    """
    Renders the dedicated Faculty PDF Reports Center, allowing faculty members 
    to export certified course attendance rosters and lecture delivery audit summaries.
    """
    # 1. Safe Brand Watermark Logo Integration
    render_brand_logo(width=220, is_sidebar=False)
    
    user_name = st.session_state.get("user_name", "Dr. Faculty (ECE)")
    
    st.markdown(f"## 📄 Faculty Certified Reports & Course Rosters — {user_name}")
    st.markdown("Export official cryptographic PDF attendance rosters and lecture delivery audit reports.")

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
            ["Assigned Course Attendance Roster (ECE301)", "Daily Lecture Delivery & QR Audit Report"]
        )
        academic_term = st.selectbox("Select Academic Term", ["Fall Semester 2026", "Spring Semester 2026"])

    with col_r2:
        st.markdown("### 📋 Metadata Preview")
        st.markdown(f"**Faculty Name:** `{user_name}`")
        st.markdown(f"**Department:** `Electronics & Communication (ECE)`")
        st.markdown(f"**Document Type:** `{doc_type}`")
        st.markdown("**Certification Status:** PragyanAI Verified Seal")

    st.markdown("---")

    # 3. Compilation & Download
    st.markdown("### 🚀 Compile & Download PDF")
    if st.button("📥 Generate Certified Faculty PDF Report"):
        with st.spinner(f"Compiling official PDF report for {user_name}..."):
            pdf_bytes = PDFReportGenerator.generate_department_pdf(
                dept_name=f"Faculty Roster - {user_name}", 
                analytics_summary={
                    "total_students": 48, 
                    "avg_attendance": 89.2, 
                    "shortage_count": 3, 
                    "critical_count": 1
                }
            )
            
            st.success("🎉 Certified PDF course roster compiled successfully!")
            
            st.download_button(
                label=f"💾 Download {doc_type.replace(' ', '_')}.pdf",
                data=pdf_bytes,
                file_name=f"PragyanAI_Faculty_Report_{user_name.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )
