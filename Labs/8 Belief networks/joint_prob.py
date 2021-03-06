# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 20:18:25 2020

@author: Amanda
"""

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


    

# Example 1
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': True})
print("{:.5f}".format(p))

# Example 2
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': False})
print("{:.5f}".format(p))

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
 
p = joint_prob(network, {'A': False, 'B':True})
print("{:.5f}".format(p)) 

# Example 4
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
 
p = joint_prob(network, {'A': False, 'B':False})
print("{:.5f}".format(p))

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

p = joint_prob(network, {'John': True, 'Mary': True,
                          'Alarm': True, 'Burglary': False,
                          'Earthquake': False})
print("{:.8f}".format(p))                        
