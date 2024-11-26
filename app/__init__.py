from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

# Initialize extensions
db = SQLAlchemy()

def create_app():
    """
    Factory function to create and configure the Flask application.

    Returns:
        Flask: Configured Flask app instance.
    """
    app = Flask(__name__)

    # Load configuration from Config class
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    CORS(app)

    # # Register blueprints
    # from app.routes.job_routes import job_bp
    # app.register_blueprint(job_bp, url_prefix='/api')

    # Ensure database tables are created
    with app.app_context():
        db.create_all()

    return app
