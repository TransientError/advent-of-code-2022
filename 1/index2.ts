import { readFile } from 'fs/promises'

const data: string[] = (await readFile("input.txt")).toString().split("\n");

let cur_elf = 1;
let cur_count = 0;
let cal_map = new Map<number, number>();

for (const count of data) {
  if (count === "") {
    cal_map.set(cur_elf, cur_count);
    cur_elf += 1;
    cur_count = 0;
  } else {
    cur_count += parseInt(count);
  }
}

let counts = Array.from(cal_map.values());

counts.sort((a, b) => a - b);

let top_three = counts.slice(-3)

let sln = top_three.reduce((accumulator, value) => accumulator + value, 0)

console.log(sln)
