from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Initialize data storage for the graph
graph_data = {
    'x': list(range(10)),  # Initial x values
    'y': [random.randint(0, 100) for _ in range(10)]  # Initial y values
}

# Endpoint to get data for graphing
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(graph_data)

# Endpoint to add new data points
@app.route('/api/add_data', methods=['POST'])
def add_data():
    data = request.get_json()
    x_val = data.get('x')
    y_val = data.get('y')
    
    # Add the new points to the dataset
    if x_val is not None and y_val is not None:
        graph_data['x'].append(x_val)
        graph_data['y'].append(y_val)
        return jsonify({"message": "Data added successfully!"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
