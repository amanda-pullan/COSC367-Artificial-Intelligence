# -*- coding: utf-8 -*-
"""Creates the concrete class LCFS Frontier for the abstract Frontier class.
Also creates a LocationGraph as a subclass of ExplicitGraph.
    
Author: Amanda Pullan
Last modified: 30 Jul 2020
"""

from search import *
from math import sqrt
from heapq import *


class LCFSFrontier(Frontier):
    """Implements a frontier container appropriate for lowest-cost first
    search."""
    
    def __init__(self):
        """ Initialises the container to an empty list."""
        self.container = []
        
    def add(self, path):
        """Adds a new path into the container."""
        if len(path) < 2 or path[-2].tail != path[-1].head:
            total_cost = 0
            for arc in path:
                total_cost += arc.cost
            current = [total_cost, path]
            heappush(self.container, current)
        
    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any. If there nothing to return this should raise a
        StopIteration exception.
        """
        if  len(self.container) > 0:
            cost, path = heappop(self.container)
            return path
        else:
            raise StopIteration


class LocationGraph(ExplicitGraph):
    """Creates a LocationGraph object representing nodes with different
    locations and distances between them."""
    
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes):
        """"Initialises a location graph.
        Keyword arguments:
        nodes -- a set of nodes
        locations -- a tuple containing the location of each node
        edge_list -- a set of tuples containing bi-directional edges
        starting_nodes -- the list of starting nodes
        goal_nodes -- the set of goal nodes
        """        
        self.nodes = nodes
        self.locations = locations
        self.edges = edges
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
    
    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects that go out from the given
        node"""
        arcs = []
        for tail, head in self.edges:
            loc1 = self.locations[tail]
            loc2 = self.locations[head]
            cost = sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)
            if tail == node:
                arcs.append(Arc(tail, head, str(tail) + '->' + str(head), cost))
            elif head == node and (head, tail) not in self.edges:
                arcs.append(Arc(head, tail, str(head) + '->' + str(tail), cost))
        return sorted(arcs, key=lambda arc: arc[1])