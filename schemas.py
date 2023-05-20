from typing import List
from pydantic import BaseModel
from datetime import date

class funcionarioBase(BaseModel):
    nome: str
    funcao: str
    horarioTrabalho: int
    cpf: str
    dataNascimento: date
    horarioTrabalho: int
    fone: str
    
    
class funcionarioCreate(funcionarioBase):
    senha: str
    
class Funcionario(funcionarioBase):
    id: int
    class Config:
        orm_mode = True
    
class PaginatedFuncionario(BaseModel):
    limit: int
    offset: int
    data: List[Funcionario]
    
class hospedeBase(BaseModel):
    nome: str
    email: str
    cpf: str
    fone: str

class hospedeCreate(hospedeBase):
    pass

class Hospede(hospedeBase):
    id: int
    class Config:
        orm_mode = True

class paginatedHospede(BaseModel):
    limit: int
    offset: int
    data: List[Hospede]
    