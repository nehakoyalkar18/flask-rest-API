from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User added!"}), 201

@app.route('/users/<int:index>', methods=['PUT'])
def update_user(index):
    if 0 <= index < len(users):
        users[index] = request.get_json()
        return jsonify({"message": "User updated!"}), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:index>', methods=['DELETE'])
def delete_user(index):
    if 0 <= index < len(users):
        users.pop(index)
        return jsonify({"message": "User deleted!"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
