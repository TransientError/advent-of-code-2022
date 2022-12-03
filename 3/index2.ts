import { readFileSync } from 'fs';
import { chunk } from 'lodash';

const data = readFileSync("input.txt").toString().split('\n').slice(0, -1);

const toPriority = (s: string) =>
  s === s.toUpperCase() ? s.charCodeAt(0) - 38 : s.charCodeAt(0) - 96;

const groups = chunk(data, 3);

let total = 0;
for (const group of groups) {
  let items_1 = new Set<string>(group[0].split(''));
  let items_2 = new Set<string>(group[1].split(''));

  let badge = group[2].split('').find((e) => items_1.has(e) && items_2.has(e));

  if (badge === undefined) {
    console.log("no badge found");
    process.exit(1);
  } else {
    console.log("badge", badge);
  }

  const priority = toPriority(badge)

  console.log("priority ", priority)
  total += priority;
}

console.log("total ", total)
