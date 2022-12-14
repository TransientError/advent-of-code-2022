from enum import Enum, auto
from pathlib import Path

data = Path("test-input.txt").read_text().splitlines()


class Operation(Enum):
    Add = (auto(),)
    Mult = (auto(),)
    Pow = auto()


class Monkey:

    initial_items: list[int]
    items: list[dict[int, int]]
    operation: tuple[Operation, int]
    test: tuple[int, int, int]
    inspected: int

    def __init__(self, items, operation, test) -> None:
        self.initial_items = items
        self.operation = operation
        self.test = test
        self.inspected = 0

    def __repr__(self) -> str:
        return "\n".join(
            [
                f"Starting items: {self.initial_items}",
                f" Operation: new = old {'+' if self.operation[0] == Operation.Add else '*'} {self.operation[1] if self.operation[0] != Operation.Pow else 'old'}",
                f" Test: divisible by {self.test[0]}",
                f"  If true: throw to monkey {self.test[1]}",
                f"  If false: throw to monkey {self.test[2]}",
            ]
        )


monkeys = []
for i in range(0, len(data), 7):
    monkey_index = data[i].split(" ")[1]
    initial_items = [int(s) for s in data[i + 1].split(":")[1].split(", ")]

    match data[i + 2].split(": ")[1]:
        case _ as op if "+" in op:
            component = int(op.split(" + ")[1])
            operation = (Operation.Add, component)
        case _ as op if "*" in op:
            components = op.split(" * ")
            if components[1] == "old":
                operation = (Operation.Pow, 2)
            else:
                component = int(components[1])
                operation = (Operation.Mult, component)

    factor = int(data[i + 3].split("by ")[1])

    true_monk = int(data[i + 4].split("monkey ")[1])
    false_monk = int(data[i + 5].split("monkey ")[1])

    monkeys.append(
        Monkey(initial_items, operation, (factor, true_monk, false_monk)) # type:ignore
    )  

for i, monkey in enumerate(monkeys):
    print("Monkey", i)
    print(monkey)
