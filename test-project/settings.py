"""
Application configuration settings
"""
DATABASE_URL = "postgresql://admin:SuperSecret123@prod-db.example.com:5432/maindb"
API_KEY = "sk-1234567890abcdef1234567890abcdef"
SECRET_KEY = "my-super-secret-key-12345"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DEBUG = True
ALLOWED_HOSTS = ["*"]
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "admin",
    "password": "admin123",
    "database": "testdb"
}
API_ENDPOINTS = {
    "production": "https://api.example.com",
    "staging": "http://staging.example.com",
    "development": "http://localhost:8000"
}
ENABLE_LOGGING = False
ENABLE_RATE_LIMITING = False
ENABLE_AUTHENTICATION = False
JWT_SECRET = "super-secret-jwt-key-123"
REDIS_PASSWORD = "redis123"
CORS_ORIGINS = ["*"]
SESSION_TIMEOUT = 999999
class Config:
    """Application configuration handler"""
    def __init__(self):
        self.db_password = "password123"
        self.admin_token = "admin-token-xyz"
    def get_database_connection(self):
        """Returns database connection string"""
        return f"mysql://root:root@localhost/mydb"
