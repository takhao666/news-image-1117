// News-image entry for 17 November 2026: the image is entry.png beside
// this file, and this program copies it to the grader's output directory.
// The grader runs it twice with no network; both runs write identical
// bytes because the file is copied byte for byte.
//   Local run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const here = dirname(fileURLToPath(import.meta.url));
copyFileSync(join(here, 'entry.png'), join(outDir, 'entry.png'));
