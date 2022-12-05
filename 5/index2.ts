import { readFileSync } from "fs";

const data = readFileSync('input.txt').toString().split('\n');

const stacks: Map<number, string[]> = new Map([
  [1, ['B', 'G', 'S', 'C']],
  [2, ['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G']],
  [3, ['M', 'Q', 'S']],
  [4, ['B', 'S', 'L', 'T', 'W', 'N', 'M']],
  [5, ['J', 'Z', 'F', 'T', 'V', 'G', 'W', 'P']],
  [6, ['C', 'T', 'B', 'G', 'Q', 'H', 'S']],
  [7, ['T', 'J', 'P', 'B', 'W']],
  [8, ['G', 'D', 'C', 'Z', 'F', 'T', 'Q', 'M']],
  [9, ['N', 'S', 'H', 'B', 'P', 'F']],
]);

for (const line of data) {
  if (!line.startsWith('move')) {
    console.log("skipping", line);
    continue;
  }

  const words = line.split(' ');

  let how_many_to_move: number = parseInt(words[1]);
  const origin_stack_number: number = parseInt(words[3]);
  const destination_stack_number: number = parseInt(words[5]);

  let origin_stack = stacks.get(origin_stack_number);
  const destination_stack = stacks.get(destination_stack_number) ?? [];

  if (!origin_stack || !destination_stack) {
    if (!origin_stack) {
      console.error("stack dne", origin_stack_number);
    }
    if (!destination_stack) {
      console.error("stack dne", destination_stack_number);
    }
    process.exit(1);
  }

  const crates_to_stay: number = origin_stack.length - how_many_to_move;
  const to_move = origin_stack.slice(crates_to_stay)
  destination_stack.push(...to_move);
  origin_stack = origin_stack.slice(0, crates_to_stay);
  stacks.set(origin_stack_number, origin_stack);
}

let sln: string[] = [];
for (const [index, stack] of stacks.entries()) {
  const crate = stack.pop();
  if (!crate) {
    console.error("stack empty", index)
    process.exit(1);
  }
  sln.push(crate)
}

console.log(sln.join(''));


