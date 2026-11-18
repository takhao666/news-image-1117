// News-image entry for 17 November 2026: the image is entry.png beside
// this file, and this program copies it to the grader's output directory.
// The grader runs it twice with no network; both runs write identical
// bytes because the file is copied byte for byte. Before copying, the
// program checks the image is really there and reports its size, so a
// missing or empty file fails loudly instead of handing the judge
// nothing.
//   Local run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
import { copyFileSync, mkdirSync, statSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, 'entry.png');
const target = join(outDir, 'entry.png');

const size = statSync(source).size;
if (size === 0) {
  throw new Error('entry.png is empty: nothing to hand the judge');
}
mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
process.stdout.write(`[entry] wrote ${target} (${size} bytes)\n`);
