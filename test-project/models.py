from datetime import datetime
import hashlib

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.created_at = datetime.now()
    
    def check_password(self, password):
        return self.password == password
    
    def update_password(self, new_password):
        self.password = new_password

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.inventory = 0
    
    def set_price(self, price):
        self.price = price
    
    def add_inventory(self, quantity):
        self.inventory = self.inventory + quantity

class Order:
    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.total = 0
    
    def calculate_total(self, price):
        total = 0
        for i in range(self.quantity):
            total = total + price
        self.total = total
        return total
