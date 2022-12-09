from pathlib import Path

Point = tuple[int, int]

def main():
    data = Path("input.txt").read_text()

    lines = data.split("\n")

    head = (0, 0)
    tail = (0, 0)

    visited: set[Point] = set()
    visited.add(tail)

    for line in lines:
        if line:
            direction, stepsStr = line.split(" ")
            steps = int(stepsStr)

            while steps > 0:
                head = move(head, direction)
                tail_direction = calculateTailMove(head, tail)
                tail = move(tail, tail_direction)
                visited.add(tail)
                steps -= 1

    print(len(visited))

def move(point: Point, direction: str) -> Point:
    x, y = point
    match direction:
        case "R":
            return (x + 1, y)
        case "L":
            return (x - 1, y)
        case "D":
            return (x, y - 1)
        case "U":
            return (x, y + 1)
        case "":
            return point
        case "UR":
            return (x + 1, y + 1)
        case "UL":
            return (x - 1, y + 1)
        case "DR":
            return (x + 1, y - 1)
        case "DL":
            return (x - 1, y - 1)
        case _:
            raise Exception("not reachable")


def calculateTailMove(head: Point, tail: Point) -> str:
    h_x, h_y = head
    t_x, t_y = tail

    x_dist = h_x - t_x
    y_dist = h_y - t_y

    if x_dist <= 1 and x_dist >= -1 and y_dist <= 1 and y_dist >= -1:
        return ""

    if x_dist > 0 and y_dist > 1 or x_dist > 1 and y_dist > 0:
        return "UR"

    if x_dist > 0 and y_dist < -1 or x_dist > 1 and y_dist < 0:
        return "DR"

    if x_dist < -1 and y_dist > 0 or x_dist < 0 and y_dist > 1:
        return "UL"

    if x_dist < -1 and y_dist < 0 or x_dist < 0 and y_dist < -1:
        return "DL"

    if y_dist < -1:
        return "D"

    if x_dist < -1:
        return "L"

    if x_dist > 1:
        return "R"

    if y_dist > 1:
        return "U"

    raise Exception("not reachable")


if __name__ == "__main__":
    main()
