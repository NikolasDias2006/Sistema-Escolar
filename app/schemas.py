from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str
    cargo: str 

class UserResponse(BaseModel):
    id: int
    nome: str
    email: str
    cargo: str
    
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: str
    senha: str
    
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
