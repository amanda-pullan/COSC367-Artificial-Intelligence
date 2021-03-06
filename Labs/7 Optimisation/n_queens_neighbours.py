# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:13:38 2020

@author: Amanda
"""

def n_queens_neighbours(state):
    """Takes a state (total assignment) for an n-queen problem
    and returns a sorted list of states that are the neighbours
    of the current assignment.
    """
    neighbours = []
    n = len(state) 
    for i in range(n-1):
        pos = i + 1
        while pos < n:
            new_state = list(state[:])
            new_state[i], new_state[pos] = new_state[pos], new_state[i]
            neighbours.append(tuple(new_state))
            pos += 1
    return sorted(neighbours)     


# # Examples
# print(n_queens_neighbours((1, 2)))
# print(n_queens_neighbours((1, 3, 2)))
# print(n_queens_neighbours((1, 2, 3)))
# print(n_queens_neighbours((1,)))

# # Bigger Examples
# for neighbour in n_queens_neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
#     print(neighbour)
# for neighbour in n_queens_neighbours((2, 3, 1, 4)):
#     print(neighbour)