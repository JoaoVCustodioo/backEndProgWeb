from sqlalchemy.orm import Session
from exceptions import PessoaAlreadyExistError, PessoaNotFoundError, ReservaAlreadyExistError, ReservaNotFoundError
import bcrypt, models, schemas

#read
def getFuncionarioById(db:Session, funcionarioId: int):
    db_funcionario = db.query(models.Funcionario).get(funcionarioId)
    if db_funcionario is None:
        raise PessoaNotFoundError
    return db_funcionario

def getAllFuncionarios(db:Session, offset: int, limit: int):
    return db.query(models.Funcionario).offset(offset).limit(limit).all()

def getFuncionarioByCpf(db:Session, funcionarioCpf: str):
    return db.query(models.Funcionario).filter(models.Funcionario.cpf == funcionarioCpf).first()

#fim do read


#create
def createFuncionario(db:Session, funcionario: schemas.funcionarioCreate):
    db_funcionario = getFuncionarioByCpf(db, funcionario.cpf)
    funcionario.senha = bcrypt.hashpw(funcionario.senha.encode('utf8'), bcrypt.gensalt())
    if db_funcionario is not None:
        raise PessoaAlreadyExistError
    db_funcionario = models.Funcionario(**funcionario.dict())
    db.add(db_funcionario)
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario



#update
def updateFuncionario(db:Session, funcionarioId: int, funcionario: schemas.funcionarioCreate):
    dbFuncionario = getFuncionarioById(db, funcionarioId)
    dbFuncionario.nome = funcionario.nome
    dbFuncionario.cpf = funcionario.cpf
    if funcionario.senha != "":
        dbFuncionario.senha = bcrypt.hashpw(funcionario.senha.encode('utf8'), bcrypt.gensalt())
    db.commit()
    db.refresh(dbFuncionario)
    return dbFuncionario


#delete
def deleteFuncionarioById(db: Session, funcionarioId: int):
    dbFuncionario = getFuncionarioById(db, funcionarioId)
    db.delete(dbFuncionario)
    db.commit()
    return



#crud para hóspedes, mesma coisa do crud de funcionario
#read
def getHospedeById(db:Session, hospedeId: int):
    db_hospede = db.query(models.Hospede).get(hospedeId)
    if db_hospede is None:
        raise PessoaNotFoundError
    return db_hospede

def getAllHospedes(db:Session, offset: int, limit: int):
    return db.query(models.Hospede).offset(offset).limit(limit).all()

def getHospedeByCpf(db:Session, hospedeCpf: str):
    return db.query(models.Hospede).filter(models.Hospede.cpf == hospedeCpf).first()

#fim do read


#create
def createHospede(db:Session, hospede: schemas.hospedeCreate):
    db_hospede = getHospedeByCpf(db, hospede.cpf)
    if db_hospede is not None:
        raise PessoaAlreadyExistError
    db_hospede = models.Hospede(**hospede.dict())
    db.add(db_hospede)
    db.commit()
    db.refresh(db_hospede)
    return db_hospede


#update
def updateHospede(db:Session, hospedeId: int, hospede: schemas.hospedeCreate):
    dbHospede = getHospedeById(db, hospedeId)
    dbHospede.nome = hospede.nome
    dbHospede.cpf = hospede.cpf
    dbHospede.email = hospede.email
    
    db.commit()
    db.refresh(dbHospede)
    return dbHospede

#delete
def deleteHospedeById(db: Session, hospedeId: int):
    dbHospede = getHospedeById(db, hospedeId)
    db.delete(dbHospede)
    db.commit()
    return


#crud para reserva abaixo

#read
def getReservaById(db:Session, reservaId: int):
    db_reserva = db.query(models.Reserva).get(reservaId)
    if db_reserva is None:
        raise ReservaNotFoundError
    return db_reserva

def getAllReservas(db:Session, offset: int, limit: int):
    return db.query(models.Reserva).offset(offset).limit(limit).all()

#fim do read

#create
def createReserva(db:Session, reserva: schemas.reservaCreate):
    
    db_reserva = models.Reserva(**reserva.dict())
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return db_reserva


#update
def updateReserva(db:Session, reservaId: int, reserva: schemas.reservaCreate):
    dbReserva = getReservaById(db, reservaId)
    dbReserva.nome = reserva.nome
    dbReserva.dataCheckIn = reserva.dataCheckIn
    dbReserva.dataCheckOut = reserva.dataCheckOut
    dbReserva.valor = reserva.valor
    db.commit()
    db.refresh(dbReserva)
    return dbReserva

#delete
def deleteReservaById(db: Session, reservaId: int):
    dbReserva = getReservaById(db, reservaId)
    db.delete(dbReserva)
    db.commit()
    return