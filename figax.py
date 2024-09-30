import matplotlib.pyplot as plt
def ax01():
    # Create a figure and an axes object
    fig, ax = plt.subplots(figsize=(10, 6))  # Set figure size

    # Plot data
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    ax.plot(x, y, color='purple', marker='o', linestyle='--', markersize=10, linewidth=2, label='Line 1')

    # Customizations
    ax.set_title("Custom Line Plot", fontsize=18, fontweight='bold', color='darkblue')  # Title font and color
    ax.set_xlabel("X Axis", fontsize=14, color='green')  # X label customization
    ax.set_ylabel("Y Axis", fontsize=14, color='red')  # Y label customization
    ax.legend(loc='upper left', fontsize=12, frameon=True, shadow=True, facecolor='lightyellow')  # Legend customization
    ax.grid(True, linestyle=':', color='gray', linewidth=0.7)  # Grid customization
    ax.set_xticks([1, 2, 3, 4, 5])  # Set custom x-ticks
    ax.set_yticks([2, 4, 6, 8, 10])  # Set custom y-ticks
    ax.set_xlim(0, 6)  # Set x-axis limit
    ax.set_ylim(0, 12)  # Set y-axis limit

    # Adding annotations
    ax.annotate("Start Point", xy=(1, 2), xytext=(1.5, 4),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

    # Show plot
    plt.show()

    # Change line color and style
    #ax.plot(x, y, color='#FF5733', linestyle=':', linewidth=2)  # Use hex color codes and change line style

    # Change font properties
    #ax.set_title("Custom Title", fontdict={'fontsize': 16, 'fontweight': 'bold', 'color': 'darkred'})
    #ax.set_xlabel("X Axis", fontdict={'fontsize': 14, 'fontstyle': 'italic'})
    #ax.set_ylabel("Y Axis", fontdict={'fontsize': 14, 'fontstyle': 'italic'})

    # Change axis ticks and labels
    #ax.tick_params(axis='x', labelsize=12, labelcolor='blue', rotation=45)  # Modify x-tick labels
    #ax.tick_params(axis='y', labelsize=12, labelcolor='red')  # Modify y-tick labels

    # Change grid style
    #ax.grid(True, linestyle='--', linewidth=0.5, color='gray')

    # Add annotation
    #ax.annotate('Peak', xy=(2, 4), xytext=(3, 5), arrowprops=dict(facecolor='black', shrink=0.05))
