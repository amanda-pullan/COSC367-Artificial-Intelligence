# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:29:21 2020

@author: Amanda
"""

def greedy_descent(initial_state, neighbours, cost):
    """Takes an initial state and two functions to compute the
    neighbours and cost of a state, and then iteratively improves
    the state until a local minimum (which may be global) is reached.
    """
    states = [initial_state]
    current = initial_state
    min_cost = False   
    while not min_cost:
        neighbour_list = neighbours(current)
        if len(neighbour_list) == 0:
            break      
        for i, neighbour in enumerate(neighbour_list):
            if cost(neighbour) < cost(current):
                current = neighbour_list[i]
                states.append(current)
        else:
            min_cost = True      
    return states
        

# Example 1
def cost(x):
    return x**2

def neighbours(x):
    return [x - 1, x + 1]

for state in greedy_descent(4, neighbours, cost):
    print(state)


# Example 2
def cost(x):
    return x**2

def neighbours(x):
    return [x - 1, x + 1]

for state in greedy_descent(-6.75, neighbours, cost):
    print(state)

# Example 3
def cost(x):
    return -x**2

def neighbours(x):
    return [x - 1, x + 1] if abs(x) < 5 else []

for state in greedy_descent(0, neighbours, cost):
    print(state)