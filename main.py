from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from exceptions import PessoaException
from database import get_db, engine
import crud, models, schemas


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


#read
@app.get("/api/funcionarios/{funcionarioId}", response_model=schemas.Funcionario)
def getFuncionarioById(funcionarioId: int, db: Session = Depends(get_db)):
    try:
        return crud.getFuncionarioById(db, funcionarioId)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)
    

@app.get("/api/funcionarios", response_model=schemas.PaginatedFuncionario)
def getAllFuncionarios(db: Session = Depends(get_db), offset:int = 0, limit: int = 10):
    dbFuncionarios = crud.getAllFuncionarios(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": dbFuncionarios}
    return response
#fim do read


#create
@app.post("/api/funcionarios/signIn", response_model=schemas.Funcionario)
def createFuncionario(funcionario: schemas.funcionarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.createFuncionario(db, funcionario)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)
    
    
#update
@app.put("/api/funcionarios/{funcionarioId}/update", response_model=schemas.Funcionario)
def updateFuncionario(funcionarioId: int, funcionario: schemas.funcionarioCreate, db: Session = Depends(get_db)):
    try: 
        return crud.updateFuncionario(db, funcionarioId, funcionario)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)
    
    
#delete
@app.delete("/api/funcionarios{funcionarioId}/delete")
def deleteFuncionarioById(funcionarioId: int, db: Session = Depends(get_db)):
    try:
        return crud.deleteFuncionarioById(db, funcionarioId)
    except PessoaException as cie:
        raise HTTPException(**cie.__dict__)
    
    
#o crud de hóspede é exatamente igual ao de funcionario, irei(joao) fazer no domingo, ai tenho que mexer no crud.py e main.py pra fazer o hospede