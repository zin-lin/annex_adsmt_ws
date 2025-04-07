import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
file_path = 'docs/analysis/test_data_logs/kinematics/odo_3_1.csv'
df = pd.read_csv(file_path)

# Plot ros y vs ros x, x = ros y, y = ros x
plt.figure(figsize=(10, 6))
plt.plot(df['y'], df['x'], marker='.', linestyle='-', color='orange',label='ros-x vs ros-y')
plt.title('Plot')
plt.xlabel('ros y')
plt.ylabel('ros x')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Add horizontal line at ros x location of need
plt.axhline(y=-0.3, color='red', linestyle='--', linewidth=1.5, label='x = -0.5')
plt.axvline(x=0.1, color='red', linestyle='--', linewidth=1.5, label='x = 0.1')

# Set axis limits to cover the full range of data
plt.xlim(df['y'].min(), df['y'].max())
plt.ylim(df['x'].max(), df['x'].min())
print(df['x'].min(), df['x'].max())
print(df['y'].min(), df['y'].max())

# Show plot
plt.show()
