# grapher.py
import matplotlib.pyplot as plt
import numpy as np

def plot_graph(x_values, y_values, title="Graph", xlabel="X-axis", ylabel="Y-axis"):
    plt.figure()
    plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig('graph.png')
    plt.close()

if __name__ == "__main__":
    # Example usage
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plot_graph(x, y, title="Sine Wave", xlabel="Time", ylabel="Amplitude")