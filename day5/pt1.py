from pathlib import Path

fresh_ids = []
processing_ranges = True
num_fresh = 0
with Path("input.txt").open() as f:
    for line in f:
        if line.strip() == "":
            processing_ranges = False
            continue

        if processing_ranges:
            start, end = map(int, line.strip().split("-"))
            fresh_ids.append((start, end))
        else:
            id = int(line.strip())
            for start, end in fresh_ids:
                if start <= id <= end:
                    num_fresh += 1
                    break
print(num_fresh)
