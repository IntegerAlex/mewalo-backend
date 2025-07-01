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
    
    def add_product(self, product_data: dict) -> bool:
        """
        Add a new product to the database.
        :param product_data: Dictionary containing product information.
        :return: True if product is added successfully, False otherwise.
        """
        try:
            db.products.insert_one(product_data)
            return True
        except Exception as e:
            print(f"Error adding product: {e}")
            return False