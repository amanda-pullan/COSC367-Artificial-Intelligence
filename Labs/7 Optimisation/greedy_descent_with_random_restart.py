# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:03:06 2020

@author: Amanda
"""

import random
from itertools import combinations

def n_queens_neighbours(state):
    """Takes a state (total assignment) for an n-queen problem
    and returns a sorted list of states that are the neighbours
    of the current assignment.
    """
    neighbours = []
    n = len(state) 
    for i in range(n):
        if i < n-1:
            pos = i + 1
            while pos < n:
                new_state = list(state[:])
                new_state[i], new_state[pos] = new_state[pos], new_state[i]
                neighbours.append(tuple(new_state))
                pos += 1
    return sorted(neighbours)  


def n_queens_cost(state):
    """Takes a state (total assignment) for an n-queen problem
    and returns the number conflicts for that state.
    """
    conflicts = 0
    for pair in list(combinations(state, 2)):
        x1, x2 = pair[0], pair[1]
        y1 = state.index(x1)
        y2 = state.index(x2)
        if abs(x1 - x2) == abs(y1 - y2):
            conflicts += 1
    return conflicts


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
        cost_list = []       
        for neighbour in neighbour_list:
            cost_list.append(cost(neighbour))
        if min(cost_list) < cost(current):
            min_index = cost_list.index(min(cost_list))
            current = neighbour_list[min_index]
            states.append(current)
        else:
            min_cost = True      
    return states


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    """Takes three functions, one to get a new random state and two to
    compute the neighbours or cost of a state and then uses greedy_descent 
    to find a solution.
    """
    current_state = random_state()
    optimal_state = False
    while not optimal_state:
        states = greedy_descent(current_state, neighbours, cost)
        for state in states:
            print(state)
        if cost(states[-1]) > 0:
            print("RESTART")
            current_state = random_state()
        else:
            optimal_state = True
    


# # Example 1
# N = 6
# random.seed(0)

# def random_state():
#     return tuple(random.sample(range(1,N+1), N))   

# greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)


# Example 2
N = 8
random.seed(0)

def random_state():
    return tuple(random.sample(range(1,N+1), N))   

greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)