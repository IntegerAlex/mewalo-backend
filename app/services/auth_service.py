from jwt import encode, decode
import random

from app.database.user_database import UserDatabase
import http.client
import json
import os
from dotenv import load_dotenv

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
        
    def send_otp_prod(self, phone: int, otp: str) -> bool:
        """
        Send an OTP via MSG91.
        :param phone: Full phone number (e.g., 919XXXXXXXXX).
        :param otp: The OTP to send.
        :return: True if sent successfully, False otherwise.
        """
        load_dotenv()  # Load .env variables

        auth_key = os.getenv("MSG91_AUTH_KEY")
        sender_id = os.getenv("MSG91_SENDER_ID")
        template_id = os.getenv("MSG91_TEMPLATE_ID")

        if not all([auth_key, sender_id, template_id]):
            print("Missing environment variables")
            return False

        conn = http.client.HTTPSConnection("control.msg91.com")

        payload = json.dumps({
            "template_id": template_id,
            "sender": sender_id,
            "short_url": "0",  # or "1"
            "mobiles": phone,
            "VAR1": otp,
            "VAR2": "Support"  # Optional
        })

        headers = {
            "Authkey": auth_key,
            "accept": "application/json",
            "content-type": "application/json"
        }

        try:
            conn.request("POST", "/api/v5/flow/", payload, headers)
            res = conn.getresponse()
            data = res.read()
            print("MSG91 Response:", data.decode("utf-8"))
            return res.status == 200
        except Exception as e:
            print("Error sending OTP:", e)
            return False

    def send_otp(self, phone: int, otp: str) -> bool:
        """
        Send an OTP via MSG91.
        :param phone: Full phone number (e.g., 919XXXXXXXXX).
        :param otp: The OTP to send.
        :return: True if sent successfully, False otherwise.
        """
        print(f"OTP: {otp} sent to {phone}")
        return True
    
    def generate_otp(self, phone: str) -> str:
        """
        Generate a one-time password (OTP) for the user.
        :param phone: User's phone number.
        :return: OTP as a string.
        """
        otp = random.randint(100000, 999999)
        try:
            self.send_otp(phone, str(otp))
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
    
    
        return True
    
    def generate_jwt(self, phone: str) -> str:
        """
        Generate a JWT for the user.
        :param phone: User's phone number.
        :return: JWT as a string.
        """
        return encode({"phone": phone}, "secret", algorithm="HS256")