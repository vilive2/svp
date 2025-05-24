import tensorflow as tf
from tensorflow import keras
from keras import layers
import numpy as np
import tf2onnx
import onnx


# Define the model
model = keras.Sequential([
    layers.Dense(2, activation='relu', input_shape=(1,)),
    layers.Dense(1)
])

# Build the model (initialize weights)
# model.build(input_shape=(None, 1))

# Manually set weights
hidden_layer_weights = np.array([[1, -1]])
hidden_layer_bias = np.array([0, 0])

output_layer_weights = np.array([[1], [1]])
output_layer_bias = np.array([0])

# Assign weights
model.layers[0].set_weights([hidden_layer_weights, hidden_layer_bias])
model.layers[1].set_weights([output_layer_weights, output_layer_bias])

# Convert model to ONNX
# spec = (tf.TensorSpec((None, 1), tf.float32, name="input"),)
# onnx_model, _ = tf2onnx.convert.from_keras(model, input_signature=spec)

# # Save ONNX model to file
# onnx_filename = "lec2nn.onnx"
# with open(onnx_filename, "wb") as f:
#     f.write(onnx_model.SerializeToString())

# print(f"Model saved as {onnx_filename}")

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
