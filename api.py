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
    return render_template('index.html')
    
@board.route("/order_list")
def order_list():
    return render_template('order_list.html')