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
        values.extend((x, x))
        x += value

sln = sum(n * values[n - 1] for n in range(20, 221, 40))

print(sln)
