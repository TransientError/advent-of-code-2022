import { readFile } from "fs/promises";

const data = (await readFile("input.txt")).toString().split("\n");

const my_score_from_result = {
  X: 0,
  Y: 3,
  Z: 6,
}

let total_score = 0;

for (const game of data) {
  if (game) {
    const moves = game.split(" ");
    const result = moves[1];
    let this_row_total = 0;
    this_row_total += my_score_from_result[result]

    switch (game) {
      // scissors
      case "A X":
      case "C Y":
      case "B Z":
        this_row_total += 3;
        break;
      // paper
      case "B Y":
      case "C X":
      case "A Z":
        this_row_total += 2;
        break;
      //rock
      case "A Y":
      case "B X":
      case "C Z":
        this_row_total += 1;
        break
    }

    console.log(this_row_total);

    total_score += this_row_total;
  }
}

console.log(total_score);
