from mongoengine import Document, StringField, EmailField, ValidationError
import re

class User(Document):
    meta = {
        'collection': 'users',
        'indexes': [
            {'fields': ['email'], 'unique': True},
            {'fields': ['phone'], 'unique': True}
        ]
    }

    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    email = EmailField(required=True, unique=True, max_length=120)
    phone = StringField(required=True, unique=True, max_length=15)

   def __repr__(self):
       return f"<User {self.first_name} {self.last_name} - {self.email}>"