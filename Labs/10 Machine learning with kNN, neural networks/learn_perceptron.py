# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:28:35 2020

@author: Amanda
"""

def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given parameters."""
    def perceptron(input):
        a = sum((weights[i] * input[i]) for i in range(len(input))) + bias
        output = 0
        if a >= 0:
            output = 1
        return output
    return perceptron


def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    """Adjusts the weights and bias by iterating through the training
    data and applying the perceptron learning rule."""
    perceptron = construct_perceptron(weights, bias)
    epochs = 0
    while epochs <= max_epochs:
        for x, t in training_examples:
            y = perceptron(x)
            if t != y:
                weights = [(weights[i] + learning_rate * x[i] * (t-y)) for i in range(len(x))]
                bias += learning_rate * (t - y)
                perceptron = construct_perceptron(weights, bias)
        epochs += 1
    return (weights, bias)
                    

# weights = [-0.5, 0.5]
# bias = -0.5
# learning_rate = 0.5

# examples = [
#     ([1, 1],   0),    # index 0 (first example)
#     ([2, 0],   1),
#     ([1, -1],  0),
#     ([-1, -1], 1),
#     ([-2, 0],  0),
#     ([-1, 1],  1),
# ]

# weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, 100)
# print(f"Weights: {weights}")
# print(f"Bias: {bias}\n")

# example 1
weights = [2, -4]
bias = 0
learning_rate = 0.5
examples = [
  ((0, 0), 0),
  ((0, 1), 0),
  ((1, 0), 0),
  ((1, 1), 1),
  ]
max_epochs = 50

weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")

perceptron = construct_perceptron(weights, bias)

print(perceptron((0,0)))
print(perceptron((0,1)))
print(perceptron((1,0)))
print(perceptron((1,1)))
print(perceptron((2,2)))
print(perceptron((-3,-3)))
print(perceptron((3,-1)))

# # example 2
# weights = [2, -4]
# bias = 0
# learning_rate = 0.5
# examples = [
#   ((0, 0), 0),
#   ((0, 1), 1),
#   ((1, 0), 1),
#   ((1, 1), 0),
#   ]
# max_epochs = 50

# weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
# print(f"Weights: {weights}")
# print(f"Bias: {bias}\n")