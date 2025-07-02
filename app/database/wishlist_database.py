from app.config import db

class WishlistDatabase:
    def __init__(self):
        self.wishlist_collection = db.wishlist

    def add_to_wishlist(self, user_id: str, product_id: str) -> bool:
        try:
            # Find the user's wishlist
            wishlist = self.wishlist_collection.find_one({"user_id": user_id})

            if wishlist:
                # If wishlist exists, add product_id to the products array
                if product_id not in wishlist.get("products", []):
                    self.wishlist_collection.update_one(
                        {"user_id": user_id},
                        {"$addToSet": {"products": product_id}}
                    )
                return True
            else:
                # If no wishlist exists, create a new one with the product_id
                self.wishlist_collection.insert_one({"user_id": user_id, "products": [product_id]})
                return True
        except Exception as e:
            print(f"Error adding to wishlist: {e}")
            return False

    def get_wishlist(self, user_id: str) -> dict | None:
        try:
            wishlist = self.wishlist_collection.find_one({"user_id": user_id})
            if wishlist and '_id' in wishlist:
                wishlist['_id'] = str(wishlist['_id'])
            return wishlist
        except Exception as e:
            print(f"Error getting wishlist: {e}")
            return None

    def remove_from_wishlist(self, user_id: str, product_id: str) -> bool:
        try:
            self.wishlist_collection.update_one(
                {"user_id": user_id},
                {"$pull": {"products": product_id}}
            )
            return True
        except Exception as e:
            print(f"Error removing from wishlist: {e}")
            return False