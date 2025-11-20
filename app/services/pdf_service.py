import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from typing import List
from app.models.asset import Asset


def generate_assets_report(assets: List[Asset]) -> str:
    """Generate PDF report for assets and return file path"""
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"assets_report_{timestamp}.pdf"
    filepath = os.path.join(reports_dir, filename)

    # Create PDF document
    doc = SimpleDocTemplate(filepath, pagesize=letter)
    elements = []

    # Add title
    styles = getSampleStyleSheet()
    title = Paragraph("Assets Inventory Report", styles['Title'])
    elements.append(title)

    # Add generation date
    date_str = f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    date_para = Paragraph(date_str, styles['Normal'])
    elements.append(date_para)

    # Add some space
    elements.append(Paragraph("<br/><br/>", styles['Normal']))

    # Prepare table data
    table_data = [['ID', 'Name', 'Category', 'Purchase Date', 'Serial Number']]

    for asset in assets:
        table_data.append([
            str(asset.id),
            asset.name,
            asset.category,
            asset.purchase_date.strftime('%Y-%m-%d'),
            asset.serial_number
        ])

    # Create table
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)

    # Build PDF
    doc.build(elements)

    return filepath