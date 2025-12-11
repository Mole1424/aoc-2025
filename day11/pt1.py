from pathlib import Path

graph = {}
with Path("input.txt").open() as f:
    for line in f:
        node, edges = line.split(": ")
        edges = edges.split()
        graph[node] = edges


def dfs(node, destination) -> int:
    if node == destination:
        return 1
    return sum(dfs(neighbor, destination) for neighbor in graph[node])


print(dfs("you", "out"))
