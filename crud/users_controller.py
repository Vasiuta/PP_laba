from database import *
from schemas import *
from app import db, bcrypt
from flask import jsonify


def create_user(body: UsersSchema):
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

    return jsonify(user.as_dict()), 201
