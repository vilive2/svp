from z3 import *
from onnx_parser import onnx_parser
from vnnlib_parser import vnnlib_parser

if __name__ == "__main__":
    prop_path = "prop_2.vnnlib"
    model_path = "ACASXU_run2a_1_2_batch_2000.onnx"
    
    X = []
    Y = []
    RELU = []
    Eq = []
    Bound = []

    vnnlib_parser(prop_path, X, Y, RELU, Eq, Bound)
    onnx_parser(model_path, X, Y, RELU, Eq, Bound)

    solve(RELU + Bound + Eq)