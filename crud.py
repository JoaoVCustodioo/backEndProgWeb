from sqlalchemy.orm import Session
from exceptions import PessoaAlreadyExistError, PessoaNotFoundError
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


def deleteFuncionarioById(db: Session, funcionarioId: int):
    dbFuncionario = getFuncionarioById(db, funcionarioId)
    db.delete(dbFuncionario)
    db.commit()
    return