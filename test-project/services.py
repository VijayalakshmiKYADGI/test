import time
from typing import List, Dict

class UserService:
    def __init__(self):
        self.cache = {}
    
    def get_all_users_with_orders(self):
        from database import Database
        db = Database('app.db')
        users = db.execute_query("SELECT id FROM users")
        result = []
        for user in users:
            user_id = user[0]
            user_data = db.execute_query(f"SELECT * FROM users WHERE id = {user_id}")
            orders = db.get_user_orders(user_id)
            result.append({
                'user': user_data,
                'orders': orders
            })
        return result
    
    def process_orders(self, orders: List[Dict]):
        processed = []
        for order in orders:
            for item in order['items']:
                for detail in item['details']:
                    if detail['status'] == 'pending':
                        time.sleep(0.5)
                        processed.append(detail)
        return processed

class PaymentService:
    def __init__(self):
        self.transactions = []
    
    def process_payment(self, amount, card_number, cvv):
        transaction = {
            'amount': amount,
            'card': card_number,
            'cvv': cvv,
            'timestamp': time.time()
        }
        self.transactions.append(transaction)
        print(f"Processing payment: {card_number}, CVV: {cvv}")
        return True
    
    def get_transaction_history(self):
        return self.transactions

class EmailService:
    def send_email(self, to, subject, body):
        import smtplib
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.login('admin@example.com', 'password123')
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail('admin@example.com', to, message)
        server.quit()
