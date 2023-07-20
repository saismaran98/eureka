# eureka_client.py
import subprocess
import requests
from flask import Flask, jsonify

app = Flask(__name__)

def run_test_script():
    output = subprocess.check_output(['sh', 'test.sh'], universal_newlines=True)
    return output.strip()

@app.route('/')
def hello():
    return 'Hello, this is the Eureka client!'

@app.route('/run_test_script', methods=['GET'])
def run_and_send_output():
    output = run_test_script()
    server_url = "http://localhost:5003/receive_output"  # Replace with your server URL
    data = {'output': output}
    response = requests.post(server_url, json=data)
    return jsonify({'message': 'Output sent to server successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
