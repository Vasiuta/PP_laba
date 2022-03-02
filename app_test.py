import pytest
import json
from app import flask_app, db
from database import Users, Credit


def test_register_user():
    client = flask_app.test_client()
    request_params = {
        "username": "username",
        "password": "1234567890",
        "clientName": "vstoleksiy",
        "firstName": "Oleksiy",
        "lastName": "Vasiuta",
        "status": "manager"
    }

    response = client.post(
        '/register',
        json=request_params
    )

    assert response.status_code == 201
    assert response.json['message'] == 'Registered successfully'


def test_login_user():
    client = flask_app.test_client()
    request_params = {
        "username": "username",
        "password": "1234567890"
    }

    response = client.post(
        '/login',
        json=request_params
    )
    assert response.status_code == 200
    assert response.json['token']


def test_login_user_bad():
    client = flask_app.test_client()
    request_params = {
        "username": "username",
        "password": "1234567ascfqwc890"
    }

    response = client.post(
        '/login',
        json=request_params
    )
    assert response.status_code == 401
    assert response.json['Error']


def generate_header():
    client = flask_app.test_client()
    request_params = {
        "username": "username",
        "password": "1234567890"
    }
    token = client.post('/login', json=request_params).json['token']
    return {
        'x-access-tokens': token[2:len(token) - 1]
    }


def get_super_user_id():
    return db.query(Users).filter_by(username='username').first().idUsers


def get_credit_id():
    return db.query(Credit).filter_by(id_borrower=get_super_user_id()).first().idCredit


def test_add_credit():
    client = flask_app.test_client()
    request_params = {
        "loan_status": "true",
        "loan_date": "29.09",
        "loan_amount": 3000,
        "interest_rate": 20,
        "id_borrower": 1
    }

    response = client.post(
        '/credits',
        json=request_params,
        headers=generate_header()
    )

    assert response.status_code == 201
    assert response.json


def test_get_credits():
    client = flask_app.test_client()

    response = client.get(
        '/credits',
        headers=generate_header()
    )
    assert response.status_code == 200
    assert response.json


def test_upgrade_credit():
    client = flask_app.test_client()
    request_params = {
        "loan_status": "True",
        "loan_date": "2.09",
        "loan_amount": 5000,
        "interest_rate": 20
    }

    response = client.put(
        f"/credits/{get_credit_id()}",
        json=request_params,
        headers=generate_header()
    )

    # assert response.status_code == 201
    assert response.json


def test_delete_credit():
    client = flask_app.test_client()

    response = client.delete(
        f"/credits/{get_credit_id()}",
        headers=generate_header()
    )
    # assert response.status_code == 202
    assert response.json


def test_add_user_to_credit():
    client = flask_app.test_client()
    request_params = {
        "user_id": 30,
        "credit_id": 16
    }

    response = client.post(
        f"/credits_by_user/{get_credit_id()}/{get_super_user_id()}",
        json=request_params,
        headers=generate_header()
    )

    assert response.status_code == 201
    assert response.json


def test_get_credits_by_user():
    client = flask_app.test_client()

    response = client.get(
        '/credits_by_user',
        headers=generate_header()
    )
    assert response.status_code == 200
    assert response.json


def test_delete_user_from_credit():
    client = flask_app.test_client()
    response = client.delete(
        f"/credits_by_user/{get_credit_id()}/{get_super_user_id()}",
        headers=generate_header()
    )

    assert response.status_code == 202
    assert response.json
