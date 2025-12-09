from pathlib import Path

with Path("input.txt").open() as f:
    coords = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

rectangles = []
for i, coord1 in enumerate(coords):
    for coord2 in coords[i + 1 :]:
        x1, y1 = coord1
        x2, y2 = coord2
        rectangle_area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        rectangles.append(rectangle_area)

print(max(rectangles))
