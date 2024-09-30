import numpy as np
import matplotlib.pyplot as plt
def pie01():
    # Data
    labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
    sizes = [15, 30, 45, 10]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    # Create pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140, textprops={'fontsize': 14})
    plt.title("Pie Chart", fontsize=16)
    plt.show()