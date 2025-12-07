from pathlib import Path

with Path("input.txt").open() as f:
    lines = f.read().splitlines()

tachyon_beams = [[1 if c == "S" else 0 for c in lines[0]]]

for i, line in enumerate(lines[1:], start=1):
    new_row = [0] * len(line)
    for j, c in enumerate(line):
        if tachyon_beams[i - 1][j]:
            if c == "^":
                if j > 0:
                    new_row[j - 1] += tachyon_beams[i - 1][j]
                if j < len(line) - 1:
                    new_row[j + 1] += tachyon_beams[i - 1][j]
            else:
                new_row[j] += tachyon_beams[i - 1][j]
    tachyon_beams.append(new_row)
print(sum(tachyon_beams[-1]))
