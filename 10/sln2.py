from pathlib import Path

data = Path("input.txt").read_text().splitlines()

x = 1
values = []

for line in data:
    if line.startswith("noop"):
        values.append(x)
        continue
    if line.startswith("addx"):
        value = int(line.split(" ")[1])
        values.append(x)
        values.append(x)
        x += value

values.append(x)


def sprite_is_visible(cycle: int):
    return cycle % 40 in range(values[cycle] - 1, values[cycle] + 2) 


sln = "".join(
    "#" if sprite_is_visible(i) else "." for i in range(240)
)

for i in range(0, len(sln), 40):
    print(sln[i:i+40])
