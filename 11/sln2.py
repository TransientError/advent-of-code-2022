from enum import Enum, auto


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

    def pre_compute(self, monks: list["Monkey"]):
        self.items = [
            {m: n % m for m in (monk.test[0] for monk in monks)}
            for n in self.initial_items
        ]
        print(self.items)

    def execute_operation(self):
        self.items = [self.perform_operation(n) for n in self.items]
        self.inspected += len(self.items)

    def throw(self) -> list[tuple[dict[int, int], int]]:
        result = [self.perform_test(n) for n in self.items]
        self.items.clear()
        return result

    def catch(self, d):
        self.items.append(d)

    def perform_operation(self, d: dict[int, int]):
        op, v = self.operation
        match op:
            case Operation.Add:
                for mod, n in d.items():
                    d[mod] = (n + v) % mod
            case Operation.Mult:
                for mod, n in d.items():
                    d[mod] = (n * v) % mod
            case Operation.Pow:
                for mod, n in d.items():
                    d[mod] = (n**v) % mod
        return d

    def perform_test(self, d):
        divisor, t_dest, f_dest = self.test
        return (d, t_dest) if d[divisor] == 0 else (d, f_dest)


monkeys = [
    Monkey(
        [92, 73, 86, 83, 65, 51, 55, 93],
        (Operation.Mult, 5),
        (11, 3, 4),
    ),
    Monkey([99, 67, 62, 61, 59, 98], (Operation.Pow, 2), (2, 6, 7)),
    Monkey([81, 89, 56, 61, 99], (Operation.Mult, 7), (5, 1, 5)),
    Monkey([97, 74, 68], (Operation.Add, 1), (17, 2, 5)),
    Monkey([78, 73], (Operation.Add, 3), (19, 2, 3)),
    Monkey([50], (Operation.Add, 5), (7, 1, 6)),
    Monkey([95, 88, 53, 75], (Operation.Add, 8), (3, 0, 7)),
    Monkey([50, 77, 98, 85, 94, 56, 89], (Operation.Add, 2), (13, 4, 0)),
]

for monkey in monkeys:
    monkey.pre_compute(monkeys)

for round in range(1, 10_001):
    print("executing round", round)
    for i, monkey in enumerate(monkeys):
        monkey.execute_operation()
        thrown = monkey.throw()
        for thrown_item, dest in thrown:
            monkeys[dest].catch(thrown_item)

inspections = [monkey.inspected for monkey in monkeys]
print(inspections)
inspections.sort()

print(inspections[-1] * inspections[-2])
