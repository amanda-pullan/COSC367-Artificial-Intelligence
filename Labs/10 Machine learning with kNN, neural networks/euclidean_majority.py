# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:03:30 2020

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


# # Examples
print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))
print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
print(majority_element("ababc") in "ab")
