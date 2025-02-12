"""
Author: Vivek Kumar
"""

from z3 import *
import onnx
import numpy as np

def constraint_adder(layer, RELU, Eq, Bound, X, W, B):
    m = len(B)
    a = [Real(f'x{layer}a{i}') for i in range(m)]
    z = [Real(f'x{layer}z{i}') for i in range(m)]

    wx = np.dot(X, W)
    wxplusb = wx + B

    for i in range(m):
        Eq.append(z[i] == wxplusb[i])
        RELU.append(a[i] == If(z[i] > 0, z[i], 0))
        Bound.append(a[i] >= 0)

    return a

def onnx_parser(filename, X, Y, RELU, Eq, Bound):
    model = onnx.load(filename)

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

    for i in range(len(Y)):
        Eq.append(Y[i] == a[i])