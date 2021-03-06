# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:57:11 2020

@author: Amanda
"""

from math import inf


def max_value(tree):
    """Given a game tree, returns the utility of the root of
    the tree when the root is a max node."""
    if type(tree) is int:
        return tree
    v = -inf
    for x in tree:
        v = max(v, min_value(x))
    return v

    
def min_value(tree):
    """Given a game tree, returns the utility of the root of
    the tree when the root is a min node."""
    if type(tree) is int:
        return tree
    v = inf
    for x in tree:
        v = min(v, max_value(x))
    return v
    


game_tree = 3
print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))

game_tree = [1, 2, 3]
print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))

game_tree = [1, 2, [3]]
print(min_value(game_tree))
print(max_value(game_tree))

game_tree = [[1, 2], [3]]
print(min_value(game_tree))
print(max_value(game_tree))