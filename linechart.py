import matplotlib.pyplot as plt
def lc01():


# Data
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Create line plot
    plt.figure(figsize=(8, 5))  # Adjust the figure size
    plt.plot(x, y, color='blue', linestyle='--', marker='o', markersize=8, linewidth=2, label='Prime Numbers')
    plt.title("Line Chart", fontsize=16)  # Modify font size
    plt.xlabel("X-Axis", fontsize=14)
    plt.ylabel("Y-Axis", fontsize=14)
    plt.legend(fontsize=12)  # Modify legend font size
    plt.grid(True, color='gray', linestyle='--', linewidth=0.5)  # Modify grid lines
    plt.xticks(fontsize=12, color='green')  # Modify x-tick labels
    plt.yticks(fontsize=12, color='red')    # Modify y-tick labels
    plt.show()
