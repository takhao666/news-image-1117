# The World in One Day — 17 November 2026

One image summing up the world news of Tuesday 17 November 2026, for the
make.fun `news-image-20261117` competition.

## The image

`entry.png` (1024×1024, PNG) is a newspaper-style infographic: a big
**17 NOVEMBER 2026** header, six story panels, and an "Also today" strip.

**The six stories** (all events of, or first reported on, 17 Nov 2026):

1. **Ukraine war — bridge war:** Ukraine badly damaged the Kerch Bridge to
   Crimea; Russia struck Kyiv's two Dnipro bridges overnight. (BBC)
2. **Middle East — Iran fires on US radar in Bahrain:** Iranian drones
   targeted a US radar at Sheikh Isa base; Bahrain said it intercepted them.
   US intelligence warned Iran weighed a "dirty bomb" plot in Washington.
   (Reuters / CNN)
3. **Gulf shipping — tankers hit by mines off Hormuz:** several oil tankers
   struck mines near the Strait of Hormuz and caught fire, as a third US
   carrier group arrived in the region. (Al Jazeera / Reuters)
4. **Asia diplomacy — Trump flies east for Xi–Putin talks:** Trump heads to
   Asia ahead of Thursday's Xi–Trump–Putin meeting in Shenzhen; US envoys
   Witkoff and Kushner head to Berlin the same day. (Outlook India / Axios)
5. **Asia-Pacific — Russian jets enter Japan's airspace:** Japan scrambled
   fighters and protested after two suspected Russian aircraft violated its
   airspace; South Korea and Taiwan also responded. (BBC)
6. **United States — Pentagon fails its 9th straight audit:** auditors again
   could not verify books covering $4.8 trillion in assets, though a record
   14 of 25 units passed. (Reuters)

**Also today:** Mongolia's president says he will resign; the UK sanctions
Israeli settlement builders; China and Canada agree tariff cuts.

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
