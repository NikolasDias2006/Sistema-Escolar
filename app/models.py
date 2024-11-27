from sqlalchemy import column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from .database import Base

class Funcionario(Base):
    __tablename__ = "Funcionario"

    id = column(Integer, primary_key=True, index=True)
    nome = column(String, nullable=False)
    cargo = column(String, unique=True, nullable=False)

class Aluno(Base):
    __tablename__ = 'Alunos'

    id = column(Integer, primary_key=True, index=True) 
    nome = column(String, nullable=False)
    responsavel = column(String, nullable=False)
    faltas = column(Integer, default=0)

class Boletim(Base):
    __tablename__ = "Boletins"
    id = column(Integer, primary_key=True, index=True)
    aluno_id = column(Integer, ForeignKey("alunos.id"), nullable=False)
    disciplina = column(String, nullable=False)
    nota1 = column(Integer, nullable=False)
    nota2 = column(Integer, nullable=False)
    media = column(Integer, nullable=True)
    aluno = relationship("Aluno")