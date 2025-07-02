from app.config import db

class WishlistDatabase:
    def __init__(self):
        self.wishlist_collection = db.wishlist

    def add_to_wishlist(self, user_id, product_id):
        self.wishlist_collection.insert_one({"user_id": user_id, "product_id": product_id})

    def get_wishlist(self, user_id):
        return self.wishlist_collection.find_one({"user_id": user_id})