# news-image-1117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/takhao666/news-image-1117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/takhao666/news-image-1117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image summing up the world news of Tuesday 17 November 2026, for the make.fun `news-image-20261117` competition.

## The image

`entry.png` (1024×1024, PNG) is a newspaper front page: a big
**17 NOVEMBER 2026** header, one illustrated lead story, three more
illustrated stories, and an "Also today" strip. Every story was reported
on 17 November 2026, and each one has a picture, not just words, so the
day reads even at small size.

**The stories:**

1. **Lead — Ukraine war, bridge war:** Ukraine struck the Kerch Bridge
   to Crimea twice in one day; Russian missiles hit Kyiv's two bridges
   over the Dnipro. (BBC / Al Jazeera)
2. **Gulf shipping — tankers burn off Hormuz:** mines hit tankers near
   the Strait of Hormuz; a third US carrier group arrived in the region.
   (Al Jazeera / Reuters)
3. **Asia diplomacy — Xi • Trump • Putin:** the first three-way meeting
   of the three leaders is set for Thursday in Shenzhen, on the sidelines
   of APEC. (Outlook India)
4. **United States — Pentagon fails its 9th straight audit:** auditors
   could not verify books covering $4.8 trillion in assets. (Reuters)

**Also today:** the Nasdaq entered correction territory as stocks slid;
Japan scrambled fighters over suspected Russian aircraft; five European
states plan a Rwanda deportation hub; Trump in Manila for Quad talks.

## How it was made

`render.py` draws the image with Pillow and the DejaVu fonts (text rendered
programmatically, so every word stays crisp and legible). Re-run it to
regenerate `entry.png`:

```sh
python3 render.py
```

## The program

`main.ts` (Node 22, standard library only) copies `entry.png` to the
grader's output directory. It runs with no network and both runs write
identical bytes:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=hvn9m3q0&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
