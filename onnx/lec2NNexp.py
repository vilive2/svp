from z3 import *

# Define variables
x1 = Real('x1')
x2w = Real('x2w')
x3w = Real('x3w')
x2a = Real('x2a')
x3a = Real('x3a')
x4 = Real('x4')

# Equalities
Eq = [
    x2w == x1,
    x3w == -x1,
    x4 == x2a + x3a
]

# Bounds
Bound = [
    x1 >= 0,
    x1 <= 1,
    x2a >= 0,
    x3a >= 0
]

# RELU constraints
RELU = [
    x2a == If(x2w > 0, x2w, 0),
    x3a == If(x3w > 0, x3w, 0)
]

# OR Constraint
OrConstraint = [Or(x4 < 0.5, x4 > 1)]

print(RELU + Bound + Eq + OrConstraint)
# Solve with all constraints
solve(RELU + Bound + Eq + OrConstraint)
