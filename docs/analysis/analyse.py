import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
file_path = 'docs/analysis/test_data_logs/autonomous-demo/imu1.csv'
df = pd.read_csv(file_path)

# Plot ros y vs ros x, x = ros y, y = ros x
plt.figure(figsize=(10, 6))
plt.plot(df['y'], df['x'], marker='o', linestyle='-', color='orange',label='ros-x vs ros-y')
plt.title('Plot')
plt.xlabel('ros y')
plt.ylabel('ros x')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='datalim')
# Set axis limits to cover the full range of data
plt.xlim(df['y'].min(), df['y'].max())
plt.ylim(df['x'].min(), df['x'].max())
print(df['x'].min(), df['x'].max())
print(df['y'].min(), df['y'].max())

# Show plot
plt.show()
