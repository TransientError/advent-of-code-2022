from pathlib import Path
from typing import Union
import json
from functools import cmp_to_key

data = Path("input.txt").read_text().splitlines()

Token = Union[list, int]

data.append("[[2]]")
data.append("[[6]]")

def compare(left: Union[int, list], right: Token) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        if right < left:
            return 1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        if not left and not right:
            # might be impossible
            return 0
        if left and not right:
            return 1
        if not left and right:
            return -1

        i = 0
        while True:
            if i >= len(left) and i < len(right):
                return -1
            if i >= len(right) and i < len(left):
                return 1
            if i >= len(right) and i >= len(left):
                return 0
            res = compare(left[i], right[i])
            if res != 0:
                return res
            i += 1

    raise Exception("unreachable")

result = sorted([json.loads(line) for line in data if line], key=cmp_to_key(compare))
print(result)
divider1 = (result.index([[2]])) + 1
divider2 = (result.index([[6]])) + 1

print(divider1, divider2, divider1 * divider2)


