# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:38:13 2020

@author: Amanda
"""

def euclidean_distance(v1, v2):
    """Returns the Euclidean distance between the points
    represented by v1 and v2."""
    return sum([(v1[i]-v2[i])**2 for i in range(len(v1))])**(1/2)


def majority_element(labels):
    """Returns the label that has the highest frequency
    (most common)."""
    return max(set(labels), key=labels.count)


def knn_predict(input, examples, distance, combine, k):
    """Takes an input and predicts the output by combining the
    output of the k nearest neighbours."""
    distances = [distance(input, example[0]) for example in examples]
    sorted_distances = sorted(enumerate(distances), key=lambda x: x[1])
    if k + 1 < len(sorted_distances):
        while sorted_distances[k-1][1] == sorted_distances[k][1]:
            k += 1
    elif k == len(sorted_distances) - 1:
        if sorted_distances[k-1][1] == sorted_distances[k][1]:
            k += 1
    nearest_neighbs = sorted_distances[:k]
    outputs = []
    for i in range(k):
        j = nearest_neighbs[i][0]
        outputs.append(examples[j][1])
    return combine(outputs)



# test example

examples = [
    ([2,1], 3.8),
    ([3,-1], -2.2),
    ([-4,-2], 7.0),
    ([5,3], 0.5),
    ([1,-1], -4.9),
    ([-2,1], 1.1),
]

def average(values):
    return sum(values) / len(values)

distance = euclidean_distance
combine = average

print(knn_predict((-10,8), examples, distance, combine, 5))


# example 1
examples = [
    ([2], '-'),
    ([3], '-'),
    ([5], '+'),
    ([8], '+'),
    ([9], '+'),
]

distance = euclidean_distance
combine = majority_element

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print(x, knn_predict([x], examples, distance, combine, k))
    print()

# example 2
# using knn for predicting numeric values

examples = [
    ([1], 5),
    ([2], -1),
    ([5], 1),
    ([7], 4),
    ([9], 8),
]

def average(values):
    return sum(values) / len(values)

distance = euclidean_distance
combine = average

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
    print()