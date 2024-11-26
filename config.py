import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    """
    Configuration class for the Flask application.
    """

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///jobs.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # CORS settings
    CORS_HEADERS = 'Content-Type'

    # Flask settings
    #DEBUG = os.getenv('DEBUG', 'True').lower() in ('true', '1', 't')
    #SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    