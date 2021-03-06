# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 14:53:56 2020

@author: Amanda
"""
from csp import *
from generate_and_test import *

def print_relations(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x: v for x, v in zip(names, values)}
        for constraint in csp.constraints:
            if satisfies(assignment, constraint):
                current = [scope(constraint)]
                for i in scope(constraint):
                    current.append(assignment[i])
                print(current)

# ## example
# # CSP form
# CSP(
#    var_domains = {var:{0,1,2} for var in 'ab'},
#    constraints = {
#       lambda a, b:  a > b,
#       lambda b: b > 0,
#    })

# # relational form
# [
#     Relation(header=['a', 'b'],
#              tuples={(2, 0),
#                      (1, 0),
#                      (2, 1)}),
    
#     Relation(header=['b'],
#              tuples={(2,),
#                      (1,)})
# ]


# # question 5
# csp = CSP(
#    var_domains = {var:{0,1,2} for var in 'abcd'},
#    constraints = {
#       lambda a, b, c: a > b + c,
#       lambda c, d: c > d
#       }
#    )


# relations = [
#     Relation(header = ['a', 'b', 'c'],
#              tuples = {(1, 0, 0),
#                        (2, 0, 0),
#                        (2, 0, 1),
#                        (2, 1, 0)}),
    
#     Relation(header = ['c', 'd'],
#              tuples = {(0, 1),
#                        (0, 2),
#                        (1, 2)}),
# ]


# print(len(relations))
# print(all(type(r) is Relation for r in relations))


# question 6
csp = CSP(
   var_domains = {var:{-1,0,1} for var in 'abcd'},
   constraints = {
      lambda a, b: a == abs(b),
      lambda c, d: c > d,
      lambda a, b, c: a * b > c + 1
      }
   )

print_relations(csp)

relations = [
    Relation(header = ['a', 'b'],
             tuples = {(0, 0),
                       (1, -1),
                       (1, 1)}),
    
    Relation(header = ['c', 'd'],
             tuples = {(0, -1),
                       (1, 0),
                       (1, -1)}),
    
    Relation(header = ['a', 'b', 'c'],
             tuples = {(-1, -1, -1),
                       (1, 1, -1)})
    ] 

relations_after_elimination = [
    Relation(header = ['b', 'c'],
             tuples = {(1, -1)}),
    
    Relation(header = ['c', 'd'],
         tuples = {(0, -1),
                   (1, 0),
                   (1, -1)})
    ]

print(len(relations))
print(all(type(r) is Relation for r in relations))






