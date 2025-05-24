import onnx
import numpy as np
import onnxruntime as ort

# Load the ONNX model
model_path = "ACASXU_run2a_1_2_batch_2000.onnx"  # Replace with your ONNX file path
model = onnx.load(model_path)

# Print model summary
# print(onnx.helper.printable_graph(model.graph))

# Get model inputs
# for input_tensor in model.graph.input:
#     print(f"Input Name: {input_tensor.name}")
#     print(f"Input Shape: {input_tensor.type.tensor_type.shape.dim}")

# Get model outputs
# for output_tensor in model.graph.output:
#     print(f"Output Name: {output_tensor.name}")
#     print(f"Output Shape: {output_tensor.type.tensor_type.shape.dim}")

# onnx.checker.check_model(model)
# print("The model is valid!")

# for layer in model.layers:
#     weights, biases = layer.get_weights()
#     print(f"Layer: {layer.name}")
#     print(f"Weights: {weights}")
#     print(f"Biases: {biases}")
#     print("----------")

print(len(model.graph.initializer))

for initializer in model.graph.initializer:
    # Print the name of the parameter (weight/bias) and its shape
    print(f"Parameter: {initializer.name}")
    print(f"Shape: {initializer.dims}")
    
    # Convert the initializer to a numpy array
    arr = np.frombuffer(initializer.raw_data, dtype=np.float32)
    arr = arr.reshape(initializer.dims)  # Reshape the array to match the dimensions
    
    # Print the array (weights/biases)
    print(f"Values:\n{arr}\n")