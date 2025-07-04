from flask import Blueprint, request, jsonify
from app.database.product_database import ProductDatabase

product_route = Blueprint('product_route', __name__)

@product_route.route('/', methods=['GET'])
def get_products():
    products = ProductDatabase().get_all_products()
    for product in products:
        if '_id' in product:
            product['_id'] = str(product['_id'])
    return jsonify({'products': products}), 200

@product_route.route('/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = ProductDatabase().get_product_by_id(product_id)
    if product and '_id' in product:
        product['_id'] = str(product['_id'])
    return jsonify({'product': product}), 200

@product_route.route('/', methods=['POST'])
def add_product():
    product_data = request.json
    if not product_data:
        return jsonify({"error": "No data provided"}), 400
    
    # --- Server-side validation ---
    required_fields = [
        'product_id', 'product_name', 'product_price', 'category', 
        'subcategory', 'product_barcode', 'product_quantity', 'product_unit', 'in_stock',
        'product_image'
    ]
    
    missing_fields = [field for field in required_fields if field not in product_data]
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

    # Type validation for numeric fields
    try:
        float(product_data['product_price'])
        int(product_data['product_quantity'])
        # Validate in_stock as a boolean
        if not isinstance(product_data['in_stock'], bool):
            raise TypeError("in_stock must be a boolean.")
    except (ValueError, TypeError) as e:
        return jsonify({"error": f"Invalid data type: {e}"}), 400
    # --- End validation ---

    try:
        success = ProductDatabase().add_product(product_data)
        if success:
            return jsonify({"message": "Product added successfully!"}), 201
        else:
            return jsonify({"error": "Failed to add product"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
