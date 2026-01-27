class Usuario:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Idade: {self.idade}"
