import pandas as pd
import matplotlib.pyplot as plt

# Read CSV into DataFrame
file_path = 'docs/analysis/test_data_logs/durability /drive.csv'
df = pd.read_csv(file_path)
# Filter data to only include time values (t) <= 30
dff = df[df['time'] >= 15]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(dff['time'], dff['dis'], label='leg 1 thigh', linestyle='-')
plt.plot(dff['time'], dff['dis'], label='leg 2 thigh', linestyle='-')
plt.plot(dff['time'], dff['dis'], label='leg 3 thigh', linestyle='-')
plt.plot(dff['time'], dff['dis'], label='leg 4 thigh', linestyle='-')
# Labels and title
plt.title('Distance value (mm) over time (s)')
plt.xlabel('Time (s)')
plt.ylabel('Distance value (mm)')
plt.legend()
plt.grid(True)



# Show plot
plt.show()
