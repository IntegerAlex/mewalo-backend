from app.config import db

class CartDatabase:
    def __init__(self):
        self.cart_collection = db.cart

    def add_to_cart(self, user_id, product_id):
        self.cart_collection.insert_one({"user_id": user_id, "product_id": product_id})

    def get_cart(self, user_id):
        return self.cart_collection.find_one({"user_id": user_id})
    
    def remove_from_cart(self, user_id, product_id):
        self.cart_collection.delete_one({"user_id": user_id, "product_id": product_id})
    
    def clear_cart(self, user_id):
        self.cart_collection.delete_many({"user_id": user_id})