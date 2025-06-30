from app.config import db
from datetime import datetime

class UserDatabase:
    def create_user(self, user_data: dict) -> bool:
        """
        Create a new user.
        :param user_data: Dictionary containing user information.
        :return: True if user is created successfully, False otherwise.
        """
        db.users.insert_one(user_data)
        return True

    def find_one(self, query: dict) -> dict | None:
        """
        Find a single user by a query.
        :param query: Dictionary containing query parameters.
        :return: User data if found, None otherwise.
        """
        user = db.users.find_one(query)
        return user
    