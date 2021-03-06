# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:09:56 2020

@author: Amanda
"""

def roulette_wheel_select(population, fitness, r):
    """Takes a list of individuals, a fitness function, and a floating-
    point random number r in the interval [0, 1), and selects and returns
    an individual from the population using the roulette wheel selection
    mechanism.
    """ 
    fitness_list = []
    for x in population:
        fitness_list.append(fitness(x))
    fitness_sum = sum(fitness_list)
    
    totals = []
    running_total = 0
    for n in fitness_list:
        running_total += (n/fitness_sum)
        totals.append(running_total)
    
    for i, x in enumerate(population):
        if r < totals[i]:
            return x


# Example 1
population = ['a', 'b']

def fitness(x):
    return 1 # everyone has the same fitness

for r in [0, 0.33, 0.49999, 0.5, 0.75, 0.99999]:
    print(roulette_wheel_select(population, fitness, r))
   
    
# Example 2
population = [0, 1, 2]

def fitness(x):
    return x

for r in [0, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))