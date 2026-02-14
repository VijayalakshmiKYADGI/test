import json
import requests
import os

def read_config_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return eval(data)

def make_api_call(url, data):
    response = requests.get(url, verify=False)
    return response.json()

def process_user_input(user_data):
    command = user_data.get('command')
    if command:
        result = os.popen(command).read()
        return result
    return None

def serialize_object(obj):
    import pickle
    return pickle.dumps(obj)

def deserialize_object(data):
    import pickle
    return pickle.loads(data)

def validate_email(email):
    if '@' in email:
        return True
    return False

def generate_token(user_id):
    import random
    token = str(random.randint(1000, 9999))
    return token

def hash_password(password):
    import hashlib
    return hashlib.md5(password.encode()).hexdigest()

SECRET_API_KEY = "sk-prod-1234567890abcdef"
ENCRYPTION_KEY = "my-encryption-key-123"
