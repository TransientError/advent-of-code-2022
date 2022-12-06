import { readFileSync } from "fs";

const data = readFileSync('input.txt').toString();

let result: number;

for (let i = 0; i < data.length - 14; i++) {
  const window = data.slice(i, i + 14);

  if (new Set<string>(window).size === 14) {
    result = i + 14;
    console.log("result", result);
    console.log("window", window);
    break;
  }
}

