from pathlib import Path
from typing import Callable


class Monkey:

    items: list[int]
    operation: Callable[[int], int]
    test: Callable[[int], tuple[int, int]]
    inspected: int

    def __init__(self, items, operation, test) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.inspected = 0

    def __repr__(self) -> str:
        return "\n".join(
            [
                f"Starting items: {self.items}",
                f" Operation: new = old {repr(self.operation)}",
                f" Test: divisible by {repr(self.test)}",
            ]
        )

data = Path("test-input.txt").read_text().splitlines()

monkeys = []
for i in range(0, len(data), 7):
    init = [int(s) for s in data[i + 1].split(": ")[1].split(", ")]

    if "+" in data[i + 2]:
        operation = lambda n: n + int(data[i + 2].split(" + ")[1])
    elif "*" in data[i + 2]:
        component = data[i + 2].split(" * ")[1]
        if component == "old":
            operation = lambda n: n**2
        else:
            operation = lambda n: n * int(component)

    factor = int(data[i + 3].split(" by ")[1])
    t_monk = int(data[i + 4].split(" monkey ")[1])
    f_monk = int(data[i + 5].split(" monkey ")[1])

    monkeys.append(Monkey(init, operation, lambda n: t_monk if n % factor == 0 else f_monk))  # type: ignore

for i, monkey in enumerate(monkeys):
    print("Monkey", i)
    print(monkey)
