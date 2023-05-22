from typing import List
from pydantic import BaseModel
from datetime import date


class funcionarioBase(BaseModel):
    nome: str
    funcao: str
    horarioTrabalho: int
    cpf: str
    dataNascimento: date
    fone: str
    
    
class funcionarioCreate(funcionarioBase):
    senha: str
    pass
    
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
    
    
class reservaBase(BaseModel):
    nome: str
    dataCheckIn: date
    dataCheckOut: date
    valor: str
    requisitos: str
    
class reservaCreate(reservaBase):
    pass
    
class Reserva(reservaBase):
    id: int
    class Config:
        orm_mode = True
    
class PaginatedReserva(BaseModel):
    limit: int
    offset: int
    data: List[Reserva]