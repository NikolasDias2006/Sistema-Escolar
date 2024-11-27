from fastapi import FastAPI
from app.routers import alunos, boletins, faltas, users
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(alunos.router)
app.include_router(boletins.router)
app.include_router(faltas.router)
app.include_router(users.router)
