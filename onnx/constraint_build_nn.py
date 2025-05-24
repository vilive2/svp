from z3 import *
import numpy as np

def constraint_adder(layer, relu, eq, bound, x, w, b):
    print(relu, eq, bound, x, w, b)

    m = len(b)
    a = [Real(f'x{layer}a{i}') for i in range(m)]
    z = [Real(f'x{layer}z{i}') for i in range(m)]

    wx = np.dot(x, w)
    wxplusb = wx + b    

    for i in range(m):
        eq.append(z[i] == wxplusb[i])
        relu.append(a[i] == If(z[i] > 0, z[i], 0))
        bound.append(a[i] >= 0)

    return a

x = [Real('xia0')]
w0 = [[1, -1]]
b0 = [0, 0]

w1 = [[1], [1]]
b1 = [0]

Eq = []
Bound = [
    x[0] >= 0,
    x[0] <= 1
]
RELU = []

a1 = constraint_adder(1, RELU, Eq, Bound, x, w0, b0)
y = constraint_adder('o', RELU, Eq, Bound, a1, w1, b1)

OrConstraint = [Or(y[0] < 0.5, y[0] > 1)]

print(RELU + Bound + Eq + OrConstraint)

solve(RELU + Bound + Eq + OrConstraint)