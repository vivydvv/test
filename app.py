from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/sayhello', methods=['POST', 'OPTIONS'])
def say_hello():
    if request.method == 'OPTIONS':
        return '', 200  # respond OK to preflight
    data = request.json
    name = data.get('name', 'Stranger')
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run()
