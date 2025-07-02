from app.database.wishlist_database import WishlistDatabase

class WishlistService:
    def __init__(self):
        self.wishlist_database = WishlistDatabase()
        pass

    def add_to_wishlist(self, user_id, product_id):
        self.wishlist_database.add_to_wishlist(user_id, product_id)

    def get_wishlist(self, user_id):
        return self.wishlist_database.get_wishlist(user_id)

    def remove_from_wishlist(self, user_id, product_id):
        self.wishlist_database.remove_from_wishlist(user_id, product_id)