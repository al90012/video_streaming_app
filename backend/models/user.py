from flask_pymongo import PyMongo
from flask import current_app
from flask_bcrypt import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

class User:
    @staticmethod
    def create_user(mongo, username, password):
        users = mongo.db.users
        if users.find_one({'username': username}):
            return None
        
        password_hash = generate_password_hash(password).decode('utf-8')
        user_id = users.insert_one({
            'username': username,
            'password_hash': password_hash
        }).inserted_id
        
        return str(user_id)

    @staticmethod
    def verify_user(mongo, username, password):
        users = mongo.db.users
        user = users.find_one({'username': username})
        
        if user and check_password_hash(user['password_hash'], password):
            return user
        return None

    @staticmethod
    def get_user_by_id(mongo, user_id):
        users = mongo.db.users
        return users.find_one({'_id': ObjectId(user_id)})
