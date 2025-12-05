from pathlib import Path

fresh_ids = []
num_fresh = 0
with Path("input.txt").open() as f:
    for line in f:
        if line.strip() == "":
            break

        start, end = map(int, line.strip().split("-"))
        fresh_ids.append((start, end))

fresh_ids.sort()
merged_ranges = []
current_start, current_end = fresh_ids[0]
for start, end in fresh_ids[1:]:
    if start <= current_end + 1:
        current_end = max(current_end, end)
    else:
        merged_ranges.append((current_start, current_end))
        current_start, current_end = start, end
merged_ranges.append((current_start, current_end))

for start, end in merged_ranges:
    num_fresh += end - start + 1

print(num_fresh)
