from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from .database import Base

class Funcionario(Base):
    __tablename__ = "Funcionario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cargo = Column(String, unique=True, nullable=False)

class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True, index=True) 
    nome = Column(String, nullable=False)
    responsavel = Column(String, nullable=False)
    faltas = Column(Integer, default=0)

class Boletim(Base):
    __tablename__ = "Boletins"
    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    disciplina = Column(String, nullable=False)
    nota1 = Column(Integer, nullable=False)
    nota2 = Column(Integer, nullable=False)
    media = Column(Integer, nullable=True)
    aluno = relationship("Aluno")