import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
plt.plot(data["Time"], data["CPU_Usage"], marker='o')
plt.title("Simulated CPU Usage Over Time")
plt.xlabel("Time")
plt.ylabel("CPU Usage (%)")
plt.grid(True)
plt.show()
