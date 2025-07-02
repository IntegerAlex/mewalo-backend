from flask import Blueprint, jsonify
from app.services.categories_service import CategoriesService

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/', methods=['GET'])
def get_categories_route():
    """
    API endpoint to get aggregated categories and subcategories.
    """
    try:
        categories_data = CategoriesService().get_aggregated_categories()
        return jsonify(categories_data), 200
    except Exception as e:
        print(f"Error in get_categories_route: {e}")
        return jsonify({"error": "Failed to retrieve categories"}), 500 