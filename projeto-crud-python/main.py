from fastapi import FastAPI
from configuracoes.banco import Base, engine
from rotas import usuario_rotas

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario_rotas.roteador)
