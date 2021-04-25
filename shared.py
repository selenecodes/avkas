import numpy as np


# Shared environment for exercise 1,2
actions = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}
list_actions = list(actions.keys())

rewards = np.array([
    [-1, -1, -1, 40],
    [-1, -1, -10, -10],
    [-1, -1, -1, -1],
    [10, -2, -1, -1],
])

exits = [(3, 0), (0, 3), (3, 1)]
start = (3, 2)