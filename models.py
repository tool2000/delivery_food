import enum
from db_connect import db
from datetime import datetime

class OrderMethod(enum.Enum):
    card = "card"
    cash = "cash"

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(10), primary_key=True, nullable=False)
    delivery_address = db.Column(db.String(100), nullable=False)

    deliveryorder = db.relationship("DeliveryOrder", backref='user')

    def __init__(self, id, delivery_address):
        self.id = id
        self.delivery_address = delivery_address

class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.String(30), primary_key=True, nullable=False)
    store_address = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)

    storedelivery = db.relationship("DeliveryOrder", backref='store')

    def __init__(self, id, store_address, contact_number):
        self.id = id
        self.store_address = store_address
        self.contact_number = contact_number

class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.String(30), primary_key=True, nullable=False)
    store_id = db.Column(db.String(30))
    price = db.Column(db.Integer, nullable=False)
    fee = db.Column(db.Integer)
    
    menudelivery = db.relationship("DeliveryOrder", backref='menu')


    def __init__(self, id, price, fee):
        self.id = id
        self.price = price
        self.fee = fee

class DeliveryOrder(db.Model):
    __tablename__ = 'delivery_order'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    order_dt = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.String(10), db.ForeignKey('user.id'))
    delivery_address = db.Column(db.String(100))
    menu_id = db.Column(db.String(30), db.ForeignKey('menu.id'))
    store_id = db.Column(db.String(10), db.ForeignKey('store.id'))
    store_contact_number = db.Column(db.String(20))
    total_price = db.Column(db.Integer, nullable=False)
    delivery_fee = db.Column(db.Integer)
    order_method = db.Column(db.Enum(OrderMethod), nullable=False)
    
    def __init__(self, user_id, delivery_address, menu_id, store_id, store_contact_number, total_price, delivery_fee, order_method):
        self.user_id = user_id
        self.delivery_address = delivery_address
        self.menu_id = menu_id
        self.store_id = store_id
        self.store_contact_number = store_contact_number
        self.total_price = total_price
        self.delivery_fee = delivery_fee
        self.order_method = order_method



