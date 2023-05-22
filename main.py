from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from exceptions import PessoaException, ReservaException
from database import get_db, engine
import crud, models, schemas
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


#read
@app.get("/api/funcionarios/{funcionarioId}", dependencies=[Depends(JWTBearer())], response_model=schemas.Funcionario)
def getFuncionarioById(funcionarioId: int, db: Session = Depends(get_db)):
    try:
        return crud.getFuncionarioById(db, funcionarioId)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)
    

@app.get("/api/funcionarios", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedFuncionario)
def getAllFuncionarios(db: Session = Depends(get_db), offset:int = 0, limit: int = 10):
    dbFuncionarios = crud.getAllFuncionarios(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": dbFuncionarios}
    return response
#fim do read


#create
@app.post("/api/funcionarios", dependencies=[Depends(JWTBearer())], response_model=schemas.Funcionario)
def createFuncionario(funcionario: schemas.funcionarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.createFuncionario(db, funcionario)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)
    
    
#update
@app.put("/api/funcionarios/{funcionarioId}", dependencies=[Depends(JWTBearer())], response_model=schemas.Funcionario)
def updateFuncionario(funcionarioId: int, funcionario: schemas.funcionarioCreate, db: Session = Depends(get_db)):
    try: 
        return crud.updateFuncionario(db, funcionarioId, funcionario)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)
    
    
#delete
@app.delete("/api/funcionarios/{funcionarioId}", dependencies=[Depends(JWTBearer())])
def deleteFuncionarioById(funcionarioId: int, db: Session = Depends(get_db)):
    try:
        return crud.deleteFuncionarioById(db, funcionarioId)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)
    
    
#o crud de hóspede é exatamente igual ao de funcionario, irei(joao) fazer no domingo, ai tenho que mexer no crud.py e main.py pra fazer o hospede

#endpoint de hospede
#read
@app.get("/api/hospedes/{hospedeId}", dependencies=[Depends(JWTBearer())], response_model=schemas.Hospede)
def getHospedeById(hospedeId: int, db: Session = Depends(get_db)):
    try:
        return crud.getHospedeById(db, hospedeId)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)
    

@app.get("/api/hospedes", dependencies=[Depends(JWTBearer())], response_model=schemas.paginatedHospede)
def getAllHospedes(db: Session = Depends(get_db), offset:int = 0, limit: int = 10):
    dbHospede = crud.getAllHospedes(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": dbHospede}
    return response
#fim do read

#create
@app.post("/api/hospedes", dependencies=[Depends(JWTBearer())], response_model=schemas.Hospede)
def createHospede(hospede: schemas.hospedeCreate, db: Session = Depends(get_db)):
    try:
        return crud.createHospede(db, hospede)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)

#update
@app.put("/api/hospedes/{hospedeId}", dependencies=[Depends(JWTBearer())], response_model=schemas.Hospede)
def updateHospede(hospedeId: int, hospede: schemas.hospedeCreate, db: Session = Depends(get_db)):
    try: 
        return crud.updateHospede(db, hospedeId, hospede)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)
    
#delete
@app.delete("/api/hospedes/{hospedeId}", dependencies=[Depends(JWTBearer())])
def deleteHospedeById(hospedeId: int, db: Session = Depends(get_db)):
    try:
        return crud.deleteHospedeById(db, hospedeId)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)
    
    
#endpoint de reserva
#read
@app.get("/api/reservas/{reservaId}", dependencies=[Depends(JWTBearer())], response_model=schemas.Reserva)
def getReservaById(reservaId: int, db: Session = Depends(get_db)):
    try:
        return crud.getReservaById(db, reservaId)
    except ReservaException as cie:
        raise HTTPException(**cie.__dict__)
    

@app.get("/api/reservas", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedReserva)
def getAllReservas(db: Session = Depends(get_db), offset:int = 0, limit: int = 10):
    dbReservas = crud.getAllReservas(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": dbReservas}
    return response
#fim do read

#create
@app.post("/api/reservas", dependencies=[Depends(JWTBearer())], response_model=schemas.Reserva)
def createReserva(reserva: schemas.reservaCreate, db: Session = Depends(get_db)):
    try:
        return crud.createReserva(db, reserva)
    except ReservaException as cie:
        raise HTTPException(**cie.__dict__)
   
   
#update
@app.put("/api/reservas/{reservaId}", dependencies=[Depends(JWTBearer())], response_model=schemas.Reserva)
def updateReserva(reservaId: int, reserva: schemas.reservaCreate, db: Session = Depends(get_db)):
    try: 
        return crud.updateReserva(db, reservaId, reserva)
    except ReservaException as cie:
        raise HTTPException(**cie.__dict__)
    
#delete
@app.delete("/api/reservas/{reservaId}", dependencies=[Depends(JWTBearer())])
def deleteReservaById(reservaId: int, db: Session = Depends(get_db)):
    try:
        return crud.deleteReservaById(db, reservaId)
    except ReservaException as cie:
        raise HTTPException(**cie.__dict__)
    
    
#signup
@app.post("/api/signup", tags=["funcionario"])
async def create_funcionario_signup(funcionario: schemas.funcionarioCreate = Body(...), db: Session = Depends(get_db)):
    try:
        crud.createFuncionario(db, funcionario)
        return signJWT(funcionario.nome)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)
    
    
#login
@app.post("/api/login", tags=["funcionario"])
async def user_login(funcionario: schemas.funcionarioLoginSchema = Body(...), db: Session = Depends(get_db)):
    if crud.checkFuncionario(db, funcionario):
        return signJWT(funcionario.nome)
    return {
        "error": "E-mail ou senha incorretos!"
}

