import numpy as np
import pandas as pd


def visualize_policy(policy, actions):
    list_actions = list(actions.keys())
    argmaxed_policy = np.argmax(policy, axis=-1)
    visual_policy = np.vectorize(list_actions.__getitem__)(argmaxed_policy)
            
    return pd.DataFrame(data=visual_policy)

def create_grid(location, matrix):
    """Calculate next position based on the action and the current position."""
    grid = np.zeros(matrix.shape)
    y, x = location
    grid[location] = 1
    return grid