from app.models.story import Story
import markdown
from fpdf import FPDF

class Exporter:
    @staticmethod
    def to_pdf(story: Story) -> str:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=story.outline.title, ln=1, align="C")
        pdf.multi_cell(0, 10, txt=story.full_content)
        filename = f"{story.outline.title.replace(' ', '_')}.pdf"
        pdf.output(filename)
        return filename

    @staticmethod
    def to_epub(story: Story) -> str:
        # Implementation for EPUB conversion
        # This would require a library like ebooklib
        pass

