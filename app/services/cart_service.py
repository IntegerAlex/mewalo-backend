from app.database.cart_database import CartDatabase

class CartService:
    def __init__(self):
        self.cart_database = CartDatabase()

    def get_cart(self, user_id):
        return self.cart_database.get_cart(user_id)

    def add_to_cart(self, user_id, product_id): 
        return self.cart_database.add_to_cart(user_id, product_id)

    def remove_from_cart(self, user_id, product_id):
        return self.cart_database.remove_from_cart(user_id, product_id)
    
    def clear_cart(self, user_id):
        return self.cart_database.clear_cart(user_id)