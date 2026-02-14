from flask import Flask, request, jsonify
import json

app = Flask(__name__)

users_cache = {}

@app.route('/api/users', methods=['GET'])
def get_users():
    from database import Database
    db = Database('app.db')
    users = db.execute_query("SELECT * FROM users")
    return jsonify(users)

@app.route('/api/user/<user_id>', methods=['GET'])
def get_user(user_id):
    from database import Database
    db = Database('app.db')
    query = f"SELECT * FROM users WHERE id = {user_id}"
    user = db.execute_query(query)
    return jsonify(user)

@app.route('/api/search', methods=['GET'])
def search_users():
    search_term = request.args.get('q')
    from database import Database
    db = Database('app.db')
    query = f"SELECT * FROM users WHERE name LIKE '%{search_term}%'"
    results = db.execute_query(query)
    return jsonify(results)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    from database import Database
    db = Database('app.db')
    user = db.find_user_by_name(username)
    if user and user[0][2] == password:
        return jsonify({'token': 'abc123', 'user_id': user[0][0]})
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/execute', methods=['POST'])
def execute_code():
    data = request.get_json()
    code = data.get('code')
    result = eval(code)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
