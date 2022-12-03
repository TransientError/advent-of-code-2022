import { readFile } from "fs/promises";

const data = (await readFile("input.txt")).toString().split("\n");

let total = 0;

const toPriority = (s: string) =>
  s === s.toUpperCase() ? s.charCodeAt(0) - 38 : s.charCodeAt(0) - 96;

for (const line of data) {
  if (line) {
    const compartment_index = line.length / 2;
    // Put first compartment into a set
    let compartment_1_items = new Set<string>(
      line.substring(0, compartment_index).split("")
    );

    // Check second compartment for shared items
    const common = line
      .substring(compartment_index)
      .split("")
      .find((e) => compartment_1_items.has(e));
    console.log("common", common);

    if (common === undefined) {
      console.log("No common character was found")
      process.exit(1);
    }

    const priority = toPriority(common);

    console.log("priority", priority);
    total += priority;
  }
}
console.log(total);
