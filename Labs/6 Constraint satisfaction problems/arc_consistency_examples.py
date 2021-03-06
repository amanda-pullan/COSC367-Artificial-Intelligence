# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:23:34 2020

@author: Amanda
"""

from csp import CSP

crossword_puzzle = CSP(
    var_domains={
        # read across:
        'a1': set("bus,has".split(',')),
        'a3': set("year,lane".split(',')),
        'a4': set("car,ant".split(',')),
        # read down:
        'd1': set("buys,hold".split(',')),
        'd2': set("search,syntax".split(',')),
        },
    constraints={
        lambda a1, d1: a1[0] == d1[0],
        lambda d1, a3: d1[2] == a3[0],
        lambda a1, d2: a1[2] == d2[0],
        lambda d2, a3: d2[2] == a3[2],
        lambda d2, a4: d2[4] == a4[0],
        })
    

canterbury_colouring = CSP(
    var_domains={
        'christchurch': {'red', 'green'},
        'selwyn': {'red', 'green'},
        'waimakariri': {'red', 'green'},
        },
    constraints={
        lambda christchurch, waimakariri: christchurch != waimakariri,
        lambda christchurch, selwyn: christchurch != selwyn,
        lambda selwyn, waimakariri: selwyn != waimakariri,
        })