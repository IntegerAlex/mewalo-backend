from flask import Blueprint, request, jsonify
from services.user_service import UserService
user_bp = Blueprint('user', __name__)


@user_bp.route('/create', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user.
    Expects JSON data with first_name, last_name, email, and phone.
    """
    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400

    user_service = UserService()
    success = user_service.create_user(user_data)

    if success:
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"error": "Failed to create user"}), 500
