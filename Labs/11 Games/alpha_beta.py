# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:01:21 2020

@author: Amanda
"""

from math import inf


def max_value(tree, alpha, beta):
    """Given a game tree, returns the utility of the root of
    the tree when the root is a max node."""
    if type(tree) is int:
        return tree
    v = -inf
    for x in tree:
        v = max(v, min_value(x, alpha, beta))
        alpha = max(v, alpha)
        if alpha >= beta:
            return v
    return v

    
def min_value(tree, alpha, beta):
    """Given a game tree, returns the utility of the root of
    the tree when the root is a min node."""
    if type(tree) is int:
        return tree
    v = inf
    for x in tree:
        v = min(v, max_value(x, alpha, beta))
        beta = min(v, beta)
        if alpha >= beta:
            return v
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


def alpha_beta_search(tree):
    v = max_action_value(tree, -inf, inf)
    return v

print(alpha_beta_search([2, [-1, 5], [1, 3], 4]))