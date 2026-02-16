from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from configuracoes.banco import SessaoLocal
from servicos import usuario_servico

roteador = APIRouter()

def obter_db():
    db = SessaoLocal()
    try:
        yield db
    finally:
        db.close()

@roteador.post("/usuarios")
def criar(nome: str, email: str, db: Session = Depends(obter_db)):
    return usuario_servico.criar_usuario(db, nome, email)

@roteador.get("/usuarios")
def listar(db: Session = Depends(obter_db)):
    return usuario_servico.listar_usuarios(db)

@roteador.get("/usuarios/{usuario_id}")
def buscar(usuario_id: int, db: Session = Depends(obter_db)):
    return usuario_servico.buscar_usuario(db, usuario_id)

@roteador.delete("/usuarios/{usuario_id}")
def deletar(usuario_id: int, db: Session = Depends(obter_db)):
    return usuario_servico.remover_usuario(db, usuario_id)
