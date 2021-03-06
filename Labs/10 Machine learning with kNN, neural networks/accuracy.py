# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:12:53 2020

@author: Amanda
"""

def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given parameters."""
    def perceptron(input):
        a = sum((weights[i] * input[i]) for i in range(len(input))) + bias
        return 1 if a >= 0 else 0
    return perceptron


def accuracy(classifier, inputs, expected_outputs):
    """Passes each input in the sequence of inputs to the given
    classifier function (e.g. a perceptron) and compares the
    predictions with the expected outputs.
    """
    outputs = [classifier(i) for i in inputs]
    matches = sum(1 for i in zip(outputs, expected_outputs) if i[0] == i[1])
    return matches/len(inputs)



# example
perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

print(accuracy(perceptron, inputs, targets))