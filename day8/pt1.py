from functools import reduce
import operator
from pathlib import Path
from collections import defaultdict

with Path("input.txt").open() as f:
    coords = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

pairs = []
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        distance = sum((a - b) ** 2 for a, b in zip(coords[i], coords[j]))
        pairs.append((distance, coords[i], coords[j]))
pairs.sort()

# union find adapted from https://www.geeksforgeeks.org/dsa/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/

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


for _, a, b in pairs[:1000]:
    union(a, b)

# find all circuits
circuits = defaultdict(list)
for coord in coords:
    root = find(coord)
    circuits[root].append(coord)

largest_cictuirs = sorted(circuits.values(), key=len, reverse=True)[:3]
print(reduce(operator.mul, (len(c) for c in largest_cictuirs), 1))
