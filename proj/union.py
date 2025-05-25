from mytypes import *

def union(A,B):
    
    def tag(prefix, nba):
        states = [prefix + s for s in nba.states]
        initials = [prefix + s for s in nba.initial_states]
        finals = [prefix + s for s in nba.final_states]
        transitions = [(prefix + src, prefix + dst, label) for src, dst, label in nba.transitions]
        return states, initials, finals, transitions

    
    s1, i1, f1, t1 = tag("A_", A)
    s2, i2, f2, t2 = tag("B_", B)

    # Union construction
    states = list(set(s1) | set(s2))
    initials = list(set(i1) | set(i2))
    finals = list(set(f1) | set(f2))
    transitions = list(set(t1) | set(t2))
    alphabets = list(set(A.alphabets) | set(B.alphabets))

    return NBA(states, alphabets, initials, finals, transitions)
