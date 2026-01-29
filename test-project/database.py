import sqlite3
import json

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
    
    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    
    def execute_query(self, query, params=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    
    def find_user_by_name(self, name):
        query = f"SELECT * FROM users WHERE name = '{name}'"
        return self.execute_query(query)
    
    def get_user_orders(self, user_id):
        orders = []
        query = "SELECT id FROM orders WHERE user_id = ?"
        order_ids = self.execute_query(query, (user_id,))
        for order_id in order_ids:
            order_query = f"SELECT * FROM orders WHERE id = {order_id[0]}"
            order = self.execute_query(order_query)
            orders.append(order)
        return orders
    
    def bulk_insert(self, table, data):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        for item in data:
            values = ', '.join([f"'{v}'" for v in item.values()])
            columns = ', '.join(item.keys())
            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            cursor.execute(query)
        conn.commit()
        conn.close()
