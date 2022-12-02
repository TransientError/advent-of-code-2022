import { readFile } from "fs/promises";

const data = (await readFile("input.txt")).toString().split("\n");

const my_move_score_map = {
  X: 1,
  Y: 2,
  Z: 3,
}

let total_score = 0;

for (const game of data) {
  if (game) {
    const moves = game.split(" ");
    const their_move = moves[0];
    const my_move = moves[1];

    total_score += my_move_score_map[my_move]

    switch (game) {
      // tie
      case "A X":
      case "B Y":
      case "C Z":
        total_score += 3;
        break;
      // lose
      case "A Z":
      case "B X":
      case "C Y":
        break;
      // win
      case "A Y":
      case "B Z":
      case "C X":
        total_score += 6;
        break;
    }
  }
}

console.log(total_score);
