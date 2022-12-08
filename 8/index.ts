import { readFileSync } from "fs";
import _ from "lodash";
import { safeParseInt } from "../utils/utils.js";

const data: number[][] = readFileSync("input.txt")
  .toString()
  .split("\n")
  .filter((line) => line)
  .map((line) => line.split("").map((c) => safeParseInt(c).unwrap()));

interface VisibleData {
  left: boolean;
  right: boolean;
  bottom: boolean;
  top: boolean;
}

const isVisible = (x: number, y: number, matrix: number[][]): VisibleData => {
  const height: number = matrix[x][y];
  const treesToLeft = matrix[x].slice(0, y);
  const treesToRight = matrix[x].slice(y + 1);

  const treesVertical: number[] = matrix.map((line) => line[y]);
  const treesBelow = treesVertical.slice(0, x);
  const treesAbove = treesVertical.slice(x + 1);

  return {
    left: !treesToLeft.some((t) => t >= height),
    right: !treesToRight.some((t) => t >= height),
    bottom: !treesBelow.some((t) => t >= height),
    top: !treesAbove.some((t) => t >= height),
  };
};

const result: number = _(data)
  .flatMap((row, i) =>
    row.map((_, j) => Object.values(isVisible(i, j, data)).some((t) => t))
  )
  .filter((t) => t)
  .size();

console.log(result);
