"""Compose the flat front cover (assets/cover/cover.png) from the author's figure and the AYOUNI logo.

The setting is the author's choice of 2026-11-24 (DECISIONS.md, COVER-02), after a study of published covers that carry one
object and a title: one column of type at the left, on a dark ground; the jar large, upright, cut by the right and bottom
edges. The faces are the book's own (assets/fonts: EB Garamond, Inter). Page 2194 x 2868, twice the logical 1097 x 1434.

The jar (assets/cover/source/jar.webp, 1024 x 1535, on a ground of 254 254 254) is cut out of its ground: the ground around
it and the two openings of its handles are made transparent, so that it stands on the cover's colour. Its painted pixels
are scaled and nothing else: never redrawn, regenerated or recoloured. The pixels of its outline that were mixed with the
white ground are unmixed, so that no pale fringe shows on a dark ground.

The back cover waits: its two lines are the author's to give, and its description is made of the book's own sentences.
The tagline of the title block opens it.

    python tools/make_cover.py
"""
import hashlib
import io
import sys
from pathlib import Path

import numpy as np
import yaml
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "cover" / "source"
FONTS = ROOT / "assets" / "fonts"
OUT = ROOT / "assets" / "cover" / "cover.png"
JAR_SHA256 = "88dde241d7b208784f304db2ca815a291e0b293e972a8c310a3486dec456253a"   # the file the author supplied
K = 2                                   # drawn at twice the logical 1097 x 1434
LW, LH = 1097, 1434
W, H = LW * K, LH * K

GROUND = (24, 26, 34)                   # the cover's dark ground
CREAM = (247, 241, 225)                 # the title, the author, the logo
OCHRE = (240, 160, 40)                  # the line under the title: the jar's own ochre
QUIET = (170, 165, 160)                 # the places and the year

LEFT = 84                               # logical px: the column of type
JAR_HEIGHT = 1250                       # logical px: the jar's height, cut by the foot of the page
JAR_CENTRE, JAR_TOP = 866, 452          # logical px: its axis and its top
PLACES = "TUNIS · NIAMEY · PARIS · 2026"

_FACES = {"garamond": "EBGaramond-normal.woff2", "garamond-i": "EBGaramond-italic.woff2", "inter": "Inter-normal.woff2"}
_fonts = {}


def font(name, size):
    key = (name, size)
    if key not in _fonts:
        data = (FONTS / _FACES[name]).read_bytes()
        _fonts[key] = ImageFont.truetype(io.BytesIO(data), round(size * K), layout_engine=ImageFont.Layout.RAQM)
    return _fonts[key]


def _advances(text, fnt):
    """Each letter's advance, with the face's own kerning toward the next letter."""
    return [fnt.getlength(c + text[i + 1]) - fnt.getlength(text[i + 1]) if i + 1 < len(text) else fnt.getlength(c)
            for i, c in enumerate(text)]


def text_width(text, fnt, tracking=0.0):
    if not tracking:
        return fnt.getlength(text)
    return sum(_advances(text, fnt)) + tracking * fnt.size * (len(text) - 1)


def draw_text(d, x, y, text, fnt, fill, tracking=0.0):
    """One line at logical x, y (its top left); returns its box in page pixels."""
    x0 = x * K
    if not tracking:
        d.text((x0, y * K), text, font=fnt, fill=fill)
        return d.textbbox((x0, y * K), text, font=fnt)
    start = x0
    for c, adv in zip(text, _advances(text, fnt)):
        d.text((x0, y * K), c, font=fnt, fill=fill)
        x0 += adv + tracking * fnt.size
    top, bottom = d.textbbox((start, y * K), text, font=fnt)[1::2]
    return (round(start), top, round(x0), bottom)


