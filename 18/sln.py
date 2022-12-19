from pathlib import Path


cubes = set()

total_surface_area = 0

data = Path("input.txt").read_text().splitlines()

for line in data:
    if line:
        x, y, z = [int(s) for s in line.split(",")]
        adjacent_cubes = sum(
            1 if cube in cubes else 0
            for cube in [
                (x, y, z - 1),
                (x, y, z + 1),
                (x, y - 1, z),
                (x, y + 1, z),
                (x - 1, y, z),
                (x + 1, y, z),
            ]
        )

        total_surface_area += -2 * adjacent_cubes + 6
        cubes.add((x, y, z))


print(total_surface_area)
