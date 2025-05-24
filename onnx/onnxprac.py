import onnx
import numpy as np
import onnxruntime as ort

# Load the ONNX model
model_path = "ACASXU_run2a_1_2_batch_2000.onnx"  # Replace with your ONNX file path
model = onnx.load(model_path)

# Print model summary
# print(onnx.helper.printable_graph(model.graph))

# # Get model inputs
# for input_tensor in model.graph.input:
#     print(f"Input Name: {input_tensor.name}")
#     print(f"Input Shape: {input_tensor.type.tensor_type.shape.dim}")

# # Get model outputs
# for output_tensor in model.graph.output:
#     print(f"Output Name: {output_tensor.name}")
#     print(f"Output Shape: {output_tensor.type.tensor_type.shape.dim}")

# onnx.checker.check_model(model)
# print("The model is valid!")
X_0 = 0.6
dx0 = (0.679857769 - 0.6) / 10
tested = 0
for _ in range(10):
    X_1 = -0.5
    dx1 = (0.5+0.5)/10
    for __ in range(10):
        X_2 = -0.5
        dx2 = (0.5+0.5)/10
        for ___ in range(10):
            X_3 = 0.45
            dx3 = (0.5-0.45)/10
            for ____ in range(10):
                X_4 = -0.5
                dx4 = (-0.45+0.5)/10
                for _____ in range(10):
                    input_data = np.array([X_0, X_1, X_2, X_3, X_4], dtype=np.float32)
                    input_data_reshaped = input_data.reshape(1, 1, 1, 5)
                    session = ort.InferenceSession(model_path)

                    input_name = session.get_inputs()[0].name

                    output = session.run(None, {input_name: input_data_reshaped})
                    output = np.array(output[0])[0]
                    if output[0] >= output[1] and output[0] >= output[2] and output[0] >= output[3] and output[0] >= output[4]:
                        print("UNSAFE", end=' ')
                        print("Input:", input_data)
                        print("Output:", output)
                    X_4 += dx4
                    tested += 1
                    print(f"\rTested: {tested}", end='')
                X_3 += dx3
            X_2 += dx2
        X_1 += dx1
    X_0 += dx0

print(tested)