from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

styles = getSampleStyleSheet()

companies = [
    {
        "name": "ABC Ltd",
        "revenue_growth": "21%",
        "profit_growth": "15%",
        "roe": "18%",
        "cashflow": "Strong"
    },
    {
        "name": "XYZ Industries",
        "revenue_growth": "12%",
        "profit_growth": "9%",
        "roe": "14%",
        "cashflow": "Average"
    },
    {
        "name": "Future Tech",
        "revenue_growth": "28%",
        "profit_growth": "22%",
        "roe": "24%",
        "cashflow": "Strong"
    }
]

output_folder = "output/company_reports"
os.makedirs(output_folder, exist_ok=True)

for company in companies:

    filename = os.path.join(
        output_folder,
        company["name"].replace(" ", "_") + ".pdf"
    )

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph(f"<b>{company['name']}</b>", styles["Heading1"]))
    story.append(Paragraph(f"Revenue Growth : {company['revenue_growth']}", styles["BodyText"]))
    story.append(Paragraph(f"Profit Growth : {company['profit_growth']}", styles["BodyText"]))
    story.append(Paragraph(f"ROE : {company['roe']}", styles["BodyText"]))
    story.append(Paragraph(f"Cash Flow : {company['cashflow']}", styles["BodyText"]))

    doc.build(story)

print("\nDay 34 Completed Successfully!")
print(f"{len(companies)} PDF reports created.")
print("Location: output/company_reports/")