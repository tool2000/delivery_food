from flask import Blueprint, render_template, jsonify, request
from models import OrderMethod, User, Store, Menu, DeliveryOrder
from db_connect import db

board = Blueprint('board',__name__)

# 작성한 게시글을 볼 수 있도록 함수를 완성하세요.
@board.route("/")
def home():
    return render_template('index.html')
    
@board.route("/post",methods=["POST", "GET"])
def create_post():
    print(request.form)
    user_id = request.form['user_id']
    order_method = request.form['order_method']
    menu = request.form['menu']

    user = db.session.query(User).filter_by(id=user_id).first()
    delivery_address = user.delivery_address

    MT = db.session.query(Menu).filter_by(id=menu).first()
    store_id, price, fee = MT.store_id, MT.price, MT.fee
    total_price = price + fee

    store = db.session.query(Store).filter_by(id=store_id).first()
    contact_number = store.contact_number

    order = DeliveryOrder(user_id, delivery_address, menu, store_id, contact_number, total_price, fee, order_method)
    db.session.add(order)
    db.session.commit()

    return render_template('index.html')
    
@board.route("/order_list")
def order_list():
    return render_template('order_list.html')