import numpy as np
import matplotlib.pyplot as plt

# Data for "Before" and "After" under "Low Load," "Medium Load," and "High Load"
before_low = []
after_low = []


before_high = []
after_high = []

# Create subplots for Low, Medium, and High Load
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# Define load levels and data
load_levels = ["Low Load", "High Load"]
before_data = [before_low, before_high]
after_data = [after_low, after_high]

for i, ax in enumerate(axs):
    # Calculate mean and standard deviation for "Before" and "After" in each load level
    mean_before = np.mean(before_data[i])
    std_dev_before = np.std(before_data[i])
    mean_after = np.mean(after_data[i])
    std_dev_after = np.std(after_data[i])

    # Calculate an appropriate range of x values based on the data
    x_min = min(mean_before - 3 * std_dev_before, mean_after - 3 * std_dev_after)
    x_max = max(mean_before + 3 * std_dev_before, mean_after + 3 * std_dev_after)
    x = np.linspace(x_min, x_max, 100)  # Adjust the range based on your data

    # Calculate the y values using the normal distribution formula
    y_before = (1 / (std_dev_before * np.sqrt(2 * np.pi))) * np.exp(-((x - mean_before) ** 2) / (2 * std_dev_before ** 2))
    y_after = (1 / (std_dev_after * np.sqrt(2 * np.pi))) * np.exp(-((x - mean_after) ** 2) / (2 * std_dev_after ** 2))

    # Plot the bell curves for each load level
    ax.plot(x, y_before, label='Before')
    ax.plot(x, y_after, label='After')
    ax.set_xlabel('Number of Packets Transferred')
    ax.set_ylabel('Probability Density')
    ax.legend()
    ax.set_title(f'Bell Curve - {load_levels[i]}')

plt.tight_layout()
plt.show()
