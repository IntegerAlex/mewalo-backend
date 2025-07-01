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
