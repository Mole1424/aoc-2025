from pathlib import Path

rotation = 50
num_zeros = 0

with Path("input.txt").open() as f:
    for line in f:
        direction = line[0]
        value = int(line[1:])
        incriment = 1 if direction == "R" else -1
        for _ in range(value):
            rotation = (rotation + incriment) % 100
            if rotation == 0:
                num_zeros += 1
print(num_zeros)
