# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:45:03 2020

@author: Amanda
"""

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.5
            }},
    
    'B': {
        'Parents': [],
        'CPT': {
            (): 0.5
            }},
    
    'C': {
    'Parents': [],
    'CPT': {
        (): 0.5
        }},
    
    'D': {
    'Parents': ['B'],
    'CPT': {
        (True,): 0.8,
        (False,): 0.2
        }},
    
    'E': {
    'Parents': ['B'],
    'CPT': {
        (True,): 0.2,
        (False,): 0.8
        }},

}
    