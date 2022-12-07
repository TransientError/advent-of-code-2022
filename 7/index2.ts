import { readFileSync } from "fs";
import path from "path";

const data = readFileSync("input.txt").toString().split("\n");

let map_filessize = new Map<string, number>();
let map_dirs = new Map<string, string[]>();
let cur: string[] = [];
let dirs: string[] = [];

for (const line of data) {
  if (line.startsWith("$ cd")) {
    if (line === "$ cd ..") {
      cur.pop();
      continue;
    } else {
      cur.push(line.split(" ")[2]);
      dirs.push(cur.reduce((a, b) => path.join(a, b)));
      continue;
    }
  }
  if (line.startsWith("$ ls")) {
    continue;
  }

  const key = cur.reduce((a, b) => path.join(a, b), "/");
  if (line.startsWith("dir")) {
    const dirs = map_dirs.get(key) ?? [];
    const dir_name = line.split(" ")[1];
    dirs.push(path.join(key, dir_name));
    map_dirs.set(key, dirs);
    continue;
  }

  if (line.match("^[0-9]")) {
    const existing = map_filessize.get(key) ?? 0;
    const new_total = existing + parseInt(line.split(" ")[0]);
    console.log(cur, "existing", existing, "new_total", new_total);
    map_filessize.set(key, new_total);
    continue;
  }
}

const calculateDirSize = (dir: string, memo: Map<string, number>): number => {
  if (memo.has(dir)) {
    return memo.get(dir);
  }

  const files_size = map_filessize.get(dir) ?? 0;
  const remaining_dirs = map_dirs.get(dir) ?? [];
  if (!remaining_dirs) {
    memo.set(dir, files_size);
    return files_size;
  } else {
    const remaining_size = remaining_dirs
      .map((sub) => calculateDirSize(sub, memo))
      .reduce((a, b) => a + b, 0);

    const result = files_size + remaining_size;
    memo.set(dir, result);
    return result;
  }
};

let map_total_sizes = new Map<string, number>();
const total_used = calculateDirSize("/", map_total_sizes);
map_total_sizes.set("/", total_used);
const total_available = 70_000_000;
const required = 30_000_000;

const needed = required - (total_available - total_used);

console.log("needed", needed);

const result = Array.from(map_total_sizes.entries())
  .filter((e) => e[1] >= needed)
  .reduce((e1, e2) => (e1[1] < e2[1] ? e1 : e2));

console.log("result", result);
process.exit(0);
