from pathlib import Path
from collections import deque

with Path("input.txt").open() as f:
    machines = f.read().splitlines()


def get_machine_state(input):
    light_state, remaining = machine.split(maxsplit=1)
    buttons, joltage = remaining.rsplit(maxsplit=1)

    light_state = [c == "#" for c in light_state[1:-1]]
    buttons = [list(map(int, b[1:-1].split(","))) for b in buttons.split()]
    joltage = list(map(int, joltage[1:-1].split(",")))

    return light_state, buttons, joltage


def push_button(light_state, button):
    new_state = light_state[:]
    for i in button:
        new_state[i] = not new_state[i]
    return new_state


num_button_pushes = 0
for machine in machines:
    goal_light_state, buttons, _ = get_machine_state(machine)

    queue = deque([([False] * len(goal_light_state), 0)])
    visited = set()
    found = False
    while queue and not found:
        current_light_state, pushes = queue.popleft()
        if tuple(current_light_state) in visited:
            continue
        visited.add(tuple(current_light_state))

        if current_light_state == goal_light_state:
            num_button_pushes += pushes
            found = True
            break

        for button in buttons:
            new_state = push_button(current_light_state, button)
            queue.append((new_state, pushes + 1))
print(num_button_pushes)
