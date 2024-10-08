from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-client-ip', methods=['GET'])
def get_client_ip():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return jsonify({"ip": client_ip})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
