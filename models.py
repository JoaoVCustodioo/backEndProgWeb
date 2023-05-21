from sqlalchemy import Column, Date, Integer, String
from database import Base



#models são as classes que representam as tabelas e seus atributos, só que em código 

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    dataNascimento = Column(Date, index=True)
    funcao = Column(String(50))
    horarioTrabalho = Column (Integer)
    cpf = Column(String(14), unique=True, index=True)
    fone = Column(String(13))
    senha = Column(String(255))
    

class Hospede(Base):
    __tablename__ = 'hospedes'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    cpf = Column(String(14), unique=True, index=True)
    fone = Column(String(13))
    email = Column(String(100), unique=True, index=True)
    


class Reserva(Base):
    __tablename__ = 'reservas'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50))
    dataCheckIn = Column(Date)
    dataCheckOut = Column(Date)
    valor = Column(String(20))
    requisitos = Column (String(200))
    