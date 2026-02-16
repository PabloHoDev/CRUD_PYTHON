from sqlalchemy.orm import Session
from repositorios import usuario_repositorio

def criar_usuario(db: Session, nome: str, email: str):
    return usuario_repositorio.criar(db, nome, email)

def listar_usuarios(db: Session):
    return usuario_repositorio.listar(db)

def buscar_usuario(db: Session, usuario_id: int):
    return usuario_repositorio.buscar_por_id(db, usuario_id)

def remover_usuario(db: Session, usuario_id: int):
    return usuario_repositorio.deletar(db, usuario_id)
