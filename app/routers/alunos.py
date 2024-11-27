from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

@router.post("/alunos/")
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(database.Sessionlocal)):
    novo_aluno = models.Aluno(nome=aluno.nome, responsavel=aluno.responsavel)
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno
