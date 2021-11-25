from sqlalchemy import create_engine, select, MetaData, Table, Integer, String, Column, ForeignKey, Enum, Boolean, \
    Index, asc, Constraint

from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base



engine = create_engine("mysql+mysqlconnector://root:290900qwer@127.0.0.1:3306/ppdatabase")
engine.connect()

SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    idUsers = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(45))
    password = Column(String(60))
    clientName = Column(String(45))
    firstName = Column(String(45))
    lastName = Column(String(45))
    status = Column(Enum('user', 'manager'))


class Credit(Base):
    __tablename__ = 'credit'
    idCredit = Column(Integer, nullable=False, primary_key=True)
    loan_status = Column(Boolean, default=False)
    loan_date = Column(String(45))
    loan_amount = Column(Integer)
    interest_rate = Column(Integer)
    id_borrower = Column(Integer, ForeignKey('users.idUsers'))
    users = relationship("Users", backref="credites")


class Balance(Base):
    __tablename__ = 'balance'
    balance = Column(Integer, nullable=False, default=517000, primary_key=True)
