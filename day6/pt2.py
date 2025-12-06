from functools import reduce
import operator
from pathlib import Path

with Path("input.txt").open() as f:
    lines = [list(line.removesuffix("\n")) for line in f.readlines()]

transposed = [*zip(*lines)]

total = 0
nums = []
addmul = None
for column in transposed:
    if all(c == " " for c in column):
        print(nums, addmul)
        if addmul == "+":
            total += sum(map(int, nums))
        else:
            total += reduce(operator.mul, map(int, nums), 1)
        nums = []
        addmul = None
        continue

    parts = "".join(column).strip().split()
    for part in parts:
        if part.isdigit():
            nums.append(part)
        elif part in "+*":
            addmul = part
        else:
            # edge case of <num>+
            nums.append(part[:-1])
            addmul = part[-1]

# final parse
if addmul == "+":
    total += sum(map(int, nums))
else:
    total += reduce(operator.mul, map(int, nums), 1)

print(total)
