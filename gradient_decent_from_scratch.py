import numpy as np

# Sample data: input (x) and output (y)
x = np.array([1, 2, 3, 4, 5], dtype=np.float64)
y = np.array([2, 4, 5, 4, 5], dtype=np.float64)


# Initialize parameters
m = 0.0  # initial slope
b = 0.0  # initial intercept
learning_rate = 0.01  # learning rate
epochs = 1000  # number of iterations
n = len(x) # number of data points


# Gradient descent algorithm
for epoch in range(epochs):
    # Predictions based on current slope and intercept
    y_pred = m * x + c

    # Calculate gradients
    dm = (-2 / n) * np.sum(x * (y - y_pred))  # partial derivative w.r.t m
    dc = (-2 / n) * np.sum(y - y_pred)        # partial derivative w.r.t b

    # Update parameters
    m = m - learning_rate * dm
    c = c - learning_rate * db

    # Optionally, print the progress
    if epoch % 100 == 0:
        mse = np.mean((y - y_pred) ** 2)
        print(f"Epoch {epoch}: Slope (m) = {m}, Intercept (b) = {b}, MSE = {mse}")


# Final slope and intercept
print(f"\nFinal Slope (m): {m}")
print(f"Final Intercept (b): {b}")


# Prediction function
def predict(x_val):
    return m * x_val + b


# Test the model with a new value
x_test = 6
y_test_pred = predict(x_test)
print(f"Predicted value for x={x_test}: {y_test_pred}")