def wrap(text, fnt, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if fnt.getlength(t) <= maxw * K or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = word
    return lines + [cur]


def jar_cutout():
    """The author's figure as RGBA at its source size, its ground and the openings of its handles transparent."""
    path = SRC / "jar.webp"
    got = hashlib.sha256(path.read_bytes()).hexdigest()
    if got != JAR_SHA256:
        raise SystemExit(f"assets/cover/source/jar.webp is not the file the author supplied (sha256 {got})")
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    near = Image.fromarray(((a.min(axis=2) >= 240) * 255).astype(np.uint8), "L")
    work = near.copy()
    for seed in ((0, 0), (im.width - 1, 0), (0, im.height - 1), (im.width - 1, im.height - 1)):
        if work.getpixel(seed) == 255:
            ImageDraw.floodfill(work, seed, 128)
    wa = np.asarray(work)
    outside = wa == 128
    # the openings of the handles: the large near-white regions that the outline encloses
    rest = Image.fromarray(((wa == 255) * 255).astype(np.uint8), "L")
    ys, xs = np.nonzero(np.asarray(rest))
    holes, seen = np.zeros_like(outside), np.zeros_like(outside)
    for y, x in zip(ys[::997], xs[::997]):
        if seen[y, x]:
            continue
        probe = rest.copy()
        ImageDraw.floodfill(probe, (int(x), int(y)), 77)
        region = np.asarray(probe) == 77
        seen |= region
        if region.sum() > 6000:
            holes |= region
    clear = outside | holes
    # the outline's pixels beside the cleared ground were mixed with it: unmix them
    grown = np.asarray(Image.fromarray((clear * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))) > 0
    edge = grown & ~clear
    alpha = np.where(clear, 0.0, 1.0)
    alpha = np.where(edge, np.clip((250.0 - a.mean(axis=2)) / 190.0, 0.0, 1.0), alpha)
    rgb = a.astype(np.float32)
    unmixed = (rgb - 254.0 * (1.0 - alpha[..., None])) / np.maximum(alpha[..., None], 0.05)
    rgb = np.where(edge[..., None], np.clip(unmixed, 0, 255), rgb)
    rgb = np.where(clear[..., None], np.array([9.0, 1.0, 1.0]), rgb)        # scaling then bleeds the outline's ink, not white
    cut = Image.fromarray(np.dstack([rgb, alpha * 255.0]).astype(np.uint8), "RGBA")
    return cut.crop(cut.getbbox())


def jar_scaled(height):
    """The cut-out jar at a logical height, scaled with its transparency premultiplied, so that no fringe appears."""
    cut = jar_cutout()
    h = round(height * K)
    w = round(cut.width * h / cut.height)
    a = np.asarray(cut).astype(np.float32) / 255.0
    pre = np.dstack([a[..., :3] * a[..., 3:4], a[..., 3:4]])
    chans = [Image.fromarray((pre[..., i] * 255).astype(np.uint8), "L").resize((w, h), Image.LANCZOS) for i in range(4)]
    p = np.dstack([np.asarray(c).astype(np.float32) / 255.0 for c in chans])
    rgb = np.clip(p[..., :3] / np.maximum(p[..., 3:4], 1e-4), 0, 1)
    return Image.fromarray((np.dstack([rgb, p[..., 3:4]]) * 255).astype(np.uint8), "RGBA")


def logo(width, colour):
    im = Image.open(SRC / "ayouni-logo.png").convert("RGBA")
    im = im.crop(im.getbbox())
    im = im.resize((round(width * K), round(im.height * width * K / im.width)), Image.LANCZOS)
    mark = Image.new("RGBA", im.size, colour + (255,))
    mark.putalpha(im.split()[3])
    return mark


def make():
    st = yaml.safe_load((ROOT / "src" / "structure.yaml").read_text(encoding="utf-8"))
    cover = Image.new("RGBA", (W, H), GROUND + (255,))
    d = ImageDraw.Draw(cover)

    jar = jar_scaled(JAR_HEIGHT)
    jx, jy = round(JAR_CENTRE * K - jar.width / 2), JAR_TOP * K
    cover.alpha_composite(jar, (jx, jy))
    painted = Image.new("L", (W, H), 0)
    painted.paste(jar.split()[3], (jx, jy))

    cover.alpha_composite(logo(150, CREAM), (LEFT * K, 86 * K))
    boxes = [draw_text(d, LEFT - 4, 196, st["title"], font("garamond", 108), CREAM)]
    y = 346
    for line in wrap(st["subtitle"], font("garamond-i", 37), 620):
        boxes.append(draw_text(d, LEFT, y, line, font("garamond-i", 37), OCHRE))
        y += 47
    boxes.append(draw_text(d, LEFT, 1302, st["author"].upper(), font("inter", 26), CREAM, tracking=0.26))
    boxes.append(draw_text(d, LEFT, 1352, PLACES, font("inter", 14), QUIET, tracking=0.22))

    # no letter stands on the jar, and the title stays inside the page's margin
    margin = 14 * K
    for b in boxes:
        if b[2] > W - 60 * K:
            raise SystemExit(f"the cover: a line of type runs to {round(b[2] / K)} px, past the right margin")
        region = painted.crop((max(0, b[0] - margin), max(0, b[1] - margin), min(W, b[2] + margin), min(H, b[3] + margin)))
        if region.getbbox():
            raise SystemExit(f"the cover: a line of type at {tuple(round(v / K) for v in b)} px touches the jar")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    cover.convert("RGB").save(OUT)
    print("wrote", OUT, cover.size, f"the jar {jar.width} x {jar.height} at ({jx}, {jy}), cut by the right and bottom edges;",
          f"{len(boxes)} lines of type, none on the jar")


if __name__ == "__main__":
    sys.exit(make())
