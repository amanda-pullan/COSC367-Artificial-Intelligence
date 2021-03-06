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
    
    
    
    
