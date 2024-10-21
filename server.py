# server.py
from flask import Flask, request, jsonify
import numpy as np
from charting import plot_graph

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
    return jsonify({"message": "Graph plotted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)