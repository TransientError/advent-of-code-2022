import { readFileSync } from "fs";

const data = readFileSync("input.txt").toString().split("\n");

const toPair = (s: string): [number, number] => {
  const range = s.split('-');
  return [parseInt(range[0]), parseInt(range[1])];
};

let fully_redundant_pairs = 0;
for (const line of data) {
  if (line) {
    const pairs = line.split(",");
    const [left_start, left_end] = toPair(pairs[0]);
    const [right_start, right_end] = toPair(pairs[1]);
  
    if (left_start <= right_start && left_end >= right_end) {
      fully_redundant_pairs += 1;
      console.log("found pairs:", line)
      continue;
    } else if (right_start <= left_start && left_end <= right_end) {
      fully_redundant_pairs += 1;
      console.log("found pairs:", line)
      continue;
    }
  }
}

console.log("total pairs", fully_redundant_pairs);
