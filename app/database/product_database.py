from app.config import db

class ProductDatabase:
    def __init__(self):
        pass

    def get_all_products(self) -> list:
        """
        Get all products from the database.
        :return: List of products.
        """
        products = list(db.products.find({}))
        for product in products:
            if '_id' in product:
                product['_id'] = str(product['_id'])
        return products
    
    def get_product_by_id(self, product_id: str) -> dict:
        """
        Get a product by its ID.
        :param product_id: The ID of the product to retrieve.
        :return: The product as a dictionary.
        """
        product = db.products.find_one({'product_id': product_id})
        if product:
            if '_id' in product:
                product['_id'] = str(product['_id'])
        return product