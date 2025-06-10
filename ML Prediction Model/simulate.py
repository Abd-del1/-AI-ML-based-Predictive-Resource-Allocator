import random
import csv

# Total time steps (e.g., 200 seconds or minutes)
TIME_STEPS = 200
data = []

# Generate usage pattern
for t in range(TIME_STEPS):
    # Simulate traffic waves
    if 0 <= t < 50:
        cpu = random.randint(30, 55)
    elif 50 <= t < 100:
        cpu = random.randint(55, 80)
    elif 100 <= t < 150:
        cpu = random.randint(40, 65)
    else:
        cpu = random.randint(60, 90)
    
    data.append((t, cpu))

# Save to CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Time", "CPU_Usage"])
    writer.writerows(data)

print("✅ Simulated data saved to data.csv")

