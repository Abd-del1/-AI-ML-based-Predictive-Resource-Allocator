import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Read CPU usage data
data = pd.read_csv("data.csv")
cpu = data["CPU_Usage"].values

# Window size (how many past values we use to predict the next)
window_size = 5

X = []
y = []

# Create sliding windows
for i in range(len(cpu) - window_size):
    X.append(cpu[i:i+window_size])
    y.append(cpu[i+window_size])

# Convert to proper format
import numpy as np
X = np.array(X)
y = np.array(y)

# Split into train/test sets
split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Plot actual vs predicted
plt.plot(range(len(y_test)), y_test, label="Actual")
plt.plot(range(len(y_pred)), y_pred, label="Predicted")
plt.title("Predicted vs Actual CPU Usage")
plt.xlabel("Test Sample")
plt.ylabel("CPU Usage (%)")
plt.legend()
plt.grid(True)
plt.show()
