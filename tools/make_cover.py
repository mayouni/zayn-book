"""Compose the flat front cover (assets/cover/cover.png) from the author's figure and the AYOUNI logo.

Lineage: the Softanza book's tools/make_cover.py (softanza-book a9e3812), function `make`: the series' one design, a pure
white page 2194 x 2868 (twice the logical 1097 x 1434), the AYOUNI logo top left, the title block on the left, one figure
in the patchwork style on the right, the author bottom left, the cities and the year bottom right. Same positions, same
faces, same sizes. Changed: the figure is the painted jar the author supplied for this book.

The jar (assets/cover/source/jar.webp, 1024 x 1535, on a ground of 254 254 254) is cropped to its bounding box and
scaled, and nothing else: it is never redrawn, regenerated, recoloured or extended. Its pixels are pasted as they are;
the one step between the figure's ground (254) and the page (255) is below what a screen or a press shows.

The back cover waits: its two lines are the author's to give, and its description is made of the book's own sentences,
which this book does not hold before its chapters are read. `make_back` of the Softanza tool is taken then.

    python tools/make_cover.py
"""
import hashlib
import sys
from pathlib import Path

import yaml
from PIL import Image, ImageChops, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "cover" / "source"
OUT = ROOT / "assets" / "cover" / "cover.png"
JAR_SHA256 = "88dde241d7b208784f304db2ca815a291e0b293e972a8c310a3486dec456253a"   # the file the author supplied
K = 2                                   # drawn at twice the logical 1097 x 1434
W, H = 1097 * K, 1434 * K
PAPER = (255, 255, 255)
INK = (20, 20, 20)
GREY = (110, 110, 106)
FONTS = Path("C:/Windows/Fonts")
JAR_HEIGHT = 868                        # logical px: the jar's height on the page
JAR_RIGHT = 56                          # logical px between the jar and the page's right edge
JAR_BOTTOM = 1290                       # logical px: the jar's foot


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size * K)


def logo_png(width):
    im = Image.open(SRC / "ayouni-logo.png").convert("RGBA")
    im = im.crop(im.getbbox())
    return im.resize((width * K, round(im.height * width * K / im.width)), Image.LANCZOS)


def wrap(draw, text, fnt, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if draw.textlength(t, font=fnt) <= maxw * K or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = word
    return lines + [cur]


def jar():
    """The author's figure, cropped to its bounding box on its own ground and scaled. No pixel is repainted."""
    path = SRC / "jar.webp"
    got = hashlib.sha256(path.read_bytes()).hexdigest()
    if got != JAR_SHA256:
        raise SystemExit(f"assets/cover/source/jar.webp is not the file the author supplied (sha256 {got})")
    im = Image.open(path).convert("RGB")
    ground = im.getpixel((0, 0))
    diff = ImageChops.difference(im, Image.new("RGB", im.size, ground)).convert("L")
    box = diff.point(lambda p: 255 if p > 12 else 0).getbbox()
    box = (max(0, box[0] - 6), max(0, box[1] - 6), min(im.width, box[2] + 6), min(im.height, box[3] + 6))
    im = im.crop(box)
    h = JAR_HEIGHT * K
    return im.resize((round(im.width * h / im.height), h), Image.LANCZOS), box


def make():
    st = yaml.safe_load((ROOT / "src" / "structure.yaml").read_text(encoding="utf-8"))
    cover = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(cover)

    figure, box = jar()
    fx, fy = W - JAR_RIGHT * K - figure.width, JAR_BOTTOM * K - figure.height
    cover.paste(figure, (fx, fy))

    logo = logo_png(232)
    cover.paste(logo, (80 * K, 92 * K), logo)

    x = 80 * K
    d.text((x, 232 * K), st["title"], font=font("arial.ttf", 112), fill=INK)
    y = 400 * K
    text_right = 0
    for line in wrap(d, st["subtitle"], font("arial.ttf", 46), 400):
        d.text((x, y), line, font=font("arial.ttf", 46), fill=INK)
        text_right = max(text_right, x + d.textlength(line, font=font("arial.ttf", 46)))
        y += 58 * K
    y += 26 * K
    ital = font("georgiai.ttf", 31)
    for line in wrap(d, st["tagline"], ital, 390):
        d.text((x, y), line, font=ital, fill=INK)
        text_right = max(text_right, x + d.textlength(line, font=ital))
        y += 46 * K
    if text_right + 16 * K > fx:
        raise SystemExit(f"the cover: the title block ({round(text_right / K)} px) runs into the figure ({round(fx / K)} px)")

    d.text((x, 1366 * K), "MANSOUR AYOUNI", font=font("arialbd.ttf", 28), fill=INK)
    right = "TUNIS \u00b7 NIAMEY \u00b7 PARIS \u00b7 2026"
    f = font("arial.ttf", 26)
    d.text((W - 80 * K - d.textlength(right, font=f), 1368 * K), right, font=f, fill=GREY)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    cover.save(OUT)
    print("wrote", OUT, cover.size, f"jar cropped to {box}, drawn {figure.width} x {figure.height} at ({fx}, {fy});",
          f"title block ends at {round(text_right / K)} px, the figure starts at {round(fx / K)} px (logical)")


if __name__ == "__main__":
    sys.exit(make())
