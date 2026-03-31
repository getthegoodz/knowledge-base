import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { execFileSync } from 'child_process';

const [, , input, output] = process.argv;
if (!input) {
  console.error('Usage: node extract.mjs <input.pdf> [output.txt]');
  process.exit(1);
}
const here = path.dirname(fileURLToPath(import.meta.url));
const cli = path.join(here, 'node_modules/.bin/pdf-parse');
const result = execFileSync(cli, ['text', input, '--format', 'text'], { encoding: 'utf8' });
if (output) {
  fs.mkdirSync(path.dirname(output), { recursive: true });
  fs.writeFileSync(output, result);
} else {
  process.stdout.write(result);
}
