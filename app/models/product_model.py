from mongoengine import Document, StringField, IntField, FloatField, ListField, ReferenceField, DictField

class Product(Document):
    product_id = StringField(required=True, unique=True)
    product_name = StringField(required=True)
    product_description = StringField()
    product_price = FloatField(required=True)
    product_category = StringField(required=True)
    product_sub_category = StringField(required=True)
    product_barcode = StringField(required=True)
    product_quantity = IntField(required=True)
    product_unit = StringField(required=True)
    product_coupon = DictField()
    product_delivery = DictField()
    product_manufacturer = StringField()
    product_image_url = StringField()
