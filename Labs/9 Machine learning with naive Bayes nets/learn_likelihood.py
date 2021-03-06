# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:12:44 2020

@author: Amanda
"""

import csv


def learn_likelihood(file_name, pseudo_count=0):
    """Takes the file name of a training set (for the spam
    detection problem) and an optional pseudo-count parameter
    and returns a sequence of pairs of likelihood probabilities.
    """
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    
    y_true = 0
    true_indices = []
    false_indices = []
    rows = len(training_examples)
    
    for i in range(1, rows):
        if int(training_examples[i][-1]) == 1:
            y_true += 1
            true_indices.append(i)
        else:
            false_indices.append(i)
    y_false = rows - (1 + y_true) + (pseudo_count * 2)
    y_true += pseudo_count * 2
    
    counts_true = [0] * (len(training_examples[0]) - 1)
    counts_false = [0] * (len(training_examples[0]) - 1)
    
    for i in range(len(counts_true)):
        count_true = pseudo_count
        for j in true_indices:
            if int(training_examples[j][i]) == 1:
                count_true += 1
        counts_true[i] = count_true / y_true
                
        count_false = pseudo_count
        for k in false_indices:
            if int(training_examples[k][i]) == 1:
                count_false += 1       
        counts_false[i] = count_false / y_false
            
    probs = []
    for i in range(len(counts_true)):
        probs.append((counts_false[i], counts_true[i]))
    
    return probs
    
        
    
               
   
    
   
#learn_likelihood("spam-labelled.csv")
   
# # 1
# likelihood = learn_likelihood("spam-labelled.csv")
# print(len(likelihood))
# print([len(item) for item in likelihood])


# 2
likelihood = learn_likelihood("spam-labelled.csv")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

 	
#3
likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)
print("With Laplacian smoothing:")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))