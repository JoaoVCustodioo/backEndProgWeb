class PessoaException(Exception):
    ...

class PessoaNotFoundError(PessoaException):
    def __init__(self):
        self.status_code = 404
        self.detail = "PESSOA_NAO_ENCONTRADA"
    
class PessoaAlreadyExistError(PessoaException):
    def __init__(self):
        self.status_code = 409
        self.detail = "PESSOA_JA_EXISTE"
    