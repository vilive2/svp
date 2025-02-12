from z3 import *
# from numpy import Inf

x1 = Real('x1')
x2w = Real ('x2w')
x2a = Real ('x2a')
x3w = Real ('x3w')
x3a = Real ('x3a')
x4 = Real ('x4')

#Equalities
Eq = [
    x2w == x1,
    x3w == -x1,
    x4 - x3a -x2a == 0
]

#Bounds
Bound = [
    x1 >= 0,
    x1 <= 1,
    x4 < 0,
    x2a >= 0,
    x3a >= 0    
]

#RELU constraints
RELU =[
    x2a == If (x2w > 0, x2w, 0),
    x3a == If (x3w > 0, x3w, 0)
]

solve (RELU + Bound + Eq)