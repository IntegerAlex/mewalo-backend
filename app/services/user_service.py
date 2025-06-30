import userDb from database as db
from PyJWT import encode, decode
from typing import Optional

class UserService:
    def create_user(self, user_data: dict) -> bool:
        """
        Create a new user in the database.
        :param user_data: Dictionary containing user information.
        :return: True if user is created successfully, False otherwise.
        """
        try:
            user = userDb.add(**user_data)
            userDb.save(user)
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
        
    def get_user_by_phone(self, phone: str) -> Optional[dict]:
        """
        Retrieve a user by their phone number.
        :param phone: User's phone number.
        :return: User data if found, None otherwise.
        """
        try:
            user = userDb.find_one({"phone": phone})
            return user if user else None
        except Exception as e:
            print(f"Error retrieving user by phone: {e}")
            return None
