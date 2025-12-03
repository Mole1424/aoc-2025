from pathlib import Path

with Path("input.txt").open() as f:
    lines = f.read().splitlines()

sum = 0
for line in lines:
    remaining_string = line
    largest_chars = []
    for i in range(12, 0, -1):
        window = remaining_string[: (len(remaining_string) - i + 1)]
        largest_chars.append(max(window))
        largest_idx = window.index(largest_chars[-1])
        remaining_string = remaining_string[largest_idx + 1 :]
    sum += int("".join(largest_chars))
print(sum)
