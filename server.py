from flask import Flask, request, jsonify, send_file
import numpy as np
from grapher import plot_graph
import os

app = Flask(__name__)

@app.route('/plot', methods=['POST'])
def plot():
    data = request.json
    x_values = np.array(data['x_values'])
    y_values = np.array(data['y_values'])
    title = data.get('title', 'Graph')
    xlabel = data.get('xlabel', 'X-axis')
    ylabel = data.get('ylabel', 'Y-axis')
    
    plot_graph(x_values, y_values, title, xlabel, ylabel)
    
    # Return the graph image
    return send_file('graph.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)