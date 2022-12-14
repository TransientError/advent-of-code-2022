from collections import defaultdict
from pathlib import Path
from typing import Dict

Point = tuple[int, int]

data = Path("input.txt").read_text().splitlines()

board: Dict[int, dict[int, str]] = defaultdict(lambda: defaultdict(lambda: "."))

for line in data:
    if line:
        points = line.split(" -> ")
        for i in range(len(points) - 1):
            # start
            s_x, s_y = (int(s) for s in points[i].split(","))
            # end
            e_x, e_y = (int(s) for s in points[i + 1].split(","))

            if s_x == e_x:
                for i in range(min(s_y, e_y), max(s_y, e_y) + 1):
                    board[s_x][i] = "#"
            elif s_y == e_y:
                for i in range(min(s_x, e_x), max(s_x, e_x) + 1):
                    board[i][s_y] = "#"
            else:
                raise Exception("Bad input")

source = (500, 0)
board[500][0] = "+"
lowest_x = min(board.keys())
highest_x = max(board.keys())
highest_y = max(max(c for c in v.keys()) for v in board.values())
floor = highest_y + 2


def get(board, x, y):
    if y == floor:
        return "#"
    else:
        return board[x][y]


def display(board: Dict[int, dict[int, str]]):
    for y in range(floor + 1):
        line = []
        for x in range(lowest_x, highest_x + 1):
            line.append(get(board, x, y))
        print(line)

    print("\n")


full = False
iterations = 0
while not full:
    rested = False
    position = source
    while not rested:
        # iterations += 1
        p_x, p_y = position
        if get(board, p_x, p_y + 1) == ".":
            board[p_x][p_y] = "." if position != source else "+"
            board[p_x][p_y + 1] = "o"
            position = p_x, p_y + 1

        elif get(board, p_x - 1, p_y + 1) == ".":
            board[p_x][p_y] = "." if position != source else "+"
            board[p_x - 1][p_y + 1] = "o"
            position = p_x - 1, p_y + 1
            lowest_x = min(lowest_x, p_x)

        elif get(board, p_x + 1, p_y + 1) == ".":
            board[p_x][p_y] = "." if position != source else "+"
            board[p_x + 1][p_y + 1] = "o"
            position = p_x + 1, p_y + 1
            highest_x = max(highest_x, p_x)

        else:
            rested = True
            if position == source:
                full = True
                break

    iterations += 1


display(board)
print(iterations)
