from marshmallow import Schema, fields, validate


class UsersSchema(Schema):
    username = fields.Str()
    password = fields.Str()
    clientName = fields.Str()
    firstName = fields.Str()
    lastName = fields.Str()
    status = fields.Str()


class CreditSchema(Schema):
    loan_status = fields.Str()
    loan_date = fields.Str()
    loan_amount = fields.Int()
    interest_rate = fields.Int()
    id_borrower = fields.Int()


class UserCreditSchema(Schema):
    user_id = fields.Int()
    credit_id = fields.Int()


class LoginSchema(Schema):
    username = fields.Str()
    password = fields.Str()
