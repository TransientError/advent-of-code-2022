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

console.log(map_dirs);
console.log(map_filessize);
console.log(dirs);

const calculateDirSize = (dir: string): number => {
  const files_size = map_filessize.get(dir) ?? 0;
  const remaining_dirs = map_dirs.get(dir) ?? [];
  if (!remaining_dirs) {
    return files_size;
  } else {
    const remaining_size = remaining_dirs
      .map((sub) => calculateDirSize(sub))
      .reduce((a, b) => a + b, 0);

    return files_size + remaining_size;
  }
};

const size = dirs
  .map((dir) => calculateDirSize(dir))
  .filter((size) => size <= 100_000)
  .reduce((a, b) => a + b, 0);

console.log("size", size);
process.exit(0);
