# -*- coding: utf-8 -*-
"""Creates the concrete subclass RoutingGraph for the abstract Graph class
from the search module and the AStarFrontier to find the best path from agent
to customer.

Author: Amanda Pullan
Last modified: 21 August 2020
"""

from search import *
import math
from heapq import *

class RoutingGraph(Graph):
    """A concrete subclass of Graph that takes a grid-like textual map
    input and represents it as a graph."""
    
    def __init__(self, state):
        """Initialises a routing graph. Keyword argument state takes
        the input text map representation.
        """
        self.state = [line.strip() for line in state.splitlines()]
        self.row_lim = len(self.state) - 1
        self.col_lim = len(self.state[0]) - 1
        self.agents = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'S'}
        self.goal_nodes = []
        for row, line in enumerate(self.state):
            indices = [i for i, val in enumerate(line) if val == 'G']
            for col in indices:
                self.goal_nodes.append((row, col))
    
    def starting_nodes(self):
        """Returns a sequence of the starting nodes."""
        start_nodes = []
        for row, line in enumerate(self.state):
            indices = [i for i, val in enumerate(line) if val in self.agents]
            for col in indices:
                fuel = math.inf if line[col] == 'S' else int(line[col])
                start_nodes.append((row, col, fuel))
        return start_nodes
        
    def is_goal(self, node):
        """Returns true if the input node is a goal node."""
        node_row, node_col, fuel = node
        return (node_row, node_col) in self.goal_nodes
    
    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects that are going out
        from the input node."""
        movements = [('N' , -1, 0),
                     ('E' ,  0, 1),
                     ('S' ,  1, 0),
                     ('W' ,  0, -1)] 
        row, col, fuel = node
        arcs = []
        for direction, vert_pos, horiz_pos in movements:
            new_row = row + vert_pos
            new_col = col + horiz_pos
            if 0 < new_row < self.row_lim and 0 < new_col < self.col_lim:
                if self.state[new_row][new_col] != "X" and 0 < fuel:
                    new_pos = (new_row, new_col, fuel - 1)
                    arcs.append(Arc(node, new_pos, direction, 5))
        if self.state[row][col] == "F" and fuel < 9:
            arcs.append(Arc(node, (row, col, 9), 'Fuel up', 15))
        return arcs
                    
    def estimated_cost_to_goal(self, node):
        "Uses the Manhattan distance as a cost heuristic."
        costs = []
        row, col, fuel = node
        for goal in self.goal_nodes:
            g_row, g_col = goal
            cost = abs(row - g_row) + abs(col - g_col)
            costs.append(cost)
        return min(costs) * 5
    

class AStarFrontier(Frontier):
    """Implements a frontier using the A* heuristic"""
    def __init__(self, graph):
        self.graph = graph
        self.container = []
        self.expanded = []
        self.priority = 0
        
    def add(self, path):
        """Adds a new path into the container."""
        if path[-1].head not in self.expanded:
            total_cost = self.graph.estimated_cost_to_goal(path[-1].head)
            for arc in path:
                total_cost += arc.cost
            self.priority += 1
            current = [total_cost, self.priority, path]
            heappush(self.container, current)
        
    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any."""
        if  len(self.container) > 0:
            cost, priority, path = heappop(self.container)
            if path[-1].head not in self.expanded:
                self.expanded.append(path[-1].head)
                return path
            else:
                return next(self)
        else:
            raise StopIteration

def print_map(graph, frontier, solution):
    """Prints the map graph and the search paths taken"""
    graph_str = graph.state    
    for node in frontier.expanded:
        row, col, fuel = node
        if graph_str[row][col] not in {'G', 'S'}:
            current = graph_str[row][:col] + "." + graph_str[row][col+1:]
            graph_str[row] = current   
    if solution is not None:
        for arc in solution[1:-1]:
            row, col = arc.head[:2]
            current = graph_str[row][:col] + "*" + graph_str[row][col+1:]
            graph_str[row] = current 
    for line in graph_str:
        print(line)
        