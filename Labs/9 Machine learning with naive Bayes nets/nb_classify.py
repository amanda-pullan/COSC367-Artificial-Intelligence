# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:44:45 2020

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


def posterior(prior, likelihood, observation):
    """Returns the posterior probability of the class variable
    being true, given the observation; that is, it returns
    p(Class=true|observation).
    """
    probTrue = prior
    probFalse = 1 - prior
    for i, obs in enumerate(observation):
        if obs:
            probTrue *= likelihood[i][1]
            probFalse *= likelihood[i][0]
        else:
            probTrue *= (1 - likelihood[i][1])
            probFalse *= (1 - likelihood[i][0])
    return probTrue / (probTrue + probFalse)


def nb_classify(prior, likelihood, input_vector):
    """Takes the learnt prior and likelihood probabilities
    and classifies an (unseen) input vector."""
    prob = posterior(prior, likelihood, input_vector)
    if prob <= 0.5:
        answer = ('Not Spam', 1 - prob)
    else:
        answer = ('Spam', prob)
    return answer


# # 1
# prior = learn_prior("spam-labelled.csv")
# likelihood = learn_likelihood("spam-labelled.csv")

# input_vectors = [
#     (1,1,0,0,1,1,0,0,0,0,0,0),
#     (0,0,1,1,0,0,1,1,1,0,0,1),
#     (1,1,1,1,1,0,1,0,0,0,1,1),
#     (1,1,1,1,1,0,1,0,0,1,0,1),
#     (0,1,0,0,0,0,1,0,1,0,0,0),
#     ]

# predictions = [nb_classify(prior, likelihood, vector) 
#                 for vector in input_vectors]

# for label, certainty in predictions:
#     print("Prediction: {}, Certainty: {:.5f}"
#           .format(label, certainty))



# 2
prior = learn_prior("spam-labelled.csv", pseudo_count=1)
likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector) 
                for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))