# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:51:59 2020

@author: Amanda
"""

import csv

def learn_prior(file_name, pseudo_count=0):
    """Takes the file name of the training set and an optional
    pseudo-count parameter and returns a real number that is
    the prior probability of spam being true.
    """
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
        
    prob = 0
    rows = len(training_examples)
    for i in range(1, rows):
        if int(training_examples[i][-1]) == 1:
            prob += 1     
            
    return (prob + pseudo_count) / ((rows - 1) + (pseudo_count * 2))
    
    
    
#learn_prior("spam-labelled.csv")

# 1   
prior = learn_prior("spam-labelled.csv")
print("Prior probability of spam is {:.5f}.".format(prior))

#2
prior = learn_prior("spam-labelled.csv")
print("Prior probability of not spam is {:.5f}.".format(1 - prior))

# 3
prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
print(format(prior, ".5f"))

# 4
prior = learn_prior("spam-labelled.csv", pseudo_count = 2)
print(format(prior, ".5f"))

# 5
prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
print(format(prior, ".5f"))

# 6
prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
print(format(prior, ".5f"))

# 7
prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
print(format(prior, ".5f"))