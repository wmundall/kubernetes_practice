import tensorflow as tf

print("--- 1. Tensors & Constants ---")
# Tensors are multi-dimensional arrays
x = tf.constant([[2.0, 4.0], [6.0, 8.0]])
print("Tensor x:\n", x)
print("Shape:", x.shape, "| Datatype:", x.dtype)

# Basic math operations match NumPy closely
y = x + 10
print("\nTensor y (x + 10):\n", y)
print("Matrix Multiplication (x @ y):\n", x @ y)

print("\n--- 2. Automatic Differentiation (GradientTape) ---")
# This is how neural networks learn: tracking changes to compute derivatives
w = tf.Variable(3.0)
with tf.GradientTape() as tape:
    loss = w**2 + 5 * w

# Calculate the gradient of loss with respect to w
grad = tape.gradient(loss, w)
print(f"Gradient of loss (w^2 + 5w) at w=3.0 is: {grad.numpy()}")