from pathlib import Path

with Path("input.txt").open() as f:
    red_coords = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

green_boundary = set()
for i in range(len(red_coords)):
    x1, y1 = red_coords[i]
    x2, y2 = red_coords[(i + 1) % len(red_coords)]

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            green_boundary.add((x1, y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            green_boundary.add((x, y1))


def point_in_polygon(x: float, y: float) -> bool:
    inside = False
    for i in range(len(red_coords)):
        xi, yi = red_coords[i]
        xj, yj = red_coords[(i + 1) % len(red_coords)]
        intersect = ((yi > y) != (yj > y)) and (
            x < (xj - xi) * (y - yi) / (yj - yi) + xi
        )
        if intersect:
            inside = not inside
    return inside


green_coords = set()
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
min_x, max_x = min(x for x, y in red_coords), max(x for x, y in red_coords)
min_y, max_y = min(y for x, y in red_coords), max(y for x, y in red_coords)
for x, y in red_coords:
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        while (
            (min_x <= nx <= max_x)
            and (min_y <= ny <= max_y)
            and ((nx, ny) not in green_boundary)
        ):

            if point_in_polygon(nx + 0.5, ny + 0.5):
                green_coords.add((nx, ny))
            nx += dx
            ny += dy

green_coords.update(green_boundary)

rectangles = []
for i, coord1 in enumerate(red_coords):
    for coord2 in red_coords[i + 1 :]:
        x1, y1 = coord1
        x2, y2 = coord2

        valid = True
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if (x, y1) not in green_coords and (x, y1) not in red_coords:
                valid = False
                break
            if (x, y2) not in green_coords and (x, y2) not in red_coords:
                valid = False
                break
        if not valid:
            continue
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if (x1, y) not in green_coords and (x1, y) not in red_coords:
                valid = False
                break
            if (x2, y) not in green_coords and (x2, y) not in red_coords:
                valid = False
                break
        if not valid:
            continue

        rectangle_area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        rectangles.append(rectangle_area)

print(max(rectangles))
