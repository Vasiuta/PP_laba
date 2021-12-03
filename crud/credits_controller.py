from database import *
from schemas import *
from app import db
from flask import jsonify


def get_credits():
    credits = db.query(Credit).all()

    return jsonify([e.as_dict() for e in credits]), 200


def add_credit(body: CreditSchema):
    credit = Credit(
        loan_status=body['loan_status'],
        loan_date=body['loan_date'],
        loan_amount=body['loan_amount'],
        interest_rate=body['interest_rate'],
        id_borrower=body['id_borrower']

    )

    db.add(credit)
    db.commit()
    db.refresh(credit)

    return jsonify(credit.as_dict()), 201


def update_credit(credit_id, body: CreditSchema):
    credit = db.query(Credit).get(credit_id)

    credit.loan_status = body['loan_status'],
    credit.loan_date = body['loan_date'],
    credit.loan_amount = body['loan_amount'],
    credit.interest_rate = body['interest_rate'],
    credit.id_borrower = body['id_borrower']

    db.merge(credit)
    db.flush()
    db.commit()

    return jsonify(credit.as_dict()), 201


def delete_credit(credit_id):
    credit = db.query(Credit).get(credit_id)

    db.delete(credit)
    db.commit()

    return jsonify(credit.as_dict()), 202


def get_credits_by_user(user_id):
    credits = db.query(Credit).filter(Credit.owner_id == user_id)

    return jsonify([e.as_dict() for e in credits]), 200


def add_user_to_credit(credit_id, user_id):
    pass
    # user_credit = Credit(
    #     user_id=user_id,
    #     event_id=event_id
    # )
    # UserEventSchema().dump(user_event)
    #
    # db.add(user_event)
    # db.commit()
    # db.refresh(user_event)
    #
    # return jsonify(user_event.as_dict()), 201


def remove_user_from_credit(credit_id, user_id):
    pass
