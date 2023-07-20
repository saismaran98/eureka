# eureka_client_5005.py
import socket
import threading
import subprocess
import requests
from flask import Flask, jsonify

app = Flask(__name__)

def run_test_script():
    output = subprocess.check_output(['sh', 'test.sh'], universal_newlines=True)
    return output.strip()

@app.route('/')
def hello():
    return 'Hello, this is the Eureka client on port 5005!'

@app.route('/run_test_script', methods=['GET'])
def run_and_send_output():
    with app.app_context():
        output = run_test_script()
        server_hostname = socket.gethostname()
        server_url = "http://localhost:5003/receive_output"
        data = {'server_hostname': server_hostname, 'output': output}
        response = requests.post(server_url, json=data)
    return jsonify({'message': 'Output sent to server successfully'}), 200

def send_output_periodically():
    threading.Timer(5, send_output_periodically).start()  # Run every 1 minute (60 seconds)
    with app.app_context():
        run_and_send_output()

if __name__ == '__main__':
    send_output_periodically()  # Start sending output every 1 minute
    app.run(host='0.0.0.0', port=5006)
