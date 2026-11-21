"""Build the CV PDF and social preview from the site's existing content."""

from pathlib import Path
from xml.sax.saxutils import escape

import yaml
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer,
)

ROOT = Path(__file__).resolve().parents[1]
ACCENT = "#99178c"
TEXT = "#20212a"
MUTED = "#58616f"


def clean(value):
    return str(value).replace("–", "-").replace("—", "-").replace("’", "'")


def build_cv():
    cv = yaml.safe_load((ROOT / "_data/cv.yml").read_text())
    destination = ROOT / "assets/pdf/laurence-miao-cv.pdf"
    destination.parent.mkdir(parents=True, exist_ok=True)
    styles = {
        "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=26, leading=31, textColor=colors.HexColor(TEXT), spaceAfter=7),
        "role": ParagraphStyle("role", fontName="Helvetica", fontSize=10.5, leading=15, textColor=colors.HexColor(ACCENT), spaceAfter=6),
        "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10, leading=14, textColor=colors.HexColor(TEXT), spaceAfter=5),
        "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=colors.HexColor(ACCENT), spaceBefore=14, spaceAfter=8, keepWithNext=True),
        "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=10.5, leading=14, textColor=colors.HexColor(TEXT), spaceAfter=2, keepWithNext=True),
        "meta": ParagraphStyle("meta", fontName="Helvetica", fontSize=9, leading=12.5, textColor=colors.HexColor(MUTED), spaceAfter=5, keepWithNext=True),
        "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.5, leading=13.2, textColor=colors.HexColor(TEXT), leftIndent=10, firstLineIndent=-8, spaceAfter=4),
    }
    story = []

    def paragraph(text, style="body"):
        return Paragraph(escape(clean(text)), styles[style])

    def heading(text):
        story.append(paragraph(text, "section"))

    story.append(paragraph("Laurence Miao", "name"))
    story.append(paragraph(cv["contact"][1]["value"], "role"))
    story.append(Paragraph(
        '<link href="https://laurence-miao.github.io" color="' + ACCENT + '">laurence-miao.github.io</link>'
        ' &nbsp; | &nbsp; <link href="https://www.linkedin.com/in/laurence-miao/" color="' + ACCENT + '">linkedin.com/in/laurence-miao</link>',
        styles["body"],
    ))
    heading("Professional summary")
    for line in cv["summary"]:
        story.append(paragraph(line))
    heading("Experience")
    for item in cv["experience"]:
        meta = f'{item["organization"]} | {item["start"]} - {item.get("end") or "Present"}'
        if item.get("location"):
            meta += f' | {item["location"]}'
        entry = [paragraph(item["title"], "title"), paragraph(meta, "meta")]
        for line in item.get("highlights", []):
            entry.append(paragraph("- " + line, "bullet"))
        entry.append(Spacer(1, 6))
        story.append(KeepTogether(entry))

    story.append(PageBreak())
    story.append(paragraph("Laurence Miao", "name"))
    story.append(paragraph("Education, technical skills & certifications", "role"))
    heading("Education")
    for item in cv["education"]:
        entry = [paragraph(item["title"], "title")]
        entry.append(paragraph(f'{item["organization"]} | {item["start"]} - {item.get("end") or "Present"}', "meta"))
        if item.get("area"):
            entry.append(paragraph(item["area"]))
        entry.append(Spacer(1, 7))
        story.append(KeepTogether(entry))
    heading("Technical skills")
    for skill in cv["skills"]:
        story.append(Paragraph(f'<b>{escape(skill["name"])}</b> - {escape(", ".join(skill["keywords"]))}', styles["body"]))
    heading("Certifications")
    for certificate in cv["certificates"]:
        story.append(paragraph(certificate["name"]))

    def decorate(canvas, document):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor(ACCENT))
        canvas.setLineWidth(2)
        canvas.line(44, letter[1] - 25, letter[0] - 44, letter[1] - 25)
        canvas.setFillColor(colors.HexColor(MUTED))
        canvas.setFont("Helvetica", 8)
        canvas.drawString(44, 24, "Laurence Miao | laurence-miao.github.io")
        canvas.drawRightString(letter[0] - 44, 24, str(document.page))
        canvas.restoreState()

    document = SimpleDocTemplate(str(destination), pagesize=letter, rightMargin=44, leftMargin=44, topMargin=43, bottomMargin=42, title="Laurence Miao - CV", author="Laurence Miao")
    document.build(story, onFirstPage=decorate, onLaterPages=decorate)
    print(destination)


def font(size, bold=False):
    candidates = (
        ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
        if bold else
        ["/System/Library/Fonts/Supplemental/Arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    )
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default(size=size)


def build_social_image():
    image = Image.new("RGB", (1200, 630), "#f7f5fa")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 14, 630), fill=ACCENT)
    draw.text((80, 88), "ENGINEERING & TECHNICAL LEADERSHIP", font=font(22, True), fill=ACCENT)
    draw.text((76, 170), "Laurence Miao", font=font(86, True), fill=TEXT)
    draw.text((80, 300), "AI/ML evaluation. Cloud architecture.", font=font(38), fill=TEXT)
    draw.text((80, 365), "Selected work, writing, and experience.", font=font(30), fill=MUTED)
    draw.line((80, 480, 1120, 480), fill="#d8c9e5", width=2)
    draw.text((80, 520), "laurence-miao.github.io", font=font(26), fill=ACCENT)
    destination = ROOT / "assets/img/social-card.png"
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, optimize=True)
    print(destination)


if __name__ == "__main__":
    build_cv()
    build_social_image()
