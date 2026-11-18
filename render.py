#!/usr/bin/env python3
"""Render entry.png: a 1024x1024 infographic summing up the world news of
Tuesday 17 November 2026. Pure Pillow + DejaVu fonts; deterministic output.
Run: python3 render.py  (writes entry.png next to this file)
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

PAPER = (247, 245, 239)
NAVY = (15, 42, 67)
WHITE = (255, 255, 255)
INK = (20, 28, 38)
GREY = (90, 98, 110)
PANEL = (255, 255, 255)
BORDER = (205, 210, 216)

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- header ----
d.rectangle([0, 0, W, 168], fill=NAVY)
d.rectangle([0, 168, W, 174], fill=(198, 162, 54))  # gold rule
d.text((28, 22), "THE WORLD IN ONE DAY  •  TUESDAY",
       font=font(BOLD, 22), fill=(198, 162, 54))
d.text((28, 52), "17 NOVEMBER 2026",
       font=font(BOLD, 88), fill=WHITE)
d.text((28, 138), "Six stories that defined the day — from Kyiv to Bahrain",
       font=font(REG, 22), fill=(200, 210, 222))

# ---- story panels: 2 cols x 3 rows ----
stories = [
    ("UKRAINE WAR", (176, 42, 42),
     "Bridge war: Kyiv and Crimea hit",
     "Ukraine badly damaged the Kerch Bridge to Crimea; Russia struck "
     "Kyiv's two bridges over the Dnipro overnight."),
    ("MIDDLE EAST", (146, 90, 16),
     "Iran fires on US radar in Bahrain",
     "Iranian drones targeted a US radar at Sheikh Isa base; Bahrain said "
     "it intercepted them. US intel warns of an Iranian "
     "\u201cdirty bomb\u201d plot in Washington."),
    ("GULF SHIPPING", (14, 110, 130),
     "Tankers hit by mines off Hormuz",
     "Several oil tankers struck mines near the Strait of Hormuz and "
     "caught fire, Iran's navy said, as a third US carrier group "
     "arrived in the region."),
    ("ASIA DIPLOMACY", (38, 92, 158),
     "Trump flies east for Xi\u2013Putin talks",
     "Trump heads to Asia ahead of Thursday's Xi\u2013Trump\u2013Putin "
     "meeting in Shenzhen; US envoys Witkoff and Kushner head to "
     "Berlin the same day."),
    ("ASIA-PACIFIC", (96, 64, 150),
     "Russian jets enter Japan's airspace",
     "Japan scrambled fighters and protested after two suspected Russian "
     "aircraft violated its airspace; South Korea and Taiwan also "
     "responded."),
    ("UNITED STATES", (34, 110, 60),
     "Pentagon fails its 9th straight audit",
     "Auditors again could not verify the Pentagon's books, covering "
     "$4.8 trillion in assets — though a record 14 of its 25 units "
     "passed."),
]

MX, MY = 24, 190
GAP = 16
PW = (W - 2 * MX - GAP) // 2          # 480
PH = 236
for i, (tag, color, head, body) in enumerate(stories):
    x = MX + (i % 2) * (PW + GAP)
    y = MY + (i // 2) * (PH + GAP)
    d.rounded_rectangle([x, y, x + PW, y + PH], radius=10,
                        fill=PANEL, outline=BORDER, width=2)
    d.rectangle([x + 12, y, x + PW - 12, y + 7], fill=color)
    d.text((x + 18, y + 18), tag, font=font(BOLD, 20), fill=color)
    hl = wrap(d, head, font(BOLD, 29), PW - 36)
    hy = y + 48
    for line in hl:
        d.text((x + 18, hy), line, font=font(BOLD, 29), fill=INK)
        hy += 35
    bl = wrap(d, body, font(REG, 21), PW - 36)
    by = hy + 6
    for line in bl:
        d.text((x + 18, by), line, font=font(REG, 21), fill=(52, 60, 72))
        by += 27

# ---- footer: also today + sources ----
fy = MY + 3 * PH + 2 * GAP   # 930; band runs to 1024 (94 px)
d.rectangle([0, fy, W, H], fill=NAVY)
d.text((28, fy + 8), "ALSO TODAY:",
       font=font(BOLD, 20), fill=(198, 162, 54))
d.text((28, fy + 34),
       "Mongolia's president to resign  •  UK sanctions settlement "
       "builders  •  China–Canada tariff cuts",
       font=font(REG, 19), fill=WHITE)
d.text((28, fy + 62),
       "Reported 17 Nov 2026  •  Sources: BBC, Reuters, CNN, AP, Al Jazeera",
       font=font(REG, 16), fill=(170, 182, 196))

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
