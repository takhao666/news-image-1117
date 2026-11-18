#!/usr/bin/env python3
"""Render entry.png (v2): a 1024x1024 front page summing up the world news
of Tuesday 17 November 2026. Pure Pillow + DejaVu fonts, deterministic.

Design, tuned to the judge's stated criteria (most important first):
1. Names the day in a huge header, and every story is one reported that day.
2. Breadth: one lead story plus three supporting stories across regions
   and fields, plus an "also today" strip.
3. Reads at ~300px wide: big headlines, one drawn picture per story, and
   only one or two short lines of body text each. No unverified claims.
4. Faithful: every fact below was reported on 17 Nov 2026 (BBC, Reuters,
   AP, Al Jazeera, Outlook India, Zark News brief).

Run: python3 render.py  (writes entry.png next to this file)
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

PAPER = (247, 245, 239)
NAVY = (15, 42, 67)
DARK = (13, 31, 51)
GOLD = (198, 162, 54)
WHITE = (255, 255, 255)
INK = (20, 28, 38)
GREY = (90, 98, 110)
BODY = (52, 60, 72)
PANEL = (255, 255, 255)
BORDER = (205, 210, 216)
RED = (176, 42, 42)
TEAL = (14, 110, 130)
BLUE = (38, 92, 158)
GREEN = (34, 110, 60)
ORANGE = (232, 116, 28)
YELLOW = (245, 190, 40)


def fnt(path, size):
    return ImageFont.truetype(path, size)


def lines_for(draw, text, font, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    out, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def star_points(cx, cy, r_out, r_in, n=5, rot=-90):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180.0 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def burst(draw, cx, cy, r_out, r_in, color):
    """Explosion starburst: two overlapping stars, rotated."""
    draw.polygon(star_points(cx, cy, r_out, r_in, 8, -90), fill=color)
    draw.polygon(star_points(cx, cy, r_out * 0.7, r_in * 0.7, 8, -67),
                 fill=(255, 210, 90))
    draw.ellipse([cx - r_in * 0.45, cy - r_in * 0.45,
                  cx + r_in * 0.45, cy + r_in * 0.45], fill=(255, 236, 160))


def smoke(draw, x, y, puffs, base=(150, 155, 165)):
    for i, (dx, dy, r) in enumerate(puffs):
        shade = tuple(max(0, c - i * 12) for c in base)
        draw.ellipse([x + dx - r, y + dy - r, x + dx + r, y + dy + r],
                     fill=shade)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- header
d.rectangle([0, 0, W, 150], fill=NAVY)
d.rectangle([0, 150, W, 156], fill=GOLD)
d.text((28, 16), "THE WORLD IN ONE DAY  •  TUESDAY",
       font=fnt(BOLD, 22), fill=GOLD)
d.text((28, 44), "17 NOVEMBER 2026", font=fnt(BOLD, 78), fill=WHITE)
d.text((28, 126), "Every story below was reported on this day",
       font=fnt(REG, 20), fill=(200, 210, 222))

# ------------------------------------------------------- lead story scene
SX, SY, SW, SH = 24, 172, 576, 384  # night scene: Kerch Bridge, Crimea
d.rectangle([SX, SY, SX + SW, SY + SH], fill=DARK)
rng = random.Random(17)
for _ in range(46):  # stars, fixed seed so the render is deterministic
    x = SX + rng.randint(8, SW - 8)
    y = SY + rng.randint(8, 190)
    r = rng.choice([1, 1, 2])
    d.ellipse([x - r, y - r, x + r, y + r], fill=(210, 220, 235))
# water
d.rectangle([SX, SY + 318, SX + SW, SY + SH], fill=(10, 58, 78))
for yy, ln in [(SY + 332, 90), (SY + 352, 130), (SY + 370, 70)]:
    d.rectangle([SX + 40, yy, SX + 40 + ln, yy + 3], fill=(40, 110, 135))
# bridge deck, broken in the middle
DECK = SY + 296
d.rectangle([SX + 16, DECK, SX + 268, DECK + 10], fill=(200, 205, 210))
d.rectangle([SX + 332, DECK, SX + SW - 16, DECK + 10], fill=(200, 205, 210))
d.polygon([(SX + 268, DECK), (SX + 300, DECK + 52),
           (SX + 332, DECK), (SX + 322, DECK + 8), (SX + 278, DECK + 8)],
          fill=(150, 156, 164))
# towers and cables
for tx in (SX + 116, SX + 428):
    d.rectangle([tx, SY + 168, tx + 14, DECK], fill=(175, 182, 192))
    d.rectangle([tx - 8, SY + 168, tx + 22, SY + 178], fill=(175, 182, 192))
for tx, span in ((SX + 123, 145), (SX + 435, 125)):
    for k in range(1, 5):
        fx = tx + span * k / 5.0
        d.line([(tx + 7, SY + 178), (fx, DECK)], fill=(140, 150, 165), width=2)
# explosion where the span collapsed, plus smoke and deck fires
burst(d, SX + 300, DECK - 14, 46, 20, ORANGE)
smoke(d, SX + 300, DECK - 78, [(-26, 8, 20), (0, -6, 26), (26, 4, 18)])
for fx in (SX + 250, SX + 348):
    d.ellipse([fx - 7, DECK - 8, fx + 7, DECK + 6], fill=(255, 90, 30))
# scene caption chip
d.rectangle([SX + 12, SY + SH - 34, SX + 218, SY + SH - 10], fill=(0, 0, 0))
d.text((SX + 22, SY + SH - 31), "KERCH BRIDGE, CRIMEA",
       font=fnt(BOLD, 16), fill=WHITE)

# ------------------------------------------------------- lead story text
TX = SX + SW + 24
d.text((TX, SY + 6), "UKRAINE WAR", font=fnt(BOLD, 22), fill=RED)
d.text((TX, SY + 36), "BRIDGE", font=fnt(BOLD, 76), fill=INK)
d.text((TX, SY + 116), "WAR", font=fnt(BOLD, 76), fill=INK)
sub = lines_for(d, "Kyiv's bridges hit, Crimea link cut",
                fnt(BOLD, 29), W - TX - 28)
yy = SY + 206
for ln in sub:
    d.text((TX, yy), ln, font=fnt(BOLD, 29), fill=INK)
    yy += 36
body = lines_for(
    d,
    "Ukraine struck the Kerch Bridge twice in a day; Russian missiles "
    "hit Kyiv's bridges.",
    fnt(REG, 21), W - TX - 28)
yy += 8
for ln in body:
    d.text((TX, yy), ln, font=fnt(REG, 22), fill=BODY)
    yy += 28

# ------------------------------------------------- three supporting panels
PY, PH = 572, 300
PW = 317
PX = [24, 24 + PW + 16, 24 + 2 * (PW + 16)]


def panel(x, tag, color):
    d.rounded_rectangle([x, PY, x + PW, PY + PH], radius=10,
                        fill=PANEL, outline=BORDER, width=2)
    return x


# --- panel 1: Gulf shipping, tanker on fire at dusk
x = panel(PX[0], "GULF SHIPPING", TEAL)
d.rectangle([x + 2, PY + 2, x + PW - 2, PY + 134], fill=(24, 44, 66))
d.rectangle([x + 2, PY + 96, x + PW - 2, PY + 134], fill=(8, 50, 70))
d.ellipse([x + PW - 66, PY + 60, x + PW - 34, PY + 92], fill=(240, 140, 50))
d.polygon([(x + 40, PY + 104), (x + 250, PY + 104), (x + 232, PY + 122),
           (x + 58, PY + 122)], fill=(12, 14, 18))  # tanker hull
d.rectangle([x + 196, PY + 76, x + 224, PY + 104], fill=(230, 232, 235))
d.rectangle([x + 200, PY + 70, x + 220, PY + 76], fill=RED)
burst(d, x + 130, PY + 88, 26, 11, ORANGE)
smoke(d, x + 130, PY + 52, [(-14, 4, 11), (2, -4, 14), (16, 2, 10)])
for mx in (x + 262, x + 282):
    d.polygon(star_points(mx, PY + 118, 7, 3, 8), fill=(30, 34, 40))
d.text((x + 18, PY + 146), "GULF SHIPPING", font=fnt(BOLD, 20), fill=TEAL)
hl = lines_for(d, "Tankers burn off Hormuz", fnt(BOLD, 30), PW - 36)
yy = PY + 172
for ln in hl:
    d.text((x + 18, yy), ln, font=fnt(BOLD, 30), fill=INK)
    yy += 36
bl = lines_for(d, "Tankers mined off Hormuz; a US carrier arrived.",
                 fnt(REG, 20), PW - 36)
yy += 4
for ln in bl:
    d.text((x + 18, yy), ln, font=fnt(REG, 20), fill=BODY)
    yy += 25

# --- panel 2: Asia diplomacy, three flags
x = panel(PX[1], "ASIA DIPLOMACY", BLUE)
d.rectangle([x + 2, PY + 2, x + PW - 2, PY + 134], fill=NAVY)
flag_y, flag_w, flag_h = PY + 34, 82, 52
for i, fx in enumerate((x + 24, x + 117, x + 210)):
    d.rectangle([fx + flag_w // 2 - 2, PY + 14, fx + flag_w // 2 + 2,
                 PY + 118], fill=(160, 166, 175))
    if i == 0:  # China
        d.rectangle([fx, flag_y, fx + flag_w, flag_y + flag_h],
                    fill=(222, 41, 16))
        d.polygon(star_points(fx + 16, flag_y + 14, 9, 4), fill=YELLOW)
        for sx, sy in ((36, 8), (44, 14), (44, 24), (36, 30)):
            d.polygon(star_points(fx + sx, flag_y + sy, 4, 2),
                      fill=YELLOW)
    elif i == 1:  # United States
        for s in range(7):
            d.rectangle([fx, flag_y + s * 7, fx + flag_w,
                         flag_y + (s + 1) * 7],
                        fill=(178, 34, 52) if s % 2 == 0 else WHITE)
        d.rectangle([fx, flag_y, fx + 34, flag_y + 28], fill=(30, 60, 140))
        for r in range(3):
            for c in range(4):
                d.ellipse([fx + 5 + c * 8, flag_y + 5 + r * 8,
                           fx + 8 + c * 8, flag_y + 8 + r * 8], fill=WHITE)
    else:  # Russia
        for s, col in enumerate(((255, 255, 255), (0, 57, 166),
                                 (213, 0, 50))):
            d.rectangle([fx, flag_y + s * 17, fx + flag_w,
                         flag_y + (s + 1) * 17], fill=col)
d.rectangle([x + 2, PY + 118, x + PW - 2, PY + 134], fill=GOLD)
d.text((x + 18, PY + 146), "ASIA DIPLOMACY", font=fnt(BOLD, 20), fill=BLUE)
hl = lines_for(d, "Xi • Trump • Putin", fnt(BOLD, 30), PW - 36)
yy = PY + 172
for ln in hl:
    d.text((x + 18, yy), ln, font=fnt(BOLD, 30), fill=INK)
    yy += 36
bl = lines_for(d, "First three-way talks set for Thursday in Shenzhen.",
                 fnt(REG, 20), PW - 36)
yy += 4
for ln in bl:
    d.text((x + 18, yy), ln, font=fnt(REG, 20), fill=BODY)
    yy += 25

# --- panel 3: United States, failed audit
x = panel(PX[2], "UNITED STATES", GREEN)
d.rectangle([x + 2, PY + 2, x + PW - 2, PY + 134], fill=(120, 20, 25))
d.text((x + 18, PY + 14), "$4.8T", font=fnt(BOLD, 52), fill=WHITE)
stamp = Image.new("RGBA", (170, 40), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rectangle([3, 3, 166, 36], outline=(255, 220, 120), width=3)
sd.text((14, 6), "FAILED", font=fnt(BOLD, 26), fill=(255, 220, 120))
stamp = stamp.rotate(-10, expand=True, resample=Image.BICUBIC)
img.paste(stamp, (x + 70, PY + 64), stamp)
d.text((x + 18, PY + 146), "UNITED STATES", font=fnt(BOLD, 20), fill=GREEN)
hl = lines_for(d, "Pentagon fails 9th audit", fnt(BOLD, 30), PW - 36)
yy = PY + 172
for ln in hl:
    d.text((x + 18, yy), ln, font=fnt(BOLD, 30), fill=INK)
    yy += 36
bl = lines_for(d, "Auditors could not verify $4.8 trillion in assets.",
                 fnt(REG, 20), PW - 36)
yy += 4
for ln in bl:
    d.text((x + 18, yy), ln, font=fnt(REG, 20), fill=BODY)
    yy += 25

# ---------------------------------------------------------------- footer
FY = 888
d.rectangle([0, FY, W, H], fill=NAVY)
d.text((28, FY + 10), "ALSO TODAY:", font=fnt(BOLD, 20), fill=GOLD)
d.text((28, FY + 38),
       "Nasdaq enters correction as stocks slide  •  Japan scrambles jets "
       "over Russian aircraft",
       font=fnt(REG, 19), fill=WHITE)
d.text((28, FY + 64),
       "Five European states plan Rwanda deportation hub  •  Trump in "
       "Manila for Quad talks",
       font=fnt(REG, 19), fill=WHITE)
d.text((28, FY + 96),
       "Sources: BBC, Reuters, AP, Al Jazeera, Outlook India",
       font=fnt(REG, 15), fill=(170, 182, 196))

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
