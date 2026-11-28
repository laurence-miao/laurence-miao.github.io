"""Build the social preview image from the site's existing content."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ACCENT = "#99178c"
TEXT = "#20212a"
MUTED = "#58616f"


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
    build_social_image()
