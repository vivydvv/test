from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to call this backend

@app.route('/sayhello', methods=['POST'])
def say_hello():
    data = request.json
    name = data.get('name', 'Stranger')
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run()
