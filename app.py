from flask import Flask, jsonify, request
from flask_cors import CORS
from app.config import db # Import the db object

from app.routes.user_routes import user_bp
from app.services.misc import MiscService
# Initialize Flask application

def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)

    # Initialize CORS
    CORS(app)

    # MongoDB connection test
    try:
        # The ping command is cheap and does not require auth.
        db.command('ping')
        print("MongoDB connected successfully!")
    except Exception as e:
        print(f"MongoDB connection failed: {e}")

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/user')

    # Register index route
    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the Mewalo Backend API!"})
    
    @app.route('/contact', methods=['POST'])
    def contact():
        inquiry_data = request.json # Assign request.json to a variable for clarity
        if not inquiry_data:
            return jsonify({"error": "No data provided"}), 400
        
        success = MiscService().contact_us(inquiry_data) # Capture the return value
        
        if success:
            return jsonify({"message": "Enquiry submitted successfully!"}), 200
        else:
            # If MiscService().contact_us returned False, indicate failure
            return jsonify({"error": "Failed to submit enquiry"}), 500

    @app.route('/subscribe', methods=['POST'])
    def subscribe():
        subscription_data = request.json # Assign request.json to a variable for clarity
        if not subscription_data:
            return jsonify({"error": "No data provided"}), 400
        
        success = MiscService().subscribe(subscription_data) # Capture the return value
        
        if success:
            return jsonify({"message": "Subscription added successfully!"}), 200
        else:
            return jsonify({"error": "Failed to add subscription"}), 500


    return app

# Create the Flask application instance
app = create_app()  

# Run the application if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)