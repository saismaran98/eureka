# eureka_server.py
from flask import Flask, jsonify, request

app = Flask(__name__)
server_data = {}  
@app.route('/receive_output', methods=['POST'])
def receive_output():
    data = request.get_json()
    server_hostname = data.get('server_hostname')
    output = data.get('output')
    server_data[server_hostname] = output  # Store server data in the dictionary
    print(f'Received output from server {server_hostname}:\n{output}')
    return jsonify({'message': 'Output received successfully'}), 200

@app.route('/checkAPI', methods=['GET'])
def checkAPI():
    return jsonify({'message': 'Server 1'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

