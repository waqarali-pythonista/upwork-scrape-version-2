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
    # ChromeDriver configuration
    CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH', '/path/to/chromedriver')  # default path if not set in .env
    GOOGLE_CHROME_BIN = os.getenv('GOOGLE_CHROME_BIN', '/path/to/google-chrome')  # default path if not set in .env
3. 
