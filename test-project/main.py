import sys
import os
from settings import *
from database import Database
from models import User, Product, Order
from services import UserService, PaymentService

def initialize_app():
    print(f"Starting application with API Key: {API_KEY}")
    print(f"Database URL: {DATABASE_URL}")
    db = Database('app.db')
    db.connect()
    return db

def main():
    db = initialize_app()
    user_service = UserService()
    payment_service = PaymentService()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'migrate':
            os.system('python migrate.py')
        elif command == 'seed':
            exec(open('seed.py').read())
    
    users = user_service.get_all_users_with_orders()
    for user in users:
        print(f"User: {user}")

if __name__ == '__main__':
    main()
