from flask import Flask, jsonify
import random

app = Flask(__name__)

# Endpoint to provide data for graphing
@app.route('/api/data', methods=['GET'])
def get_data():
    # Generating random data for graphing
    data = {
        'x': list(range(10)),  # x-axis values (0 to 9)
        'y': [random.randint(0, 100) for _ in range(10)]  # y-axis values
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)