from sqlalchemy.orm import Session
from modelos.usuario import Usuario

def criar(db: Session, nome: str, email: str):
    novo_usuario = Usuario(nome=nome, email=email)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def listar(db: Session):
    return db.query(Usuario).all()

def buscar_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def deletar(db: Session, usuario_id: int):
    usuario = buscar_por_id(db, usuario_id)
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario