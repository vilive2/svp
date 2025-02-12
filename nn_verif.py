from z3 import *
import onnx

# Load the ONNX model


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