from pathlib import Path

with Path("input.txt").open() as f:
    coords = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

pairs = []
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        distance = sum((a - b) ** 2 for a, b in zip(coords[i], coords[j]))
        pairs.append((distance, coords[i], coords[j]))
pairs.sort()


parent = {}


def find(x):
    if parent.setdefault(x, x) != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return False
    parent[rx] = ry
    return True


num_components = len(coords)
last_edge = None

for _, a, b in pairs:
    if union(a, b):
        num_components -= 1
        last_edge = (a, b)
        if num_components == 1:
            break

print(last_edge[0][0] * last_edge[1][0])
