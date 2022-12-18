from copy import deepcopy
from dataclasses import dataclass
from enum import IntEnum
from pathlib import Path
from typing import Optional


data = Path("test-input.txt").read_text()

Point = tuple[int, int]


class RockType(IntEnum):
    Horizontal = 0
    Cross = 1
    Corner = 2
    Vertical = 3
    Square = 4


@dataclass
class Rock:
    type: RockType
    coordinates: list[Point]


class Chamber:
    repr: list[list[str]]
    next_rock_type: int
    cur_rock: Optional[Rock]
    rocks_dropped: int
    jetstreams: str
    jetstream_ix: int

    @staticmethod
    def empty_line() -> list[str]:
        return [".", ".", ".", ".", ".", ".", "."]

    def __init__(self, jetstreams: str) -> None:
        self.repr = [Chamber.empty_line() for _ in range(3)]
        self.next_rock = 0
        self.cur_rock = None
        self.rocks_dropped = 0
        self.jetstreams = jetstreams
        self.jetstream_ix = -1
        self.jetstream_counter = 0

    def display(self):
        repr = deepcopy(self.repr)
        if self.cur_rock:
            for (y, x) in self.cur_rock.coordinates:
                repr[y][x] = "@"
        repr.reverse()

        for line in repr:
            print(line)

        print(self.get_height())

    def draw_rock(self):
        assert self.cur_rock is None, "Can't draw next rock until last rock is settled"
        size = len(self.repr)
        match RockType(self.next_rock):
            case RockType.Horizontal:
                self.repr.append(Chamber.empty_line())
                size += 1
                self.cur_rock = Rock(
                    RockType.Horizontal,
                    [(size - 1, 2), (size - 1, 3), (size - 1, 4), (size - 1, 5)],
                )
            case RockType.Cross:
                for _ in range(3):
                    self.repr.append(Chamber.empty_line())
                size += 3
                self.cur_rock = Rock(
                    RockType.Cross,
                    [
                        (size - 1, 3),
                        (size - 2, 2),
                        (size - 2, 3),
                        (size - 2, 4),
                        (size - 3, 3),
                    ],
                )
            case RockType.Corner:
                for _ in range(3):
                    self.repr.append(Chamber.empty_line())
                size += 3
                self.cur_rock = Rock(
                    RockType.Corner,
                    [
                        (size - 3, 2),
                        (size - 3, 3),
                        (size - 3, 4),
                        (size - 2, 4),
                        (size - 1, 4),
                    ],
                )
            case RockType.Vertical:
                for _ in range(4):
                    self.repr.append(Chamber.empty_line())

                size += 4
                self.cur_rock = Rock(
                    RockType.Vertical,
                    [(size - 1, 2), (size - 2, 2), (size - 3, 2), (size - 4, 2)],
                )
            case RockType.Square:
                for _ in range(2):
                    self.repr.append(Chamber.empty_line())
                size += 2
                self.cur_rock = Rock(
                    RockType.Square,
                    [(size - 1, 2), (size - 1, 3), (size - 2, 2), (size - 2, 3)],
                )

        self.next_rock = (self.next_rock + 1) % 5

    def is_occupiable(self, y: int, x: int) -> bool:
        return y >= 0 and x >= 0 and x < 7 and self.repr[y][x] != "#"

    def shift_rock(self, dir: str):
        assert self.cur_rock is not None, "there is no rock to shift"
        rock = self.cur_rock
        match dir:
            case "<":
                if all(self.is_occupiable(y, x - 1) for (y, x) in rock.coordinates):
                    for (i, (y, x)) in enumerate(rock.coordinates):
                        rock.coordinates[i] = (y, x - 1)
            case ">":
                if all(self.is_occupiable(y, x + 1) for (y, x) in rock.coordinates):
                    for (i, (y, x)) in enumerate(rock.coordinates):
                        rock.coordinates[i] = (y, x + 1)

    def fall(self) -> bool:
        assert self.cur_rock is not None, "there is no rock to fall"

        if all(self.is_occupiable(y - 1, x) for y, x in self.cur_rock.coordinates):
            for (i, (y, x)) in enumerate(self.cur_rock.coordinates):
                self.cur_rock.coordinates[i] = (y - 1, x)
            return False
        return True

    def stabilize_rock(self):
        assert self.cur_rock is not None, "There is no rock to stabilize"
        for (y, x) in self.cur_rock.coordinates:
            self.repr[y][x] = "#"
        self.cur_rock = None
        self.rocks_dropped += 1

    def get_next_jetstream(self) -> str:
        self.jetstream_ix = (self.jetstream_ix + 1) % (len(self.jetstreams) - 1)
        return self.jetstreams[self.jetstream_ix]

    def peek_next_jetstream(self) -> str:
        return self.jetstreams[(self.jetstream_ix + 1) % len(self.jetstreams)]

    def add_buffer_lines(self):
        index = len(self.repr) - 1
        count = 0
        while all(s == "." for s in self.repr[index]):
            index -= 1
            count += 1

        if count < 3:
            for _ in range(3 - count):
                self.repr.append(Chamber.empty_line())

        elif count > 3:
            for _ in range(count - 3):
                self.repr.pop()

    def drop(self):
        while self.rocks_dropped < 2022:
            self.draw_rock()
            self.shift_rock(self.get_next_jetstream())
            while not self.fall():
                self.shift_rock(self.get_next_jetstream())
            self.stabilize_rock()
            self.add_buffer_lines()

    def get_height(self):
        index = len(self.repr) - 1
        while all(s == "." for s in self.repr[index]):
            index -= 1

        return index + 1


chamber = Chamber(data)
chamber.drop()
chamber.display()
