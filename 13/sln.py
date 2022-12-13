from pathlib import Path
from typing import Union
import json

data = Path("input.txt").read_text().splitlines()

Token = Union[list[int], int]


def compare(left: Union[int, list[int]], right: Token) -> bool:
    if isinstance(left, int) and isinstance(right, int):
        return left <= right
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        if not left and not right:
            # might be impossible
            return True
        if left and not right:
            return False
        if not left and right:
            return True

        i = 0
        while True:
            if i >= len(left) and i < len(right):
                return True
            if i >= len(right) and i < len(left):
                return False
            if i >= len(right) and i >= len(left):
                return True
            elif left[i] == right[i]:
                i += 1
                continue
            return compare(left[i], right[i])

    raise Exception("unreachable")


right_order = []
iteration = 1
for i in range(0, len(data), 3):
    left = json.loads(data[i])
    right = json.loads(data[i + 1])

    if compare(left, right):
        right_order.append(iteration)
    iteration += 1

print(right_order)
print(sum(right_order))
