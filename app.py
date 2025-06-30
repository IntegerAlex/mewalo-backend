from flask import Flask, jsonify
from flask_cors import CORS
 

from app.routes.user_routes import user_bp
# Initialize Flask application

def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)

    # Initialize CORS
    CORS(app)

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/user')

    # Register index route
    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the Mewalo Backend API!"})

    return app

# Create the Flask application instance
app = create_app()  

# Run the application if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)