from marshmallow import Schema, fields, validate


class UsersSchema(Schema):
    idUsers = fields.Int()
    username = fields.Str()
    password = fields.Str()
    clientName = fields.Str()
    firstName = fields.Str()
    lastName = fields.Str()
    status = fields.Str()


class CreditSchema(Schema):
    idCredit = fields.Int()
    loan_status = fields.Bool()
    loan_date = fields.Str()
    loan_amount = fields.Int()
    interest_rate = fields.Int()
    id_borrower = fields.Int()


class BalanceSchema(Schema):
    balance = fields.Int()

# class Users(Base):
#     __tablename__ = 'users'
#     idUsers = Column(Integer, nullable=False, primary_key=True)
#     username = Column(String(45))
#     password = Column(String(60))
#     clientName = Column(String(45))
#     firstName = Column(String(45))
#     lastName = Column(String(45))
#     status = Column(Enum('user', 'manager'))
#
#
# class Credit(Base):
#     __tablename__ = 'credit'
#     idCredit = Column(Integer, nullable=False, primary_key=True)
#     loan_status = Column(Boolean, default=False)
#     loan_date = Column(String(45))
#     loan_amount = Column(Integer)
#     interest_rate = Column(Integer)
#     id_borrower = Column(Integer, ForeignKey('users.idUsers'))
#     users = relationship("Users", backref="credites")
#
#
# class Balance(Base):
#     __tablename__ = 'balance'
#     balance = Column(Integer, nullable=False, default=517000, primary_key=True)
