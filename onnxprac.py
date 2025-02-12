import onnx
import numpy as np
import onnxruntime as ort

# Load the ONNX model
model_path = "ACASXU_run2a_1_2_batch_2000.onnx"  # Replace with your ONNX file path
model = onnx.load(model_path)

# Print model summary
print(onnx.helper.printable_graph(model.graph))

# Get model inputs
for input_tensor in model.graph.input:
    print(f"Input Name: {input_tensor.name}")
    print(f"Input Shape: {input_tensor.type.tensor_type.shape.dim}")

# Get model outputs
for output_tensor in model.graph.output:
    print(f"Output Name: {output_tensor.name}")
    print(f"Output Shape: {output_tensor.type.tensor_type.shape.dim}")

onnx.checker.check_model(model)
print("The model is valid!")

input_data = np.array([0.5, 0.2, 0.1, 1, 0.2], dtype=np.float32)
input_data_reshaped = input_data.reshape(1, 1, 1, 5)
session = ort.InferenceSession(model_path)

input_name = session.get_inputs()[0].name

output = session.run(None, {input_name: input_data_reshaped})


print("Input:", input_data)
print("Output:", output)