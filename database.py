from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, ForeignKey, Enum, Boolean, Index, asc, Constraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/ppdatabase")
Base = declarative_base()
meta = MetaData()
meta.create_all(engine)

connection = engine.connect()

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
    id_borrower = Column(Integer, ForeignKey('id.borrower'))
    fk_Credit_Users_idx = Index(id_borrower, asc)
    fk_Credit_Users = Constraint
    users = relationship("Users", backref="credites")

class Balance(Base):
    __tablename__ = 'balance'
    balance = Column(Integer, nullable=False, default=517000)

if __name__ == '__main__':
    Base.MetaData.create_all(engine)

# CREATE TABLE IF NOT EXISTS `mydb`.`Users` (
#   `idUsers` INT NOT NULL,
#   `username` VARCHAR(45) NULL,
#   `password` VARCHAR(45) NULL,
#   `clientName` VARCHAR(45) NULL,
#   `firstName` VARCHAR(45) NULL,
#   `lastName` VARCHAR(45) NULL,
#   `status` ENUM('user', 'manager') NULL,
#   PRIMARY KEY (`idUsers`))

# CREATE TABLE IF NOT EXISTS `mydb`.`Credit` (
#   `idCredit` INT NOT NULL,
#   `loan_status` TINYINT NULL DEFAULT 0,
#   `loan_date` VARCHAR(45) NULL,
#   `loan_amount` INT NULL,
#   `interest_rate` INT NULL COMMENT 'minimum : 0\nmaximum : 30\n',
#   `id_borrower` INT NOT NULL,
#   PRIMARY KEY (`idCredit`),
#   INDEX `fk_Credit_Users_idx` (`id_borrower` ASC) VISIBLE,
#   CONSTRAINT `fk_Credit_Users`
#     FOREIGN KEY (`id_borrower`)
#     REFERENCES `mydb`.`Users` (`idUsers`)
#     ON DELETE NO ACTION
#     ON UPDATE NO ACTION)

# CREATE TABLE IF NOT EXISTS `mydb`.`Balance` (
#   `balance` INT NOT NULL DEFAULT 517000)
