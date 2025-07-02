from flask import Blueprint, jsonify, request
from app.services.wishlist_service import WishlistService

wishlist_bp = Blueprint('wishlist_bp', __name__)

@wishlist_bp.route('/', methods=['GET'])
def get_wishlist():
    """
    Endpoint to get a user's wishlist.
    """
    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400
    wishlist_service = WishlistService().get_wishlist(user_data["user_id"])
    return jsonify({"wishlist": wishlist_service}), 200

@wishlist_bp.route('/', methods=['POST'])
def add_to_wishlist():
    """
    Endpoint to add a product to a user's wishlist.
    """ 
    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400
    wishlist_service = WishlistService().add_to_wishlist(user_data["user_id"], user_data["product_id"])
    return jsonify({"wishlist": wishlist_service}), 200

@wishlist_bp.route('/', methods=['DELETE'])
def remove_from_wishlist():
    """
    Endpoint to remove a product from a user's wishlist.
    """
    user_data = request.json
    if not user_data:
        return jsonify({"error": "No data provided"}), 400
    wishlist_service = WishlistService().remove_from_wishlist(user_data["user_id"], user_data["product_id"])
    return jsonify({"wishlist": wishlist_service}), 200

