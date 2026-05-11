from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle
)
from reportlab.lib import colors
from datetime import datetime
from typing import List, Dict


class PDFExporter:
    def __init__(self, output_path: str):
        self.doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=32
        )

        self.styles = getSampleStyleSheet()
        self.story = []

        self._setup_custom_styles()

    def _setup_custom_styles(self):
        """تعریف استایل‌های سفارشی"""

        self.styles.add(
            ParagraphStyle(
                name="CustomTitle",
                parent=self.styles["Heading1"],
                fontSize=24,
                leading=30,
                alignment=TA_CENTER,
                textColor=colors.HexColor("#1f2937"),
                spaceAfter=30,
            )
        )

        self.styles.add(
            ParagraphStyle(
                name="SectionHeading",
                parent=self.styles["Heading2"],
                fontSize=18,
                leading=24,
                textColor=colors.HexColor("#2563eb"),
                spaceBefore=20,
                spaceAfter=12,
            )
        )

        self.styles.add(
            ParagraphStyle(
                name="CustomBody",
                parent=self.styles["BodyText"],
                fontSize=11,
                leading=18,
                alignment=TA_JUSTIFY,
                textColor=colors.HexColor("#111827"),
                spaceAfter=12,
            )
        )

        self.styles.add(
            ParagraphStyle(
                name="Citation",
                parent=self.styles["BodyText"],
                fontSize=9,
                leading=12,
                textColor=colors.HexColor("#6b7280"),
                leftIndent=16,
                spaceAfter=8,
            )
        )

    def add_title(self, title: str):
        """اضافه کردن عنوان اصلی"""

        self.story.append(
            Paragraph(title, self.styles["CustomTitle"])
        )

        self.story.append(
            Spacer(1, 0.3 * inch)
        )

    def add_metadata(self, topic: str):
        """اضافه کردن اطلاعات گزارش"""

        created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

        metadata = f"""
        <b>Topic:</b> {topic}<br/>
        <b>Generated At:</b> {created_at}
        """

        self.story.append(
            Paragraph(metadata, self.styles["CustomBody"])
        )

        self.story.append(
            Spacer(1, 0.2 * inch)
        )

    def add_section(self, heading: str, content: str):
        """اضافه کردن سکشن"""

        self.story.append(
            Paragraph(heading, self.styles["SectionHeading"])
        )

        paragraphs = content.split("\n\n")

        for para in paragraphs:
            para = para.strip()

            if para:
                self.story.append(
                    Paragraph(para, self.styles["CustomBody"])
                )

        self.story.append(
            Spacer(1, 0.15 * inch)
        )

    def add_bullet_list(self, items: List[str]):
        """اضافه کردن لیست"""

        for item in items:
            bullet = f"• {item}"

            self.story.append(
                Paragraph(bullet, self.styles["CustomBody"])
            )

    def add_table(self, headers: List[str], rows: List[List[str]]):
        """اضافه کردن جدول"""

        data = [headers] + rows

        table = Table(data, repeatRows=1)

        table.setStyle(
            TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563eb")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),

                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),

                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#f9fafb")),

                ("GRID", (0, 0), (-1, -1), 1, colors.HexColor("#d1d5db")),
            ])
        )

        self.story.append(table)

        self.story.append(
            Spacer(1, 0.25 * inch)
        )

    def add_citations(self, citations: List[Dict]):
        """اضافه کردن منابع"""

        self.story.append(
            PageBreak()
        )

        self.story.append(
            Paragraph("References", self.styles["SectionHeading"])
        )

        for idx, cite in enumerate(citations, start=1):

            citation_text = f"""
            [{idx}] <b>{cite.get('title', 'Unknown')}</b><br/>
            URL: {cite.get('url', 'N/A')}<br/>
            Accessed: {cite.get('date', 'N/A')}
            """

            self.story.append(
                Paragraph(citation_text, self.styles["Citation"])
            )

    def add_page_break(self):
        """رفتن به صفحه بعد"""

        self.story.append(PageBreak())

    def build(self):
        """ساخت PDF نهایی"""

        self.doc.build(self.story)


# مثال استفاده
if __name__ == "__main__":

    exporter = PDFExporter("research_report.pdf")

    exporter.add_title("AI Research Report")

    exporter.add_metadata(
        topic="Multi-Agent AI Systems"
    )

    exporter.add_section(
        heading="Introduction",
        content="""
        Multi-agent systems are becoming one of the most important
        paradigms in modern AI applications.

        These systems allow autonomous agents to collaborate,
        coordinate, and solve complex tasks.
        """
    )

    exporter.add_section(
        heading="Key Advantages",
        content="""
        Agentic workflows provide modularity, scalability,
        and autonomous decision making.
        """
    )

    exporter.add_bullet_list([
        "Autonomous planning",
        "Parallel execution",
        "Tool usage",
        "Self-reflection",
        "Collaborative reasoning"
    ])

    exporter.add_table(
        headers=["Component", "Purpose"],
        rows=[
            ["Planner", "Creates task plan"],
            ["Searcher", "Finds information"],
            ["Summarizer", "Condenses results"],
            ["Critic", "Evaluates quality"]
        ]
    )

    exporter.add_citations([
        {
            "title": "LangGraph Documentation",
            "url": "https://python.langchain.com/docs/langgraph",
            "date": "2026-05-11"
        },
        {
            "title": "OpenAI Research",
            "url": "https://openai.com/research",
            "date": "2026-05-11"
        }
    ])

    exporter.build()

    print("✅ PDF generated successfully!")
