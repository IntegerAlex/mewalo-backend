from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.services.auth_service import AuthService, temp_user
from app.database.user_database import UserDatabase
from bson.objectid import ObjectId
user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to create a new user.
    Expects JSON data with first_name, last_name, email, and phone.
    """

    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400
    
    success = AuthService().register_user(user_data)
    print(success)
    if success:
        return jsonify({"message": "OTP sent successfully"}), 200
    else:
        return jsonify({"error": "Failed to send OTP"}), 500

@user_bp.route('/register/verify', methods=['POST'])
def verify_user():
    """
    Endpoint to verify a user.
    Expects JSON data with phone and otp.
    """
    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400
    verify_otp = AuthService().verify_otp(user_data["phone"], user_data["otp"])
    if verify_otp:
        user_to_create = temp_user[user_data["phone"]]
        UserService().create_user(user_to_create)
        del temp_user[user_data["phone"]]

        # Convert ObjectId to string for JSON serialization
        if '_id' in user_to_create and isinstance(user_to_create['_id'], ObjectId):
            user_to_create['_id'] = str(user_to_create['_id'])

        jwt = AuthService().generate_jwt(user_data["phone"])
        return jsonify({"message": "User verified successfully", "jwt": jwt, "user": user_to_create}), 200
    else:
        return jsonify({"error": "Invalid OTP"}), 400


@user_bp.route('/login', methods=['POST'])
def login_user():
    """
    Endpoint to login a user.
    Expects JSON data with phone and password.
    """
    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400
    user = UserService().get_user_by_phone(user_data["phone"])
    if not user:
        return jsonify({"error": "User not found"}), 404
    AuthService().generate_otp(user_data["phone"])
    return jsonify({"message": "OTP sent successfully"}), 200

@user_bp.route('/login/verify', methods=['POST'])
def verify_login():
    """
    Endpoint to verify a user login.
    Expects JSON data with phone and otp.
    """
    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400
    
    verify_otp = AuthService().verify_otp(user_data["phone"], user_data["otp"])
    if verify_otp:
        # Retrieve the full user object from the database
        user = UserService().get_user_by_phone(user_data["phone"])
        
        if not user:
            return jsonify({"error": "User not found after verification"}), 404

        # Convert ObjectId to string for JSON serialization
        if '_id' in user and isinstance(user['_id'], ObjectId):
            user['_id'] = str(user['_id'])

        jwt = AuthService().generate_jwt(user["phone"]) # Use user["phone"] from retrieved user
        return jsonify({"message": "User logged in successfully", "jwt": jwt, "user": user}), 200 # Return full user object
    else:
        return jsonify({"error": "Invalid OTP"}), 400

