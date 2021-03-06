# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 20:08:55 2020

@author: Amanda
"""

from csp import *




cryptic_puzzle = CSP(
    var_domains = {x: set(range(0, 10)) for x in 'twofur'},
    constraints = {
        lambda t: t > 0,
        lambda f: f > 0,
        lambda t,w,o,f,u,r: len([t,w,o,f,u,r]) == len(set([t,w,o,f,u,r])),
        lambda t,w,o,f,u,r: (t*100 + w*10 + o) == (f*1000 + o*100 + u*10 + r)/2})



# # test 1
# print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
# print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twour"))

# # test 2
# new_csp = arc_consistent(cryptic_puzzle)
# print(sorted(new_csp.var_domains['r']))
# # [0, 2, 4, 6, 8]

# test 3
new_csp = arc_consistent(cryptic_puzzle)
print(sorted(cryptic_puzzle.var_domains['w']))

# # test 4
# from collections import OrderedDict
# new_csp = arc_consistent(cryptic_puzzle)
# solutions = []
# for solution in generate_and_test(new_csp):
#     solutions.append(sorted((x, v) for x, v in solution.items()
#                             if x in "twofur"))
# print(len(solutions))
# solutions.sort()
# print(solutions[0])
# print(solutions[5])