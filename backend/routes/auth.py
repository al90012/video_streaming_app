from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token
from models.user import User
from flask_pymongo import PyMongo

auth_bp = Blueprint('auth', __name__)

# Helper to get mongo instance from app context
def get_mongo():
    return current_app.extensions['pymongo']

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    mongo = get_mongo()
    user_id = User.create_user(mongo, username, password)

    if not user_id:
        return jsonify({"msg": "Username already exists"}), 409

    return jsonify({"msg": "User created", "user_id": user_id}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    mongo = get_mongo()
    user = User.verify_user(mongo, username, password)

    if not user:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=str(user['_id']))
    return jsonify(access_token=access_token), 200
