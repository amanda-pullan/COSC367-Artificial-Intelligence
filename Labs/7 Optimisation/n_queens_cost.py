# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:13:36 2020

@author: Amanda
"""

from itertools import combinations

def n_queens_cost(state):
    """Takes a state (total assignment) for an n-queen problem
    and returns the number conflicts for that state.
    """
    conflicts = 0
    for pair in list(combinations(state, 2)):
        x1, x2 = pair[0], pair[1]
        y1, y2 = state.index(x1), state.index(x2)
        if abs(x1 - x2) == abs(y1 - y2):
            conflicts += 1
    return conflicts




# Examples
print(n_queens_cost((1, 2)))

print(n_queens_cost((1, 3, 2)))
print(n_queens_cost((1, 2, 3)))
print(n_queens_cost((1,)))
print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))
print(n_queens_cost((2, 3, 1, 4)))
print(n_queens_cost((2, 4, 1, 3)))
print(n_queens_cost((4, 1, 3, 2, 6, 5)))