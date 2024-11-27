from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
router = APIRouter()

@router.put("/alunos/{aluno_id}/faltas/")
def registrar_falta(aluno_id: int, quantidade: int, db: Session = Depends(database.Sessionlocal)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    aluno.faltas += quantidade
    db.commit()
    if aluno.faltas > 20:
        pass
    return aluno
