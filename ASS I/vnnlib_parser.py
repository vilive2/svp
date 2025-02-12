"""
Author: 
"""

from z3 import *

def vnnlib_parser(filename, X, Y, RELU, Eq, Bound):
    for i in range(5):
        X.append(Real(f'X_{i}'))
        Y.append(Real(f'Y_{i}'))
    
    Bound.extend([
        X[0] <= 0.679857769,
        X[0] >= 0.6,
        X[1] <= 0.5,
        X[1] >= -0.5,
        X[2] <= 0.5,
        X[2] >= -0.5,
        X[3] <= 0.5,
        X[3] >= 0.45,
        X[4] <= -0.45,
        X[4] >= -0.5,
        Y[1] <= Y[0],
        Y[2] <= Y[0],
        Y[3] <= Y[0],
        Y[4] <= Y[0]
    ])