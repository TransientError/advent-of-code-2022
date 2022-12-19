from pathlib import Path
import re
from typing import Optional

from icecream import ic


Point = tuple[int, int]


class Range:
    repr: tuple[int, int]

    def __init__(self, low: int, high: int) -> None:
        self.repr = (low, high)

    def __contains__(self, n: int) -> bool:
        low, high = self.repr
        return n >= low and n < high

    def merge(self, other: "Range") -> list["Range"]:
        s_low, s_high = self.repr
        o_low, o_high = other.repr

        if not s_low > o_high and not o_low > s_high:
            return [Range(min(s_low, o_low), max(s_high, o_high))]

        return [self, other]

    def width(self) -> int:
        return self.repr[1] + 1 - self.repr[0]

    def __repr__(self) -> str:
        return str(self.repr)


def taxicab_dist(left_x: int, left_y: int, right_x: int, right_y: int):
    return abs(left_x - right_x) + abs(right_y - left_y)


class Sensor:
    PARSER_RE: re.Pattern = re.compile(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )

    sensor: Point
    beacon: Point
    distance: Optional[int]
    y_range: Optional[Range]

    def __init__(self, sensor_x, sensor_y, beacon_x, beacon_y) -> None:
        self.sensor = sensor_x, sensor_y
        self.beacon = beacon_x, beacon_y
        self.distance = None
        self.y_range = None

    @staticmethod
    def parse(line: str) -> "Sensor":
        m = Sensor.PARSER_RE.match(line)
        assert m is not None
        sensor_x, sensor_y, beacon_x, beacon_y = (
            int(s) for s in (m[1], m[2], m[3], m[4])
        )
        return Sensor(sensor_x, sensor_y, beacon_x, beacon_y)

    def get_distance(self) -> int:
        if not self.distance:
            self.distance = taxicab_dist(*self.sensor, *self.beacon)
        return self.distance

    def get_y_range(self) -> Range:
        if not self.y_range:
            sensor_y = self.sensor[1]
            self.y_range = Range(
                sensor_y - self.get_distance(), sensor_y + self.get_distance()
            )

        return self.y_range

    def calculate_x_range_for(self, y: int) -> Range:
        s_x, s_y = self.sensor
        distance_from_center = abs(y - s_y)
        return Range(
            s_x - self.get_distance() + distance_from_center,
            s_x + self.get_distance() - distance_from_center,
        )

    def __repr__(self) -> str:
        return f"({self.sensor}, {self.distance})"


row_we_want = 2000000

data = Path("input.txt").read_text()

relevant_sensors = []
relevant_beacons = set([])

for line in data.splitlines():
    sensor = Sensor.parse(line)
    if row_we_want in sensor.get_y_range():
        relevant_sensors.append(sensor)
    if sensor.beacon[1] == row_we_want:
        relevant_beacons.add(sensor.beacon)

ranges = sorted(
    [s.calculate_x_range_for(row_we_want) for s in relevant_sensors],
    key=lambda r: r.repr,
)
solution = []
cur: Range = ranges[0]
for i in range(1, len(ranges)):
    second = ranges[i]

    result = cur.merge(second)
    if len(result) == 1:
        cur = result[0]
    else:
        solution.append(result[0])
        cur = result[1]

solution.append(cur)

print(sum(s.width() for s in solution) - len(relevant_beacons))
