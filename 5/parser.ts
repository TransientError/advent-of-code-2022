import { readFileSync } from "fs";

const data = readFileSync("input.txt").toString().split("\n");

let stacks = new Map<number, string[]>();

for (const line of data) {
  if (line && !line.startsWith("move") && !line.startsWith(" 1")) {
    for (let i = 1; i < line.length; i += 4) {
      const stack_index = Math.trunc(i / 4 + 1);
      const stack = stacks.get(stack_index) ?? [];
      if (line[i].trim()) {
        stack.push(line[i]);
        stacks.set(stack_index, stack);
      }
    }
  }
  if (line?.startsWith(" 1")) {
    for (const stack of stacks.values()) {
      stack.reverse();
    }
  }
}

console.log(stacks);
