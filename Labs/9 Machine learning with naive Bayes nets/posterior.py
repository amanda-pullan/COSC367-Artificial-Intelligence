# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:47:13 2020

@author: Amanda
"""


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
        




# # Example 1
# prior = 0.05
# likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))
# observation = (True, True, True)
# posterior(prior, likelihood, observation)
# class_posterior_true = posterior(prior, likelihood, observation)
# print("P(C=False|observation) is approximately {:.5f}"
#       .format(1 - class_posterior_true))
# print("P(C=True |observation) is approximately {:.5f}"
#       .format(class_posterior_true))  

# 	
# # Example 2
# prior = 0.05
# likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

# observation = (True, False, True)

# class_posterior_true = posterior(prior, likelihood, observation)
# print("P(C=False|observation) is approximately {:.5f}"
#       .format(1 - class_posterior_true))
# print("P(C=True |observation) is approximately {:.5f}"
#       .format(class_posterior_true))  

# 	
# # Example 3
# prior = 0.05
# likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

# observation = (False, False, True)

# class_posterior_true = posterior(prior, likelihood, observation)
# print("P(C=False|observation) is approximately {:.5f}"
#       .format(1 - class_posterior_true))
# print("P(C=True |observation) is approximately {:.5f}"
#       .format(class_posterior_true))  

# 	
# # Example 4
# prior = 0.05
# likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

# observation = (False, False, False)

# class_posterior_true = posterior(prior, likelihood, observation)
# print("P(C=False|observation) is approximately {:.5f}"
#       .format(1 - class_posterior_true))
# print("P(C=True |observation) is approximately {:.5f}"
#       .format(class_posterior_true))  