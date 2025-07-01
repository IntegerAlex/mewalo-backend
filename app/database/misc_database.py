from app.config import db

class MiscDatabase:
    def add_enquiry(self, enquiry_data: dict) -> bool:
        """
        Add a new enquiry to the database, including a timestamp.
        :param enquiry_data: Dictionary containing enquiry information, including timestamp.
        :return: True if enquiry is added successfully, False otherwise.
        """
        try:
            db.enquiries.insert_one(enquiry_data)
            return True
        except Exception as e:
            print(f"Error adding enquiry: {e}")
            return False
        
    def add_subscription(self, subscription_data: dict) -> bool:
        """
        Add a new subscription to the database.
        :param subscription_data: Dictionary containing subscription information.
        :return: True if subscription is added successfully, False otherwise.
        """
        try:
            db.subscriptions.insert_one(subscription_data)
            return True
        except Exception as e:
            print(f"Error adding subscription: {e}")
            return False