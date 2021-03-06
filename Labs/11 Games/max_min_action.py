# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:27:35 2020

@author: Amanda
"""

from math import inf


def max_value(tree):
    """Given a game tree, returns the utility of the root of
    the tree when the root is a max node."""
    if type(tree) is int:
        return tree
    v = -inf
    for subtree in tree:
        v = max(v, min_value(subtree))
    return v

    
def min_value(tree):
    """Given a game tree, returns the utility of the root of
    the tree when the root is a min node."""
    if type(tree) is int:
        return tree
    v = inf
    for subtree in tree:
        v = min(v, max_value(subtree))
    return v


def max_action_value(game_tree):
    """Given a game tree, returns a pair where first element is
    the best action and the second element is the utility of the
    root of the tree when the root is a max node.
    """
    if type(game_tree) is int:
        return (None, game_tree)
    max_actions = []
    for i, subtree in enumerate(game_tree):
        max_actions.append((i, min_value(subtree)))
    max_actions.sort(key=lambda x: -x[1])
    return max_actions[0]
    
    
def min_action_value(game_tree):
    """Given a game tree, returns a pair where first element is
    the best action and the second element is the utility of the
    root of the tree when the root is a min node.
    """
    if type(game_tree) is int:
        return (None, game_tree)
    min_actions = []
    for i, subtree in enumerate(game_tree):
        min_actions.append((i, max_value(subtree)))
    min_actions.sort(key=lambda x: x[1])
    return min_actions[0]
    
    
# 1
game_tree = [2, [-3, 1], 4, 1]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)

# 2
game_tree = 3

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)

# 3
game_tree = [1, 2, [3]]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)