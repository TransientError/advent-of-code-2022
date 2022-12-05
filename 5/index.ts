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

  console.log(how_many_to_move, origin_stack_number, destination_stack_number);

  while (how_many_to_move > 0) {
    const origin_stack = stacks.get(origin_stack_number);
    const destination_stack = stacks.get(destination_stack_number);

    const crate = origin_stack.pop();
    if (crate == undefined) {
      console.log("stack was empty", origin_stack_number)
      process.exit(1);
    }
    destination_stack.push(crate);

    how_many_to_move -= 1;
  }
}


for (const stack of stacks.values()) {
  console.log(stack.pop());
}


