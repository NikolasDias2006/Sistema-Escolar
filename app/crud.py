from sqlalchemy.orm import Session
from app.models import Funcionario
from app.schemas import UserCreate, UserLogin
from werkzeug.security import generate_password_hash, check_password_hash

def criar_usuario(db: Session, usuario: UserCreate):
    hashed_password = generate_password_hash(usuario.senha)
    db_usuario = Funcionario(
        nome=usuario.nome,
        email=usuario.email,
        senha=hashed_password,
        cargo=usuario.cargo
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def autenticar_usuario(db: Session, usuario: UserLogin):
    db_usuario = db.query(Funcionario).filter(Funcionario.email == usuario.email).first()
    if db_usuario and check_password_hash(db_usuario.senha, usuario.senha):
        return db_usuario
    return None
