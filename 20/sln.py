from collections import deque
from copy import deepcopy
from pathlib import Path


data = Path("input.txt").read_text().splitlines()

initial = [int(s) for s in data]
working = deque(enumerate(deepcopy(initial)))
indexes = list(range(len(initial)))


def swap_forward(i: int):
    global indexes
    index = indexes[i]
    next_index = (index + 1) % len(initial)
    working[index], working[next_index] = working[next_index], working[index]
    indexes[i] = next_index
    indexes[working[index][0]] = index

    if next_index == len(initial) - 1:
        right = working.pop()
        working.appendleft(right)
        indexes = [(n + 1) % len(initial) for n in indexes]


def swap_backward(i: int):
    global indexes
    index = indexes[i]
    next_index = (index - 1) % len(initial)
    working[index], working[next_index] = working[next_index], working[index]
    indexes[i] = next_index
    indexes[working[index][0]] = index

    if next_index == 0:
        left = working.popleft()
        working.append(left)
        indexes = [n - 1 for n in indexes]


for i, n in enumerate(initial):
    for _ in range(abs(n)):
        if n > 0:
            swap_forward(i)
        if n < 0:
            swap_backward(i)

result = [t[1] for t in working]
zero_index = result.index(0)

print(
    sum(
        working[n % len(initial)][1]
        for n in range(1000 + zero_index, 3001 + zero_index, 1000)
    )
)
