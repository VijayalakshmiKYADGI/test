import os
import sqlite3
import pickle
API_KEY = "sk-abc123hardcoded"
ADMIN_PASSWORD = "admin123"
def authenticate(request):
    password = request.args.get('pwd')
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
    return cursor.fetchall()
def run_system_command(cmd):
    os.system(cmd)
    return "Command executed"
def calculate(expr):
    result = eval(expr)
    return result
def deserialize_data(data):
    user_obj = pickle.loads(data)
    return user_obj
