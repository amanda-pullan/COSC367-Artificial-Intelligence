# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:41:25 2020

@author: Amanda
"""

import itertools


def joint_prob(network, assignment):
    """Given a belief network and a complete assignment of all
    the variables in the network, returns the probability of the
    assignment.
    """
    prob = 1
    for a_key in assignment:
        conditions = []
        current = network[a_key]
        for parent in current['Parents']:
            conditions.append(True) if assignment[parent] else conditions.append(False)
        conditions = tuple(conditions)
        if not assignment[a_key]:
            prob *= (1 - current['CPT'].get(conditions))
        else:
            prob *= (current['CPT'].get(conditions))   
    return prob



def query(network, query_var, evidence):
    """Given a belief network, the name of a variable in
    the network, and some evidence, returns the posterior
    distribution of query_var.
    """
    
    queryTrue = {query_var: True}
    queryTrue.update(evidence)
    probsTrue = []  
    queryFalse = {query_var: False}
    queryFalse.update(evidence)
    probsFalse = []
    
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    for values in itertools.product((True, False), repeat=len(hidden_vars)):
        hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
        currentTrue = {**queryTrue, **hidden_assignments}
        probsTrue.append(joint_prob(network, currentTrue))
        currentFalse = {**queryFalse, **hidden_assignments}
        probsFalse.append(joint_prob(network, currentFalse)) 
    alpha = 1 / (sum(probsTrue) + sum(probsFalse))
    probTrue = alpha * sum(probsTrue)
    probFalse = alpha * sum(probsFalse)
    
    return {True: probTrue, False: probFalse}
    
    
    
    


# # Example 1
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

answer = query(network, 'A', {})
print("P(A=true) = {:.5f}".format(answer[True]))
print("P(A=false) = {:.5f}".format(answer[False]))

# 	
# # Example 2
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
answer = query(network, 'B', {'A': False})
print("P(B=true|A=false) = {:.5f}".format(answer[True]))
print("P(B=false|A=false) = {:.5f}".format(answer[False]))


# Example 3
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
answer = query(network, 'B', {})
print("P(B=true) = {:.5f}".format(answer[True]))
print("P(B=false) = {:.5f}".format(answer[False]))

# 	
# # Example 4
network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

answer = query(network, 'Burglary', {'John': True, 'Mary': True})
print("Probability of a burglary when both\n"
      "John and Mary have called: {:.3f}".format(answer[True]))                        

 	
# Example 5
network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

answer = query(network, 'John', {'Mary': True})
print("Probability of John calling if\n"
      "Mary has called: {:.5f}".format(answer[True]))                       
