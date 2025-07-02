from flask import Blueprint, jsonify, request
from app.services.cart_service import CartService

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/', methods=['GET'])
def get_cart():
    """
    Endpoint to get a user's cart.
    """
    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400
    cart_service = CartService().get_cart(user_data["user_id"])
    return jsonify({"cart": cart_service}), 200

@cart_bp.route('/', methods=['POST'])
def add_to_cart():
    """
    Endpoint to add a product to a user's cart.
    Expects JSON data with product_id.
    """
    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400
    cart_service = CartService().add_to_cart(user_data["product_id"])
    return jsonify({"cart": cart_service}), 200

@cart_bp.route('/', methods=['DELETE'])
def remove_from_cart():
    """
    Endpoint to remove a product from a user's cart.
    Expects JSON data with product_id.
    """
    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400
    cart_service = CartService().remove_from_cart(user_data["product_id"])
    return jsonify({"cart": cart_service}), 200

@cart_bp.route('/', methods=['DELETE'])
def clear_cart():
    """
    Endpoint to clear a user's cart.
    """
    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400
    cart_service = CartService().clear_cart(user_data["user_id"])
    return jsonify({"cart": cart_service}), 200