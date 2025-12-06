from functools import reduce
import operator
from pathlib import Path

with Path("input.txt").open() as f:
    lines = f.read().splitlines()

cols: list[list[int]] = []
total = 0
for line in lines:
    parts = line.split()
    for i, part in enumerate(parts):
        if part.isdigit():
            while len(cols) <= i:
                cols.append([])
            cols[i].append(int(part))
        else:
            if part == "+":
                total += sum(cols[i])
            else:
                total += reduce(operator.mul, cols[i], 1)
print(total)
