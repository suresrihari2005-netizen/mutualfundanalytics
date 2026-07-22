from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

doc = SimpleDocTemplate("output/company_tearsheet.pdf")

story = []

story.append(Paragraph("<b>Company Financial Tearsheet</b>", styles["Heading1"]))
story.append(Paragraph("Sample financial summary generated for Day 33.", styles["BodyText"]))

data = [
    ["Metric", "Value"],
    ["Company", "ABC Ltd"],
    ["Revenue Growth", "21%"],
    ["Profit Growth", "15%"],
    ["ROE", "18%"],
    ["Cash Flow", "Strong"],
    ["Valuation", "Fair Value"]
]

table = Table(data)

table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
]))

story.append(table)

doc.build(story)

print("Day 33 Completed Successfully!")
print("Saved: output/company_tearsheet.pdf")