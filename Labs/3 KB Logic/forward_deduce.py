# -*- coding: utf-8 -*-
"""Implements the functions clauses and forward_deduce which together take the
string of a knowledge base, parse the definite clauses and return a complete
set of atoms derivable from the knowledge base.

Author: Amanda Pullan
Last modified: 2 August 2020
"""

import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 31 Jul 2019

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")
        

def forward_deduce(kb):
    """Uses the knowledge base output from clauses function containing
    propositional definite clauses and returns a (complete) set of atoms
    (strings) that can be derived (to be true) from the knowledge base.
    """
    knowledge_base = list(clauses(kb))
    consequences = []
    found_all = False
    while not found_all:
        checked = 0
        for head, body in knowledge_base:
            if head in consequences:
                checked += 1
            else:
                count = 0
                for atom in body:
                    if atom in consequences:
                        count += 1
                if len(body) == count:
                    consequences.append(head)
                else:
                    checked += 1
        if checked == len(knowledge_base):
            found_all = True
    return consequences
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        