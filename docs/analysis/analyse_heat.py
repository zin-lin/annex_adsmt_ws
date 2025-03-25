import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binned_statistic_2d
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Load CSV file
file_path = 'docs/analysis/test_data_logs/bridge/imu-bridge.csv'
df = pd.read_csv(file_path)

# Define bin size
bins = 50

# Compute 2D binned statistics
stat, x_edges, y_edges, _ = binned_statistic_2d(
    df['y'], df['x'], None, statistic='count', bins=bins
)

# Create a custom colormap from white → orange → black
colors = [(1, 1, 1), (1, 0.7, 0), (0, 0, 0)]  # White → Orange → Black
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors, N=256)

# Plot the heatmap
plt.figure(figsize=(10, 6))
plt.imshow(
    stat.T,
    origin='lower',
    extent=[x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]],
    cmap=custom_cmap,
    aspect='auto',
    norm=Normalize(vmin=0, vmax=stat.max())  # Keep 0 values light
)

# Add color bar
plt.colorbar(label='Count')

# Set plot labels and title
plt.title('Heatmap of ros-x vs ros-y acceleration data (IMU)')
plt.xlabel('ros y ')
plt.ylabel('ros x ')
plt.show()

# Show plot
plt.show()
