from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    """Simple API endpoint for testing."""
    return jsonify({'message': 'Hello from your Flask API in a container!'})

@app.route('/data', methods=['POST'])
def process_data():
    """Endpoint to receive and process data."""
    if request.method == 'POST':
        data = request.get_json()
        if data:
            # Process data here (replace with your specific logic)
            processed_data = data.get('value', None) * 2  # Example processing
            return jsonify({'processed_data': processed_data})
        else:
            return jsonify({'error': 'No data provided in request body'}), 400
    else:
        return jsonify({'error': 'Unsupported method'}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # Expose for external access
