from pathlib import Path

with Path("input.txt").open() as f:
    lines = f.read().splitlines()

tachyon_beams = [[c == "S" for c in lines[0]]]

num_splits = 0
for i, line in enumerate(lines[1:], start=1):
    new_row = [False] * len(line)
    for j, c in enumerate(line):
        if tachyon_beams[i - 1][j]:
            if c == "^":
                num_splits += 1
                if j > 0:
                    new_row[j - 1] = True
                if j < len(line) - 1:
                    new_row[j + 1] = True
            else:
                new_row[j] = True
    tachyon_beams.append(new_row)
print(num_splits)
