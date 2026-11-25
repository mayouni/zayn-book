"""Compose the flat front cover (assets/cover/cover.png) from the author's figure and the AYOUNI logo.

The setting is the author's choice of 2026-11-24 (DECISIONS.md, COVER-02), after a study of published covers that carry one
object and a title: one column of type at the left, on a dark ground; the jar large, upright, cut by the right and bottom
edges. The faces are the book's own (assets/fonts: EB Garamond, Inter). Page 2194 x 2868, twice the logical 1097 x 1434.

The jar (assets/cover/source/jar.webp, 1024 x 1535, on a ground of 254 254 254) is cut out of its ground: the ground around
it and the two openings of its handles are made transparent, so that it stands on the cover's colour. Its painted pixels
are scaled and nothing else: never redrawn, regenerated or recoloured. The pixels of its outline that were mixed with the
white ground are unmixed, so that no pale fringe shows on a dark ground.

The back (assets/cover/back.png) is drawn on the same ground, in the same faces and on the same column (BACK-01). The tagline
of the title block opens it (TITLE-02), alone, as the author ruled; its description is made of the book's own
sentences (src/structure.yaml, back_*), never new prose; then the author, the imprint, the free reader's address with its QR
code (decoded and checked), the shelf and the licence. It fails rather than let two blocks touch.

    python tools/make_cover.py                      the front and the back
    python tools/make_cover.py --back-lines DIR     one back for each candidate second line (back_line_candidates), if any
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


BACK = ROOT / "assets" / "cover" / "back.png"
DIM = (206, 200, 188)                   # the back's body text: the cream, one step quieter, so that the bold reads
RULE = (70, 72, 82)                     # the hairline above the imprint
BODY_SIZES = (27, 26, 25, 24, 23, 22)   # logical px: the description takes the largest that fits every candidate line


def spaced_lines(d, x, y, text, fnt, fill, tracking, maxw):
    """Small capitals tracked, wrapped to maxw; returns the y under the last line."""
    words, line = text.split(), ""
    for w in words:
        t = (line + " " + w).strip()
        if text_width(t, fnt, tracking) <= maxw * K or not line:
            line = t
        else:
            draw_text(d, x, y, line, fnt, fill, tracking)
            y += round(fnt.size / K * 1.55)
            line = w
    draw_text(d, x, y, line, fnt, fill, tracking)
    return y + round(fnt.size / K * 1.55)


def rich(d, x, y, text, size, maxw, fill, bold_fill, lead=1.45, write=True):
    """A paragraph with **bold** runs, wrapped to maxw at logical size; the bold is the face thickened, as the reader does.
    Returns the y under it."""
    fnt = font("garamond", size)
    runs, bold = [], False
    for part in text.split("**"):
        runs += [(w, bold) for w in part.split()]
        bold = not bold
    space = fnt.getlength(" ")
    lines, cur, width = [], [], 0.0
    for w, b in runs:
        wl = fnt.getlength(w) + (2 if b else 0)
        if cur and width + space + wl > maxw * K:
            lines.append(cur)
            cur, width = [], 0.0
        width += (space if cur else 0) + wl
        cur.append((w, b))
    lines.append(cur)
    for ln in lines:
        x0 = x * K
        for i, (w, b) in enumerate(ln):
            if write:
                d.text((x0, y * K), w, font=fnt, fill=bold_fill if b else fill, stroke_width=1 if b else 0,
                       stroke_fill=bold_fill if b else None)
            x0 += fnt.getlength(w) + (2 if b else 0) + space
        y += round(size * lead)
    return y


def qr_code(url, size):
    """The free reader's address as a QR code, module by module, dark on cream with its quiet zone, then read back."""
    import cv2
    import segno
    q = segno.make(url, error="m", micro=False)
    m = [list(r) for r in q.matrix]
    n, quiet = len(m), 4
    cell = (size * K) // (n + 2 * quiet)
    im = Image.new("RGB", (cell * (n + 2 * quiet),) * 2, CREAM)
    dq = ImageDraw.Draw(im)
    for r, row in enumerate(m):
        for c, v in enumerate(row):
            if v:
                x0, y0 = (c + quiet) * cell, (r + quiet) * cell
                dq.rectangle((x0, y0, x0 + cell - 1, y0 + cell - 1), fill=GROUND)
    got, _, _ = cv2.QRCodeDetector().detectAndDecode(np.asarray(im.convert("L")))
    if got != url:
        raise SystemExit(f"the back cover: the QR code reads {got!r}, not {url!r}")
    return im


