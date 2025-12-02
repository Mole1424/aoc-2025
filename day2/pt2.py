from pathlib import Path

with Path("input.txt").open() as f:
    line = f.readline().strip()

sum = 0
for range_section in line.split(","):
    start, end = map(int, range_section.split("-"))

    for i in range(start, end + 1):
        str_i = str(i)
        # check if contains a repeating sequence of digits
        for seq_len in range(1, len(str_i) // 2 + 1):
            if len(str_i) % seq_len == 0:
                num_repeats = len(str_i) // seq_len
                sequence = str_i[:seq_len]
                if sequence * num_repeats == str_i:
                    sum += i
                    break

print(sum)
