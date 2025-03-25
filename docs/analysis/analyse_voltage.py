import pandas as pd
import matplotlib.pyplot as plt

# Read CSV into DataFrame
file_path = 'docs/analysis/test_data_logs/durability /voltage_vol.csv'
df = pd.read_csv(file_path)
# Filter data to only include time values (t) <= 30
dff = df[df['time'] <= 1060]
# Plotting
plt.figure(figsize=(10, 6))
plt.plot(dff['time'], dff['12'], label='leg 1 thigh', linestyle='-')
plt.plot(dff['time'], dff['22'], label='leg 2 thigh', linestyle='-')
plt.plot(dff['time'], dff['32'], label='leg 3 thigh', linestyle='-')
plt.plot(dff['time'], dff['42'], label='leg 4 thigh', linestyle='-')
# Labels and title
plt.title('ID Values Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Dynamixel Value')
plt.legend()
plt.grid(True)

# knees
plt.figure(figsize=(10, 6))
plt.plot(dff['time'], dff['13'], label='leg 1 knee', linestyle='-')
plt.plot(dff['time'], dff['23'], label='leg 2 knee', linestyle='-')
plt.plot(dff['time'], dff['33'], label='leg 3 knee', linestyle='-')
plt.plot(dff['time'], dff['43'], label='leg 4 knee', linestyle='-')

# Labels and title
plt.title('ID Values Over Time')
plt.xlabel('Time (s)')
plt.ylabel(' Dynamixel Value')
plt.legend()
plt.grid(True)


# Show plot
plt.show()
