from z3 import *

X_0 = Real('X_0')
X_1 = Real('X_1')
X_2 = Real('X_2')
X_3 = Real('X_3')
X_4 = Real('X_4')

Y_0 = Real('Y_0')
Y_1 = Real('Y_1')
Y_2 = Real('Y_2')
Y_3 = Real('Y_3')
Y_4 = Real('Y_4')

# Bounds
Bound = [
    X_0 <= 0.679857769,
    X_0 >= 0.6,
    X_1 <= 0.5,
    X_1 >= -0.5,
    X_2 <= 0.5,
    X_2 >= -0.5,
    X_3 <= 0.5,
    X_3 >= 0.45,
    X_4 <= -0.45,
    X_4 >= -0.5
]

# Equalities
Eq = [
    Y_1 <= Y_0,
    Y_2 <= Y_0,
    Y_3 <= Y_0,
    Y_4 <= Y_0
]