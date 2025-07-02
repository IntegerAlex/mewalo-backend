from app.config import db

class CartDatabase:
    def __init__(self):
        self.cart_collection = db.cart

    def add_to_cart(self, user_id: str, product_id: str) -> bool:
        try:
            # Find the user's cart
            cart = self.cart_collection.find_one({"user_id": user_id})

            if cart:
                # If cart exists, add product_id to the products array
                if product_id not in cart.get("products", []):
                    self.cart_collection.update_one(
                        {"user_id": user_id},
                        {"$addToSet": {"products": product_id}}
                    )
                return True
            else:
                # If no cart exists, create a new one with the product_id
                self.cart_collection.insert_one({"user_id": user_id, "products": [product_id]})
                return True
        except Exception as e:
            print(f"Error adding to cart: {e}")
            return False

    def get_cart(self, user_id: str) -> dict | None:
        try:
            cart = self.cart_collection.find_one({"user_id": user_id})
            if cart and '_id' in cart:
                cart['_id'] = str(cart['_id'])
            return cart
        except Exception as e:
            print(f"Error getting cart: {e}")
            return None

    def remove_from_cart(self, user_id: str, product_id: str) -> bool:
        try:
            self.cart_collection.update_one(
                {"user_id": user_id},
                {"$pull": {"products": product_id}}
            )
            return True
        except Exception as e:
            print(f"Error removing from cart: {e}")
            return False

    def clear_cart(self, user_id):
        self.cart_collection.delete_many({"user_id": user_id})