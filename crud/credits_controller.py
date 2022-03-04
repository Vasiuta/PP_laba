from database import *
from schemas import *
from app import db, token_required
from flask import jsonify


@token_required
def get_credits(current_user):
    credits = db.query(Credit).filter_by(id_borrower=current_user.idUsers)

    return jsonify([e.as_dict() for e in credits]), 200


@token_required
def add_credit(current_user, body: CreditSchema):
    credit = Credit(
        loan_status=body['loan_status'],
        loan_date=body['loan_date'],
        loan_amount=body['loan_amount'],
        interest_rate=body['interest_rate'],
        id_borrower=current_user.idUsers

    )

    db.add(credit)
    db.commit()
    db.refresh(credit)

    return jsonify(credit.as_dict()), 201


@token_required
def add_user_to_credit(current_user, credit_id, user_id):
    user_credit = User_Credit(
        user_id=user_id,
        credit_id=credit_id
    )
    UserCreditSchema().dump(user_credit)

    if db.query(Credit).get(credit_id).id_borrower != current_user.idUsers:
        return jsonify({'Error': 'Permission denied'}), 403

    db.add(user_credit)
    db.commit()
    db.refresh(user_credit)

    return jsonify(user_credit.as_dict()), 201


@token_required
def get_credits_by_user(current_user):
    user_credits = db.query(User_Credit).filter_by(user_id=current_user.idUsers).all()

    credits = []
    for ue in user_credits:
        credits.append(db.query(Credit).get(ue.credit_id))

    return jsonify([e.as_dict() for e in credits]), 200


@token_required
def update_credit(current_user, credit_id, body: CreditSchema):
    print(body['loan_status'])
    credit = db.query(Credit).filter_by(id_borrower=current_user.idUsers, idCredit=credit_id).first()

    if not (bool(credit)):
        return jsonify({'Error': 'Not found'}), 404

    credit.loan_status = body['loan_status']
    credit.loan_date = body['loan_date']
    credit.loan_amount = body['loan_amount']
    credit.interest_rate = body['interest_rate']
    credit.id_borrower = current_user.idUsers

    db.add(credit)
    db.commit()

    return jsonify(credit.as_dict()), 201


@token_required
def delete_credit(current_user, credit_id):
    credit = db.query(Credit).filter_by(id_borrower=current_user.idUsers, idCredit=credit_id).first()
    user_credits = db.query(User_Credit).filter_by(user_id=current_user.idUsers, credit_id=credit_id).first()

    if not (bool(credit)):
        return jsonify({'Error': 'Not found'}), 404

    if bool(user_credits):
        return jsonify({'Error': 'Firstly delete credit from user'}), 400

    db.delete(credit)
    db.commit()

    return jsonify(credit.as_dict()), 202


@token_required
def delete_user_from_credit(current_user, credit_id, user_id):
    user_credit = db.query(User_Credit).filter_by(user_id=user_id, credit_id=credit_id).first()
    if not (bool(user_credit)):
        return jsonify({'Error': 'Not found'}), 404
    if db.query(Credit).get(credit_id).id_borrower != current_user.idUsers:
        return jsonify({'Error': 'Permision denied'}), 403

    db.delete(user_credit)
    db.commit()

    return jsonify(user_credit.as_dict()), 202
