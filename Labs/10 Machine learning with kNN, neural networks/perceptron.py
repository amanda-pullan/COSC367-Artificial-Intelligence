# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:50:55 2020

@author: Amanda
"""

def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given parameters."""
    def perceptron(input):
        a = sum((weights[i] * input[i]) for i in range(len(input))) + bias
        return 0 if a < 0 else 1
    return perceptron


weights = [-0.5, 0.5]
bias = -0.5
perceptron = construct_perceptron(weights, bias)

print(perceptron([1, 1]))

print(0.5+(0.5*1))


# # example 1
# weights = [2, -4]
# bias = 0
# perceptron = construct_perceptron(weights, bias)

# print(perceptron([1, 1]))
# print(perceptron([2, 1]))
# print(perceptron([3, 1]))
# print(perceptron([-1, -1]))

# # example 2
# weights = [3, 5]
# bias = 1
# perceptron = construct_perceptron(weights, bias)

# print(perceptron([0, 0]))
# print(perceptron([1, -1]))
# print(perceptron([-1, 1]))

