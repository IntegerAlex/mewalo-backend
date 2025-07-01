from app.database.misc_database import MiscDatabase
from datetime import datetime

class MiscService:
    def contact_us(self, data: dict) -> bool:
        """
        Contact us.
        :param data: Dictionary containing contact information.
        :return: True if contact is sent successfully, False otherwise.
        """
        try:
            data["timestamp"] = datetime.now()
            MiscDatabase().add_enquiry(data)
            return True
        except Exception as e:
            print(f"Error adding enquiry: {e}")
            return False
    
    def subscribe(self, data: dict) -> bool:
        """
        Subscribe to the newsletter.
        :param data: Dictionary containing subscription information.
        :return: True if subscription is sent successfully, False otherwise.
        """
        try:
            MiscDatabase().add_subscription(data)
            return True
        except Exception as e:
            print(f"Error adding subscription: {e}")
            return False