from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import Sessionlocal
from werkzeug.security import check_password_hash

router = APIRouter()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

# Rota para registrar um novo usuário
@router.post("/users/", response_model=schemas.UserResponse)
def criar_usuario(usuario: schemas.UserCreate, db: Session = Depends(get_db)):
    db_usuario = crud.criar_usuario(db=db, usuario=usuario)
    return db_usuario

# Rota para login de usuário
@router.post("/login/")
def login(usuario: schemas.UserLogin, db: Session = Depends(get_db)):
    db_usuario = crud.autenticar_usuario(db=db, usuario=usuario)
    if db_usuario is None:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")
    return {"msg": "Login bem-sucedido", "user_id": db_usuario.id}
