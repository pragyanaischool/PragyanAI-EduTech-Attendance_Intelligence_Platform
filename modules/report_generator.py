from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from io import BytesIO

class PDFReportGenerator:
    @staticmethod
    def generate_department_pdf(dept_name, analytics_summary):
        """Compiles clean institutional PDF audit documents using ReportLab."""
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
        story = []
        styles = getSampleStyleSheet()
        
        title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=18, textColor=colors.HexColor("#1F2937"), spaceAfter=12)
        story.append(Paragraph(f"PragyanAI Official Institutional Report — {dept_name}", title_style))
        story.append(Paragraph(f"Generated via Attendance Intelligence Platform | Date: August 2026", styles['Normal']))
        story.append(Spacer(1, 15))
        
        data = [
            ["Metric Category", "Institutional Value"],
            ["Total Department Students", str(analytics_summary.get("total_students", 420))],
            ["Overall Average Attendance", f"{analytics_summary.get('avg_attendance', 86.4)}%"],
            ["Active Shortage Count (<75%)", str(analytics_summary.get("shortage_count", 37))],
            ["Critical Risk Students (<65%)", str(analytics_summary.get("critical_count", 12))]
        ]
        
        t = Table(data, colWidths=[250, 250])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2563EB")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0,0), (-1,0), 8),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#F3F4F6")),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#D1D5DB"))
        ]))
        
        story.append(t)
        doc.build(story)
        buffer.seek(0)
        return buffer