def portrait(size):
    """The author's portrait (assets/cover/source/author.png, from his own press material) as a disc, never enlarged."""
    ph = Image.open(SRC / "author.png").convert("RGB")
    side = min(ph.size)
    px = round(size * K)
    if px > side:
        raise SystemExit(f"the back cover: the portrait would be enlarged ({side} px to {px} px)")
    ph = ph.crop(((ph.width - side) // 2, (ph.height - side) // 2, (ph.width + side) // 2, (ph.height + side) // 2))
    ph = ph.resize((px, px), Image.LANCZOS)
    big = Image.new("L", (px * 4, px * 4), 0)
    ImageDraw.Draw(big).ellipse((0, 0, px * 4 - 1, px * 4 - 1), fill=255)
    return ph, big.resize((px, px), Image.LANCZOS)


def facts(text):
    """{{n:key}} in a back cover's text, read from the book's last run (data/book-run.json): no count is typed."""
    import json
    import re
    law = json.loads((ROOT / "data" / "book-run.json").read_text(encoding="utf-8"))["run"]["law"]

    def one(m):
        if m.group(1) not in law:
            raise SystemExit(f"the back cover names {m.group(1)}, which data/book-run.json does not hold")
        return str(law[m.group(1)])
    return re.sub(r"\{\{n:([\w.]+)\}\}", one, text)


def make_back(st, line, out, body, write=True):
    """The back cover with `line` as the author's second line, its description at `body` px, written to `out`; returns
    the free space above the author (negative: it overflows)."""
    back = Image.new("RGB", (W, H), GROUND)
    d = ImageDraw.Draw(back)
    right = LW - LEFT
    tw = right - LEFT

    y = spaced_lines(d, LEFT, 72, f"{st['title']} · {st['subtitle']}".upper(), font("inter", 14), QUIET, 0.16, tw)
    y += 16
    for sentence in st["tagline"].replace(". ", ".\n").split("\n"):
        draw_text(d, LEFT - 3, y, sentence, font("garamond", 60), CREAM)
        y += 70
    y += 8
    for ln in (wrap(line, font("garamond-i", 30), tw) if line else []):
        draw_text(d, LEFT, y, ln, font("garamond-i", 30), OCHRE)
        y += 39
    y += 22 if line else 14
    d.rectangle((LEFT * K, y * K, (LEFT + 64) * K, (y + 4) * K), fill=OCHRE)
    y += 34

    for para in st["back_blurb"]:
        if para.startswith("## "):
            y += 6
            draw_text(d, LEFT, y, para[3:].upper(), font("inter", 14), OCHRE, tracking=0.16)
            y += 30
        else:
            y = rich(d, LEFT, y, facts(para), body, tw, DIM, CREAM) + round(body / 2)
    draw_text(d, LEFT, y + 2, st["back_runs"], font("inter", 17), CREAM)
    end_blurb = y + 30

    band = 1176                                     # the hairline above the imprint
    top = band - 186                                # the author's block
    if not write or end_blurb > top - 24:
        return top - 24 - end_blurb
    ph, mask = portrait(118)
    back.paste(ph, (LEFT * K, top * K), mask)
    tx = LEFT + 118 + 30
    draw_text(d, tx, top + 4, st["author"].upper(), font("inter", 16), CREAM, tracking=0.2)
    note_end = rich(d, tx, top + 36, st["back_author_note"], 18, right - tx, DIM, CREAM, lead=1.42)
    if note_end > band - 16:
        raise SystemExit(f"the back cover: the author's note runs into the imprint ({note_end - (band - 16)} px too long)")

    d.rectangle((LEFT * K, band * K, right * K, band * K + 1), fill=RULE)
    lg = logo(150, CREAM)
    back.paste(lg, (LEFT * K, (band + 34) * K), lg)
    draw_text(d, LEFT, band + 34 + round(lg.height / K) + 16, st["series"].upper(), font("inter", 14), QUIET, tracking=0.2)

    qr = qr_code(st["back_url"], 140)
    back.paste(qr, (right * K - qr.width, (band + 22) * K))
    host, path = st["back_url"].split("://", 1)[1].split("/", 2)[0:2], st["back_url"].split("://", 1)[1].split("/", 2)[2]
    qx = right - round(qr.width / K) - 22
    f1, f2 = font("inter", 19), font("inter", 15)
    for i, (s, f, c) in enumerate(((st["back_free"], f1, CREAM), ("/".join(host) + "/", f2, QUIET), (path, f2, QUIET))):
        draw_text(d, qx - round(f.getlength(s) / K), band + 40 + (0, 36, 60)[i], s, f, c)

    foot = 1378
    fc = font("inter", 14)
    cat = st["back_category"].upper()
    lic = st["back_licence"].upper()
    draw_text(d, LEFT, foot, cat, fc, QUIET, tracking=0.12)
    lw = text_width(lic, fc, 0.12) / K
    draw_text(d, right - round(lw), foot, lic, fc, QUIET, tracking=0.12)
    if LEFT + text_width(cat, fc, 0.12) / K > right - lw - 30:
        raise SystemExit("the back cover: the shelf and the licence touch")

    out.parent.mkdir(parents=True, exist_ok=True)
    back.save(out)
    print("wrote", out, back.size, f"body {body} px, {top - 24 - end_blurb} px free above the author")
    return top - 24 - end_blurb


def make_backs(st, out_dir=None):
    """One description size for every candidate line, the largest at which each fits, so that the backs compare."""
    lines = st.get("back_line_candidates") or [st.get("back_line", "")]
    for body in BODY_SIZES:
        if all(make_back(st, ln, None, body, write=False) >= 0 for ln in lines):
            break
    else:
        raise SystemExit(f"the back cover's description does not fit at {BODY_SIZES[-1]} px: shorten it in src/structure.yaml")
    if out_dir is None:
        make_back(st, st["back_line"], BACK, body)
        return
    for i, line in enumerate(lines, 1):
        make_back(st, line, Path(out_dir) / f"back-{i}.png", body)


if __name__ == "__main__":
    if "--back-lines" in sys.argv:
        st = yaml.safe_load((ROOT / "src" / "structure.yaml").read_text(encoding="utf-8"))
        sys.exit(make_backs(st, sys.argv[sys.argv.index("--back-lines") + 1]))
    make()
    sys.exit(make_backs(yaml.safe_load((ROOT / "src" / "structure.yaml").read_text(encoding="utf-8"))))
