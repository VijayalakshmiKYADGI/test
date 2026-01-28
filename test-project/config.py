"""
Configuration file with hardcoded secrets and poor practices
"""

# Hardcoded credentials - SECURITY ISSUE!
DATABASE_URL = "postgresql://admin:SuperSecret123@prod-db.example.com:5432/maindb"
API_KEY = "sk-1234567890abcdef1234567890abcdef"
SECRET_KEY = "my-super-secret-key-12345"

# AWS Credentials hardcoded - CRITICAL SECURITY ISSUE!
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Configuration settings
DEBUG = True  # Should be False in production!
ALLOWED_HOSTS = ["*"]  # Too permissive!

# Database settings
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "admin",
    "password": "admin123",  # Weak password!
    "database": "testdb"
}

# API endpoints
API_ENDPOINTS = {
    "production": "https://api.example.com",
    "staging": "http://staging.example.com",  # HTTP instead of HTTPS!
    "development": "http://localhost:8000"
}

# Feature flags
ENABLE_LOGGING = False  # Should be True!
ENABLE_RATE_LIMITING = False  # Security risk!
ENABLE_AUTHENTICATION = False  # Major security risk!

class Config:
    """Configuration class with mixed concerns"""
    
    def __init__(self):
        self.db_password = "password123"  # Hardcoded!
        self.admin_token = "admin-token-xyz"  # Hardcoded!
    
    def get_database_connection(self):
        """Returns connection string with credentials"""
        return f"mysql://root:root@localhost/mydb"  # Hardcoded credentials!
