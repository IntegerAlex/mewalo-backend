from jwt import encode, decode
import random
from app.database.user_database import UserDatabase
temp_otp =  {}
temp_user = {}
class AuthService:
    def register_user(self, user_data: dict) -> bool:
        """
        Register a new user.
        :param user_data: Dictionary containing user information.
        :return: True if user is registered successfully, False otherwise.
        """
        try:
            temp_user[user_data["phone"]] = user_data
            self.generate_otp(user_data["phone"])
            return True
        except Exception as e:
            print(f"Error validating user data: {e}")
            return False
    



    def generate_otp(self, phone: str) -> str:
        """
        Generate a one-time password (OTP) for the user.
        :param phone: User's phone number.
        :return: OTP as a string.
        """
        otp = random.randint(100000, 999999)
        try:
            self.send_otp(phone, otp)
            temp_otp[phone] = otp
            print(temp_otp)
            return True
        except Exception as e:
            print(f"Error sending OTP: {e}")
            return False
    
    def verify_otp(self, phone: str, otp: str) -> bool:
        """
        Verify the OTP for the user.
        :param phone: User's phone number.
        :param otp: OTP to verify.
        :return: True if OTP is verified successfully, False otherwise.
        """
        if phone not in temp_otp:
            return False
        if temp_otp[phone] != int(otp):
            return False
        del temp_otp[phone]
        return True
    
    def send_otp(self, phone: str, otp: str) -> bool:
        """
        Send an OTP to the user.
        :param phone: User's phone number.
        :param otp: OTP to send.
        :return: True if OTP is sent successfully, False otherwise.
        """
        return True
    
    def generate_jwt(self, phone: str) -> str:
        """
        Generate a JWT for the user.
        :param phone: User's phone number.
        :return: JWT as a string.
        """
        return encode({"phone": phone}, "secret", algorithm="HS256")