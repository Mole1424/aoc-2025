from pathlib import Path

with Path("input.txt").open() as f:
    lines = f.read().splitlines()

sum = 0
for line in lines:
    largest_char = max(line[:-1])
    largext_idx = line.index(largest_char)
    remaining = line[largext_idx + 1 :]
    largest_remaining = max(remaining)
    sum += int(largest_char) * 10 + int(largest_remaining)
print(sum)
