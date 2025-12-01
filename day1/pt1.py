from pathlib import Path

rotation = 50
num_zeros = 0

with Path("input.txt").open() as f:
    for line in f:
        direction = line[0]
        value = int(line[1:])
        rotation = (
            (rotation - value) % 100 if direction == "L" else (rotation + value) % 100
        )
        if rotation == 0:
            num_zeros += 1
print(num_zeros)
