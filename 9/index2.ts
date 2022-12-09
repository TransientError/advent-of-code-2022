import { readFileSync } from "fs";

type Point = [number, number]

const data = readFileSync("input.txt").toString().split("\n");

// bleh this is kinda a real dealbreaker for js. You can only compare primitives in Set.
const stringify = (p: Point): string => p.join(',');

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

const calculateMove = (node1: number[], node2: number[]): string => {
  const [x_1, y_1] = node1;
  const [x_2, y_2] = node2;

  const x_distance = x_1 - x_2;
  const y_distance = y_1 - y_2;
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

let snake = Array(10).fill([0, 0]);

visited.add(stringify(snake[9]));

for (const line of data) {
  if (line) {
    const [direction, stepsStr] = line.split(" ");
    let steps = parseInt(stepsStr);
    if (isNaN(steps)) {
      console.log(stepsStr, "could not be parsed");
      process.exit(1);
    }

    while (steps > 0) {
      snake[0] = move(snake[0], direction);

      for (let i = 1; i < snake.length; i++) {
        const dir = calculateMove(snake[i - 1], snake[i]);
        snake[i] = move(snake[i], dir);
      }

      visited.add(stringify(snake[9]));
      steps--;
    }
  }
}

console.log(visited.size);
