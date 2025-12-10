from pathlib import Path
from collections import deque
import numpy as np
from scipy.optimize import linprog

with Path("input.txt").open() as f:
    machines = f.read().splitlines()


def get_machine_state(machine):
    light_state, remaining = machine.split(maxsplit=1)
    buttons, joltage = remaining.rsplit(maxsplit=1)

    light_state = [c == "#" for c in light_state[1:-1]]
    buttons = [list(map(int, b[1:-1].split(","))) for b in buttons.split()]
    joltage = list(map(int, joltage[1:-1].split(",")))

    return light_state, buttons, joltage


num_button_pushes = 0
for machine in machines:
    _, buttons, goal_joltage = get_machine_state(machine)

    # idea and general method from advent of code subreddit

    # define A for LP
    # A[i,j] = number of times button j increases joltage i
    m = len(goal_joltage)
    n = len(buttons)
    A = np.zeros((m, n), dtype=int)
    for j, btn in enumerate(buttons):
        for i in btn:
            A[i, j] += 1

    res = linprog(
        np.ones(n), A_eq=A, b_eq=goal_joltage, bounds=[(0, None)] * n, method="highs"
    )
    num_button_pushes += np.rint(res.x).astype(int).sum()

print(num_button_pushes)
