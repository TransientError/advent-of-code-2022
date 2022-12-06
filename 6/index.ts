import { readFileSync } from "fs";

const data = readFileSync('input.txt').toString();

let result: number;

for (let i = 0; i < data.length - 4; i++) {
  const window = data.slice(i, i + 4);

  if (new Set<string>(window).size === 4) {
    result = i + 4;
    console.log("result", result);
    console.log("window", window);
    break;
  }
}



