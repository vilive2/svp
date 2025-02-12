from z3 import *
import onnx
import numpy as np

def constraint_adder(layer, relu, eq, bound, x, w, b):
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

X = [
    Real('X_0'), 
    Real('X_1'), 
    Real('X_2'), 
    Real('X_3'), 
    Real('X_4')
]

Y = [
    Real('Y_0'), 
    Real('Y_1'), 
    Real('Y_2'), 
    Real('Y_3'), 
    Real('Y_4')
]

Eq = []
Bound = [
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
]
RELU = []

# Load the ONNX model
model_path = "ACASXU_run2a_1_2_batch_2000.onnx"
model = onnx.load(model_path)

a = X
for i in range(1, len(model.graph.initializer), 2):
    winitializer = model.graph.initializer[i]
    binitializer = model.graph.initializer[i+1]
    layer = i // 2
    
    # Convert the initializer to a numpy array
    w = np.frombuffer(winitializer.raw_data, dtype=np.float32)
    w = w.reshape(winitializer.dims)

    b = np.frombuffer(binitializer.raw_data, dtype=np.float32)
    b = b.reshape(binitializer.dims)

    a = constraint_adder(layer, RELU, Eq, Bound, a, w, b)

Eq.append(Y[0] == a[0])
Eq.append(Y[1] == a[1])
Eq.append(Y[2] == a[2])
Eq.append(Y[3] == a[3])
Eq.append(Y[4] == a[4])

solve(RELU + Bound + Eq)
