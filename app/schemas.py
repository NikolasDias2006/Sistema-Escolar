from pydantic import BaseModel

class LoginSchema(BaseModel):
    email: str
    senha: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class ErrorResponse(BaseModel):
    detail: str

class AlunoCreate(BaseModel):
    nome: str
    responsavel: str

class AlunoResponse(AlunoCreate):
    id: int
    faltas: int

class AlunoUpdate(BaseModel):
    quantidade: int  


class BoletimCreate(BaseModel):
    aluno_id: int
    disciplina: str
    nota1: int
    nota2: int

class BoletimResponse(BoletimCreate):
    id: int
    media: float  

class BoletimCreate(BaseModel):
    aluno_id: int
    disciplina: str
    nota1: int
    nota2: int

class BoletimResponse(BoletimCreate):
    id: int
    media: float 
