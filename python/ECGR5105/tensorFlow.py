import tensorflow as tf
import numpy as np
import time

# Load MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_test = x_test / 255.0
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# Define a simple CNN model for MNIST classification
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model briefly (for demonstration; in practice, train longer for better accuracy)
model.fit(x_train.reshape(-1, 28, 28, 1) / 255.0, y_train, epochs=1, batch_size=32, verbose=1)

# Convert to TensorFlow Lite model (optimized for edge devices like iMX8M Plus)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model
with open('mnist_model.tflite', 'wb') as f:
    f.write(tflite_model)

# Load the TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_path='mnist_model.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Run inference on the first 10 test images and measure latency
latencies = []
for i in range(10):
    input_data = x_test[i:i+1].astype(np.float32)
    start_time = time.time()
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    end_time = time.time()
    latency = end_time - start_time
    latencies.append(latency)
    predicted_label = np.argmax(output_data)
    actual_label = y_test[i]
    print(f"Image {i}: Predicted {predicted_label}, Actual {actual_label}, Latency {latency:.4f}s")

# Calculate and print average latency
average_latency = np.mean(latencies)
print(f"\nAverage inference latency: {average_latency:.4f} seconds per image")