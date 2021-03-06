"""Creates the concrete class FunkyNumericGraph for the abstract Graph class.
Also implements concrete subclasses DFSFrontier and its subclass BFSFrontier
for the abstract class Frontier from the search module.

Author: Amanda Pullan
Last modified: 18 July 2020

"""

from search import *
from collections import deque
import copy

BLANK = ' '


class SlidingPuzzleGraph(Graph):
    """Objects of this type represent (n squared minus one)-puzzles.
    """

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""
        
        n = len(state) # the size of the puzzle
        i, j = next((i, j) for i in range(n) for j in range(n)
                    if state[i][j] == BLANK) # find the blank tile
        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i-1][j]) # or blank goes up
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i+1][j]) # or blank goes down
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j-1]) # or blank goes left
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], BLANK
            arcs.append(Arc(state, new_state, action, 1))     
        if j < n - 1:
            action = "Move {} left".format(state[i][j+1]) # or blank goes left
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        return [self.starting_state]
    
    def is_goal(self, state):
        """Returns true if the given state is the goal state, False
        otherwise. There is only one goal state in this problem."""
        
        n = len(state)
        count = 0
        for i in range(n):
            for j in range(n):
                if state[i][j] == BLANK:
                    count += 1
                elif state[i][j] == count:
                    count += 1
        return count == n**2


class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""
    
    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs (always two arcs in this problem)"""
        return [Arc(tail_node, tail_node-1, action="1down", cost=1),
                Arc(tail_node, tail_node+2, action="2up", cost=1)]
        
    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the seqence always has one element."""
        return [self.starting_number]

    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal."""
        return node % 10 == 0


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any. If there nothing to return this should raise a
        StopIteration exception.

        """
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration


class BFSFrontier(DFSFrontier):
    """Implements a frontier container appropriate for breadth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty deque."""
        self.container = deque()
  
    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any. If there nothing to return this should raise a
        StopIteration exception.

        """
        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration