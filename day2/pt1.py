from pathlib import Path

with Path("input.txt").open() as f:
    line = f.readline().strip()

sum = 0
for range_section in line.split(","):
    start, end = map(int, range_section.split("-"))

    for i in range(start, end + 1):
        str_i = str(i)
        if len(str_i) % 2 == 0:
            mid = len(str_i) // 2
            left, right = str_i[:mid], str_i[mid:]
            if left == right:
                sum += i

print(sum)
