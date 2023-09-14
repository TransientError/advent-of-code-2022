from collections import deque
from pathlib import Path


def to_decimal(s: str) -> int:
    place = 1
    result = 0
    for i in range(len(s)):
        char = s[-1 - i]
        match char:
            case "1":
                value = 1
            case "2":
                value = 2
            case "=":
                value = -2
            case "-":
                value = -1
            case "0":
                value = 0
            case _:
                raise Exception(f"Unknown char {char}")

        result += value * place

        place *= 5
    return result


def from_decimal(n: int) -> str:
    place = 1
    result = deque()
    while n > 0:
        remainder = n % (5 * place)
        match (d := remainder // place):
            case 0 | 1 | 2:
                result.appendleft(str(d))
                n -= d * place
            case 3:
                result.appendleft("=")
                n += 2 * place
            case 4:
                result.appendleft("-")
                n += place
        
        place *= 5
    
    return ''.join(result)


data = Path("input.txt").read_text().splitlines()

total = sum(to_decimal(line) for line in data)
print(from_decimal(total))
