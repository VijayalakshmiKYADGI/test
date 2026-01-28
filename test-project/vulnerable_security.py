import os
import sqlite3
API_KEY = "sk-abc123hardcoded"
def login(request):
    password = request.args.get('pwd')
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
    return cursor.fetchall()
