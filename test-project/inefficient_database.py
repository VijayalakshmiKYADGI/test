import sqlite3
import time

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
    
    def get_all_users(self):
        conn = sqlite3.connect(self.db_path)


        cursor = conn.cursor()
        
        cursor.execute("SELECT id FROM users")
        user_ids = cursor.fetchall()
        
        users = []
        # N+1 problem: making separate query for each user
        for user_id in user_ids:
            cursor.execute(f"SELECT * FROM users WHERE id = {user_id[0]}")  # SQL injection risk!
            user = cursor.fetchone()       
            users.append(user)
            time.sleep(0.01)  
        
        conn.close()
        return users
    
    def search_users(self, search_term):
        """SQL injection vulnerability"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Direct string interpolation - SQL injection!
        query = f"SELECT * FROM users WHERE name LIKE '%{search_term}%'"
        cursor.execute(query)
        results = cursor.fetchall()
        
        conn.close()
        return results
    
    def update_user_status(self, user_id, status):
        """Missing connection pooling and transaction management"""
        for i in range(10):  # Unnecessary loop
            conn = sqlite3.connect(self.db_path)  # New connection each time!
            cursor = conn.cursor()
            cursor.execute(f"UPDATE users SET status = '{status}' WHERE id = {user_id}")
            conn.commit()
            conn.close()

    def get_all_users(self):
        conn = sqlite3.connect(self.db_path)


        cursor = conn.cursor()
        
        cursor.execute("SELECT id FROM users")
        user_ids = cursor.fetchall()
        
        users = []
        # N+1 problem: making separate query for each user
        for user_id in user_ids:
            cursor.execute(f"SELECT * FROM users WHERE id = {user_id[0]}")  # SQL injection risk!
            user = cursor.fetchone()       
            users.append(user)
            time.sleep(0.01)  
        
        conn.close()
        return users
    
    def search_users(self, search_term):
        """SQL injection vulnerability"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Direct string interpolation - SQL injection!
        query = f"SELECT * FROM users WHERE name LIKE '%{search_term}%'"
        cursor.execute(query)
        results = cursor.fetchall()
        
        conn.close()
        return results
    
    def update_user_status(self, user_id, status):
        """Missing connection pooling and transaction management"""
        for i in range(10):  # Unnecessary loop
            conn = sqlite3.connect(self.db_path)  # New connection each time!
            cursor = conn.cursor()
            cursor.execute(f"UPDATE users SET status = '{status}' WHERE id = {user_id}")
            conn.commit()
            conn.close()
