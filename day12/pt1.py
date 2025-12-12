from pathlib import Path

total = 0
with Path("input.txt").open() as f:
    for line in f:
        lhs, rhs = line.split(":")
        x, y = map(int, lhs.split("x"))
        size = x * y
        amounts = sum(map(int, rhs.split()))
        if size >= amounts * 7:
            total += 1
print(total)
