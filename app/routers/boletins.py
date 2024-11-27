from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

@router.post("/boletins/")
def criar_boletim(boletim: schemas.BoletimCreate, db: Session = Depends(database.Sessionlocal)):
    novo_boletim = models.Boletim(
        aluno_id=boletim.aluno_id,
        disciplina=boletim.disciplina,
        nota1=boletim.nota1,
        nota2=boletim.nota2,
        media=(boletim.nota1 + boletim.nota2) / 2,
    )
    db.add(novo_boletim)
    db.commit()
    db.refresh(novo_boletim)
    return novo_boletim
