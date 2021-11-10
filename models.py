import enum
from db_connect import db
from datetime import datetime

class OrderMethod(enum.Enum):
    card = 
    cash = 

class User(db.Model):
    __tablename__ = 'user'


    def __init__(self):
        

class Store(db.Model):
    __tablename__ = 'store'
    def __init__(self, id, store_address, contact_number):
        self.

class Menu(db.Model):
    __tablename__ = 'menu'
    def __init__(self, store_id, price, fee):
        self.

class DeliveryOrder(db.Model):
    __tablename__ = 'delivery_order'
    def __init__(self, user_id, delivery_address, menu_id, store_id, store_contact_number, total_price, delivery_fee, order_method):
        self.


