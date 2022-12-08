import { readFileSync } from "fs";
import { safeParseInt } from "../utils/utils.js";

const data: number[][] = readFileSync("input.txt")
  .toString()
  .split("\n")
  .slice(0, -1)
  .map((line) => line.split("").map((c) => safeParseInt(c).unwrap()));

interface VisibleData {
  left: number;
  right: number;
  bottom: number;
  top: number;
}

const calculateTreesVisible = (
  h: number,
  array: number[],
  rev: boolean
): number => {
  let visible = 0;
  for (const height of rev ? array.reverse() : array) {
    if (height <= h) {
      visible++;
    }

    if (height >= h) {
      break;
    }
  }
  return visible;
};

const treesVisible = (
  x: number,
  y: number,
  matrix: number[][]
): VisibleData => {
  const height = matrix[x][y];

  const treesToLeft = matrix[x].slice(0, y);
  const treesToRight = matrix[x].slice(y + 1);

  const treesVertical: number[] = matrix.map((line) => line[y]);
  const treesBelow = treesVertical.slice(0, x);
  const treesAbove = treesVertical.slice(x + 1);

  return {
    left: calculateTreesVisible(height, treesToLeft, true),
    right: calculateTreesVisible(height, treesToRight, false),
    bottom: calculateTreesVisible(height, treesBelow, true),
    top: calculateTreesVisible(height, treesAbove, false),
  };
};

const result: number[] = data
  .flatMap((line, i) => line.map((_, j) => treesVisible(i, j, data)))
  .map((vd) => Object.values(vd).reduce((a, b) => a * b));

console.log(Math.max(...result));
