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

    def execute_operation(self):
        self.items = [self.operation(n) for n in self.items]
        self.inspected += len(self.items)

    def relief(self):
        self.items = [n // 3 for n in self.items]

    def throw(self) -> list[tuple[int, int]]:
        result = [self.test(n) for n in self.items]
        self.items.clear()
        return result

    def catch(self, n: int):
        self.items.append(n)


monkeys = [
    Monkey(
        [92, 73, 86, 83, 65, 51, 55, 93],
        lambda n: n * 5,
        lambda n: (n, 3) if n % 11 == 0 else (n, 4),
    ),
    Monkey(
        [99, 67, 62, 61, 59, 98],
        lambda n: n * n,
        lambda n: (n, 6) if n % 2 == 0 else (n, 7),
    ),
    Monkey(
        [81, 89, 56, 61, 99],
        lambda n: n * 7,
        lambda n: (n, 1) if n % 5 == 0 else (n, 5),
    ),
    Monkey([97, 74, 68], lambda n: n + 1, lambda n: (n, 2) if n % 17 == 0 else (n, 5)),
    Monkey([78, 73], lambda n: n + 3, lambda n: (n, 2) if n % 19 == 0 else (n, 3)),
    Monkey([50], lambda n: n + 5, lambda n: (n, 1) if n % 7 == 0 else (n, 6)),
    Monkey(
        [95, 88, 53, 75], lambda n: n + 8, lambda n: (n, 0) if n % 3 == 0 else (n, 7)
    ),
    Monkey(
        [50, 77, 98, 85, 94, 56, 89],
        lambda n: n + 2,
        lambda n: (n, 4) if n % 13 == 0 else (n, 0),
    ),
]

for round in range(1, 21):
    for monkey in monkeys:
        monkey.execute_operation()
        monkey.relief()
        thrown = monkey.throw()
        for thrown_item, dest in thrown:
            monkeys[dest].catch(thrown_item)

inspections = [monkey.inspected for monkey in monkeys]
inspections.sort()
print(inspections)

print(inspections[-1] * inspections[-2])




