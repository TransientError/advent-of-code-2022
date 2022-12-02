let fs = require('fs').promises;

console.log('hey there!');
const data = (await fs.readFile("input.txt")).toString().split('\n');

console.log(data);

let cur_elf = 1;
let cur_count = 0;
let cur_max = 0;
let max_elf: number;

for (const count of data) {
  if (count === "") {
    if (cur_count > cur_max) {
      cur_max = cur_count;
      max_elf = cur_elf;
    }
    cur_elf += 1;
    cur_count = 0;
  } else {
    cur_count += parseInt(count);
  }
}

console.log(max_elf, cur_max)

export {}

