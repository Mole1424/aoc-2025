from pathlib import Path
from functools import cache

graph = {}
with Path("input.txt").open() as f:
    for line in f:
        node, edges = line.split(": ")
        edges = edges.split()
        graph[node] = edges


@cache
def dfs(node, destination, goal_1, goal_2) -> int:
    if node == destination:
        return 1 if goal_1 and goal_2 else 0

    goal_1 = goal_1 or node == "fft"
    goal_2 = goal_2 or node == "dac"

    return sum(dfs(neighbor, destination, goal_1, goal_2) for neighbor in graph[node])


print(dfs("svr", "out", False, False))
