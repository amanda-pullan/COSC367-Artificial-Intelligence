# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:30:38 2020

@author: Amanda
"""

import random


def depth(expression):
    """Takes an expression (that follows our definition of expression)
    and returns the depth of the expression tree."""
    if type(expression) in [int, str]:
        return 0
    return max(depth(expression[1]), depth(expression[2])) + 1
    
            
def evaluate(expression, bindings):
    """Takes an expression and a dictionary of bindings and returns
    an integer that is the value of the expression."""
    if type(expression) is int:
        return expression
    elif type(expression) is str:
        return bindings[expression]
    func = bindings[expression[0]]
    arg1 = evaluate(expression[1], bindings)
    arg2 = evaluate(expression[2], bindings)
    return func(arg1, arg2)


def random_expression(function_symbols, leaves, max_depth):
    """Randomly generates an expression."""
    if max_depth <= 0:
        return random.choice(leaves)  
    n = random.randint(0, max_depth) 
    if n % 2 == 1:
        return random.choice(leaves)  
    elif n % max_depth == 0:
        left_tree = random_expression(function_symbols, leaves, n-1)
        right_tree = random_expression(function_symbols, leaves, n-1)
        return [random.choice(function_symbols), left_tree, right_tree] 
    else:
        left_tree = random_expression(function_symbols, leaves, n)
        right_tree = random_expression(function_symbols, leaves, n)
        return [random.choice(function_symbols), left_tree, right_tree]


def generate_rest(initial_sequence, expression, length_to_generate):
    """Returns a list of integers with the specified length that
    is the continuation of the initial list according to the given
    expression.
    """
    n = len(initial_sequence)
    sequence = initial_sequence[:]
    bindings = {"*": lambda x, y: x * y,
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y}
    
    for l in range(n, n + length_to_generate):
        bindings['x'] = sequence[-2]
        bindings['y'] = sequence[-1]
        bindings['i'] = l
        sequence.append(evaluate(expression, bindings)) 
        
    return sequence[n:]


def predict_rest(sequence):
    """Takes a sequence of integers of length at least 5, finds the
    pattern in the sequence, and "predicts" the rest by returning a
    list of the next five integers in the sequence.
    """
    random.seed(1995)
    function_symbols = ('*', '+', '-')
    leaves = list(range(-2, 3)) + ['i', 'x', 'y'] 
    test = []
    while test != sequence:
        expression = random_expression(function_symbols, leaves, 3)
        test = sequence[:2] + generate_rest(sequence[:2], expression, len(sequence)-2) 
    return generate_rest(sequence, expression, 5)


def is_valid_expression(object, function_symbols, leaf_symbols):
    """Takes an object as its first argument and tests whether it is
    a valid expression according to the definition of expressions in
    this assignment.
    """
    if type(object) is int or (type(object) is str and object in leaf_symbols):
        return True
    elif type(object) is list and len(object) == 3:
        if type(object[0]) is str and object[0] in function_symbols:
            for i in range(1,3):
                if is_valid_expression(object[i], function_symbols, leaf_symbols):
                    return True
    return False


sequence = [1, 3, -5, 13, -31, 75, -181, 437]
print(predict_rest(sequence))