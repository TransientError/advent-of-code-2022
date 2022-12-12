from pathlib import Path
from collections import deque
from typing import Deque

map: list[str] = Path("input.txt").read_text().splitlines()

Point = tuple[int, int]


def find_start(map: list[str]) -> tuple[int, int]:
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                return i, j

    raise Exception("no S in map")


def calculate_adjacent(t: tuple[int, int]) -> list[Point]:
    x, y = t
    return [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]


def is_accessible_from(o: Point, d: Point) -> bool:
    o_x, o_y = o
    d_x, d_y = d
    char_at_o = map[o_x][o_y]
    char_at_d = map[d_x][d_y]
    o_height = char_at_o if char_at_o != "S" else "a"
    d_height = map[d_x][d_y] if char_at_d != "E" else "z"

    return ord(d_height) - ord(o_height) <= 1


start = find_start(map)
print("found S at ", start)

queue: Deque[tuple[Point, int]] = deque([(start, 0)])
visited = set([])
result = []

while queue:
    cur, steps = queue.popleft()
    if not cur in visited:
        print("Checking", cur)
        cur_x, cur_y = cur
        if map[cur_x][cur_y] == "E":
            result.append(steps)
            break
        adjacent = calculate_adjacent(cur)

        for point in adjacent:
            x, y = point
            if (
                x >= 0
                and x < len(map)
                and y >= 0
                and y < len(map[0])
                and is_accessible_from(cur, point)
            ):
                queue.append((point, steps + 1))

        visited.add(cur)

print(result)
