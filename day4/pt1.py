from pathlib import Path

grid = []
with Path("input.txt").open() as f:
    for line in f:
        grid.append([c == "@" for c in line.strip()])

num_rolls = 0
adjacent_directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]
for row in range(len(grid)):
    for cell in range(len(grid[row])):
        num_adjacent = 0
        for dx, dy in adjacent_directions:
            x, y = row + dx, cell + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[row]) and grid[x][y]:
                num_adjacent += 1
        if num_adjacent < 4 and grid[row][cell]:
            num_rolls += 1
print(num_rolls)
