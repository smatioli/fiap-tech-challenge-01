from sqlalchemy import Column, Integer, String, BigInteger, Enum
from app.db.base import Base
import enum

class ProductionDB(Base):
    __tablename__ = 'producao'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    product = Column('produto', String, nullable=False)
    year = Column('ano', Integer, nullable=False)
    quantity = Column('quantidade', BigInteger, nullable=False)

class ProcessingDB(Base):
    __tablename__ = 'processamento'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    grape_classification = Column('classificacao_uva', String, nullable=False)
    grape_cultivar = Column('cultivar', String, nullable=False)
    year = Column('ano', Integer, nullable=False)
    quantity = Column('quantidade', BigInteger, nullable=False)


class CommercializationDB(Base):
    __tablename__ = 'comercializacao'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    product = Column('produto', String, nullable=False)
    year = Column('ano', Integer, nullable=False)
    quantity = Column('quantidade', BigInteger, nullable=False)

class ImportationDB(Base):
    __tablename__ = 'importacao'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    grape_derivative = Column('derivado_uva', String, nullable=False)
    country = Column('pais', String, nullable=False)
    year = Column('ano', Integer, nullable=False)
    quantity = Column('quantidade', BigInteger, nullable=False)
    value = Column('valor', BigInteger, nullable=False)


class ExportationDB(Base):
    __tablename__ = 'exportacao'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    grape_derivative = Column('derivado_uva', String, nullable=False)
    country = Column('pais', String, nullable=False)
    year = Column('ano', Integer, nullable=False)
    quantity = Column('quantidade', BigInteger, nullable=False)
    value = Column('valor', BigInteger, nullable=False)


# class AccountType(enum.Enum):
#     PRODUCTION = "producao"
#     PROCESSING = "processamento"
#     COMMERCIALIZATION = "comercializacao"
#     IMPORTATION = "importacao"
#     EXPORTATION = "exportacao"
    
# class VitiBrasilDB(Base):
#     __tablename__ = 'vitibrasil'    
#     id = Column('id', Integer, primary_key=True, autoincrement=True)
#     account = Column('conta', Enum(AccountType), nullable=False, )
#     year = Column('ano', Integer, nullable=False)
#     product = Column('produto', String, nullable=False)
#     derivative = Column('derivado', String, nullable=False)
#     classification = Column('classificacao', String, nullable=False, default="NA")
#     cultivar = Column('cultivar', String, nullable=False, default="NA")    
#     country = Column('pais', String, nullable=False,default="NA")
#     quantity = Column('quantidade', BigInteger, nullable=False)
#     value = Column('valor', BigInteger, nullable=False)


class UserDB(Base):
    __tablename__ = 'usuarios'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)