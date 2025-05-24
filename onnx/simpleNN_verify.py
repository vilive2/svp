import random
from z3 import *

w = []

for i in range(12):
    w.append(random.random())
print(w)

x1 = Real('x1')
x2 = Real('x2')
z1 = Real('z1')
z2 = Real('z2')
z3 = Real('z3')
a1 = Real('a1')
a2 = Real('a2')
a3 = Real('a3')
y1 = Real('y1')
y2 = Real('y2')

# Equalities
Eq = [
    z1 == w[0]*x1 + w[3]*x2,
    z2 == w[1]*x1 + w[4]*x2,
    z3 == w[2]*x1 + w[5]*x2,
    y1 == w[6]*a1 + w[8]*a2 + w[10]*a3,
    y2 == w[7]*a1 + w[9]*a2 + w[11]*a3
]

# Bounds
Bound = [
    x1 >= 0,
    x1 < 1,
    x2 >= 0,
    x2 < 1,
    y1 > 1,
]

# RELU constraints
RELU = [
    a1 == If (z1 > 0, z1, 0),
    a2 == If (z2 > 0, z2, 0),
    a3 == If (z3 > 0, z3, 0)
]

solve (RELU + Bound + Eq)