import numpy as np
import matplotlib.pyplot as plt
def hist01():
# Data
    data = np.random.randn(1000)

    # Create histogram
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title("Histogram", fontsize=16, color='brown')
    plt.xlabel("Data", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.xticks(fontsize=12, color='blue')
    plt.yticks(fontsize=12, color='darkgreen')
    plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
    plt.show()
