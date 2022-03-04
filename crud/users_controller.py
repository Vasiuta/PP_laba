import pytest
from database import *
from schemas import *
from app import db, bcrypt, app
from flask import jsonify
from flask_jwt import jwt
import datetime

def register_user(body: UsersSchema):
    user = Users(
        username=body['username'],
        password=bcrypt.generate_password_hash(body['password']),
        clientName=body['clientName'],
        firstName=body['firstName'],
        lastName=body['lastName'],
        status=body['status']
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return jsonify({'message': 'Registered successfully'}), 201


def login_user(body: LoginSchema):
    if not body or not body['username'] or not body['password']:
        return jsonify({'Error': 'Authentication failed'}), 401

    user = db.query(Users).filter_by(username=body['username']).first()
    if bcrypt.check_password_hash(user.password, body['password']):
        token = jwt.encode(
            {'id': user.idUsers,
             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
            app.app.config['SECRET_KEY'],
            "HS256"
        )

        return jsonify({'token': str(token)}), 200

    return jsonify({'Error': 'Authentication failed'}), 401
