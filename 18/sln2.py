from enum import Enum, auto
from pathlib import Path
from typing import Iterable, Iterator
from icecream import ic


class Direction(Enum):
    North = auto()
    South = auto()
    East = auto()
    West = auto()
    Up = auto()
    Down = auto()


Cube = tuple[int, int, int]
Face = tuple[Direction, Cube]


def point_in_dir(point: Cube, dir: Direction) -> Cube:
    x, y, z = point
    match dir:
        case Direction.North:
            return (x, y + 1, z)
        case Direction.South:
            return (x, y - 1, z)
        case Direction.East:
            return (x + 1, y, z)
        case Direction.West:
            return (x - 1, y, z)
        case Direction.Up:
            return (x, y, z + 1)
        case Direction.Down:
            return (x, y, z - 1)


def opposite_direction(dir: Direction) -> Direction:
    match dir:
        case Direction.North:
            return Direction.South
        case Direction.South:
            return Direction.North
        case Direction.East:
            return Direction.West
        case Direction.West:
            return Direction.East
        case Direction.Up:
            return Direction.Down
        case Direction.Down:
            return Direction.Up


class BoundsCalculator:
    bound: int

    def __init__(self, cubes: Iterable[Cube]) -> None:
        self.bound = max(max(c) for c in cubes)

    def point_in_bounds(self, point: Cube) -> bool:
        x, y, z = point
        return (
            x >= -1
            and y >= -1
            and z >= -1
            and x < self.bound + 2
            and y < self.bound + 2
            and z < self.bound + 2
        )


faces = set()
cubes: set[Cube] = set(
    tuple(int(coord) for coord in line.split(","))
    for line in Path("input.txt").read_text().splitlines()
    if line
)

bc = BoundsCalculator(cubes)

visited = set()

stack: list[Cube] = [(-1, -1, -1)]

while stack:
    cur = stack.pop()
    visited.add(cur)
    for dir in Direction:
        point = point_in_dir(cur, dir)
        if not bc.point_in_bounds(point):
            continue
        if point in cubes:
            faces.add((opposite_direction(dir), point))
            continue
        if point not in visited:
            stack.append(point)

print(len(faces))
