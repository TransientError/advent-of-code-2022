from collections import defaultdict
from pathlib import Path


class Cave:
    X_SOURCE = 500
    Y_SOURCE = 0
    SOURCE = (X_SOURCE, Y_SOURCE)

    layout: dict[int, dict[int, str]]
    left_border: int
    right_border: int
    bottom_border: int
    floor: int

    def __init__(self, input: str) -> None:
        self.layout = defaultdict(lambda: defaultdict(lambda: "."))
        for line in input.splitlines():
            if line:
                points = line.split(" -> ")
                for i in range(len(points) - 1):
                    # start
                    s_x, s_y = (int(s) for s in points[i].split(","))
                    # end
                    e_x, e_y = (int(s) for s in points[i + 1].split(","))

                    if s_x == e_x:
                        for i in range(min(s_y, e_y), max(s_y, e_y) + 1):
                            self.layout[s_x][i] = "#"
                    elif s_y == e_y:
                        for i in range(min(s_x, e_x), max(s_x, e_x) + 1):
                            self.layout[i][s_y] = "#"
                    else:
                        raise Exception("Bad input")
        self.layout[Cave.X_SOURCE][Cave.Y_SOURCE] = "+"

        self.left_border = min(self.layout.keys())
        self.right_border = max(self.layout.keys())
        self.bottom_border = max(max(c for c in v.keys()) for v in self.layout.values())
        self.floor = self.bottom_border + 2

    def char_at_point(self, x: int, y: int) -> str:
        return "#" if y == self.floor else self.layout[x][y]

    def display(self):
        for y in range(self.floor + 1):
            line = []
            for x in range(self.left_border, self.right_border + 1):
                line.append(self.char_at_point(x, y))
            print(line)

        print("\n")

    def restore_point(self, x: int, y: int):
        self.layout[x][y] = "." if (x, y) != Cave.SOURCE else "+"

    def drop_sand(self) -> bool:
        position = Cave.SOURCE
        self.layout[500][0] = "o"
        while True:
            p_x, p_y = position

            if self.char_at_point(p_x, p_y + 1) == ".":
                self.restore_point(p_x, p_y)
                self.layout[p_x][p_y + 1] = "o"
                position = p_x, p_y + 1

            elif self.char_at_point(p_x - 1, p_y + 1) == ".":
                self.restore_point(p_x, p_y)
                self.layout[p_x - 1][p_y + 1] = "o"
                position = p_x - 1, p_y + 1
                self.left_border = min(self.left_border, p_x)

            elif self.char_at_point(p_x + 1, p_y + 1) == ".":
                self.restore_point(p_x, p_y)
                self.layout[p_x + 1][p_y + 1] = "o"
                position = p_x + 1, p_y + 1
                self.right_border = max(self.right_border, p_x)

            else:
                if position == Cave.SOURCE:
                    return True
                break

        return False


data = Path("input.txt").read_text()
cave = Cave(data)

iterations = 1
while not cave.drop_sand():
    iterations += 1


cave.display()
print(iterations)
