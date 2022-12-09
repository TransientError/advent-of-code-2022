import { readFileSync } from "fs";
import { safeParseInt } from "../utils/utils.js";

const data = readFileSync("input.txt").toString().split("\n");

const stringify = (p: number[]) => p.join(',');

const move = (point: number[], direction: string): number[] => {
  const [x, y] = point;
  switch (direction) {
    case "R":
      return [x + 1, y];
    case "L":
      return [x - 1, y];
    case "D":
      return [x, y - 1];
    case "U":
      return [x, y + 1];
    case "":
      return point;
    case "UR":
      return [x + 1, y + 1];
    case "UL":
      return [x - 1, y + 1];
    case "DR":
      return [x + 1, y - 1];
    case "DL":
      return [x - 1, y - 1];
  }
};

const calculateTailMove = (head: number[], tail: number[]): string => {
  const [h_x, h_y] = head;
  const [t_x, t_y] = tail;

  const x_distance = h_x - t_x;
  const y_distance = h_y - t_y;
  if (
    x_distance <= 1 &&
    x_distance >= -1 &&
    y_distance <= 1 &&
    y_distance >= -1
  ) {
    return "";
  }

  if (
    (x_distance > 0 && y_distance > 1) ||
    (x_distance > 1 && y_distance > 0)
  ) {
    return "UR";
  }

  if (
    (x_distance > 0 && y_distance < -1) ||
    (x_distance > 1 && y_distance < 0)
  ) {
    return "DR";
  }

  if (
    (x_distance < -1 && y_distance > 0) ||
    (x_distance < 0 && y_distance > 1)
  ) {
    return "UL";
  }

  if (
    (x_distance < -1 && y_distance < 0) ||
    (x_distance < 0 && y_distance < -1)
  ) {
    return "DL";
  }

  if (y_distance < -1) {
    return "D";
  }

  if (x_distance < -1) {
    return "L";
  }

  if (x_distance > 1) {
    return "R";
  }

  if (y_distance > 1) {
    return "U";
  }
};

const visited = new Set<string>();

let head = [0, 0];
let tail = [0, 0];

visited.add(stringify(tail));

for (const line of data) {
  if (line) {
    const [direction, stepsStr] = line.split(" ");
    let steps = safeParseInt(stepsStr).unwrap();

    while (steps > 0) {

      head = move(head, direction);
      const tail_direction = calculateTailMove(head, tail);
      tail = move(tail, tail_direction);
      visited.add(stringify(tail));
      steps--;
    }
  }
}

console.log(visited.size);
