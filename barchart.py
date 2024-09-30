import matplotlib.pyplot as plt
def bc01():

    # Data
    categories = ['A', 'B', 'C', 'D']
    values = [4, 7, 1, 8]

    # Create bar plot
    plt.figure(figsize=(8, 5))  # Adjust the figure size
    plt.bar(categories, values, color='purple', width=0.5, edgecolor='black', linewidth=1.5)
    plt.title("Bar Chart", fontsize=16, fontweight='bold')  # Modify font size and weight
    plt.xlabel("Categories", fontsize=14)
    plt.ylabel("Values", fontsize=14)
    plt.xticks(fontsize=12, color='orange')
    plt.yticks(fontsize=12, color='purple')
    plt.grid(True, axis='y', color='gray', linestyle='--', linewidth=0.5)
    plt.show()
