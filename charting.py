import matplotlib.pyplot as plt
import numpy as np

def create_line_chart(data, xlabel="X-axis", ylabel="Y-axis", title="Line Chart"):
    """
    Creates a line chart based on the given data.

    Args:
        data (list): A list of data points (x, y) pairs.
        xlabel (str, optional): The label for the x-axis. Defaults to "X-axis".
        ylabel (str, optional): The label for the y-axis. Defaults to "Y-axis".
        title (str, optional): The title of the chart. Defaults to "Line Chart".
    """

    x_values, y_values = zip(*data)
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='blue')  # Customize appearance
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)  # Add grid lines for better readability
    plt.show()

def create_bar_chart(data, xlabel="X-axis", ylabel="Y-axis", title="Bar Chart"):
    """
    Creates a bar chart based on the given data.

    Args:
        data (list): A list of data points (x, y) pairs.
        xlabel (str, optional): The label for the x-axis. Defaults to "X-axis".
        ylabel (str, optional): The label for the y-axis. Defaults to "Y-axis".
        title (str, optional): The title of the chart. Defaults to "Bar Chart".
    """

    x_values, y_values = zip(*data)
    plt.bar(x_values, y_values, color='orange')  # Customize appearance
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(x_values)  # Ensure x-axis labels are displayed
    plt.show()

# Example usage
data = [(1, 2), (2, 4), (3, 6)]
create_line_chart(data)
create_bar_chart(data)