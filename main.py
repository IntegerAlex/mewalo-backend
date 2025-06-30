from flask import Flask, jsonify, request
from flask_cors import CORS
from app.config import db  # Import the db object
from app.routes.user_routes import user_bp
from app.services.misc import MiscService

def create_app():
    app = Flask(__name__)
    CORS(app)

    # MongoDB connection test
    try:
        db.command('ping')
        print("MongoDB connected successfully!")
    except Exception as e:
        print(f"MongoDB connection failed: {e}")

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/user')

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the Mewalo Backend API!"})

    @app.route('/contact', methods=['POST'])
    def contact():
        inquiry_data = request.json
        if not inquiry_data:
            return jsonify({"error": "No data provided"}), 400

        success = MiscService().contact_us(inquiry_data)

        if success:
            return jsonify({"message": "Enquiry submitted successfully!"}), 200
        else:
            return jsonify({"error": "Failed to submit enquiry"}), 500

    @app.route('/subscribe', methods=['POST'])
    def subscribe():
        subscription_data = request.json
        if not subscription_data:
            return jsonify({"error": "No data provided"}), 400

        success = MiscService().subscribe(subscription_data)

        if success:
            return jsonify({"message": "Subscription added successfully!"}), 200
        else:
            return jsonify({"error": "Failed to add subscription"}), 500

    return app

# Create the app here so gunicorn can find it
app = create_app()

# Only run the server in development mode
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
