from model.usuario import Usuario


class UsuarioService:
    def __init__(self):
        self.usuarios = []
        self.proximo_id = 1

    def criar_usuario(self, nome, idade):
        if not nome.strip():
            print("❌ Nome não pode ser vazio.")
            return

        if idade <= 0:
            print("❌ Idade inválida.")
            return

        usuario = Usuario(self.proximo_id, nome, idade)
        self.usuarios.append(usuario)
        self.proximo_id += 1

        print("✅ Usuário criado com sucesso!")

    def listar_usuarios(self):
        if not self.usuarios:
            print("⚠️ Nenhum usuário cadastrado.")
            return

        for usuario in self.usuarios:
            print(usuario)

    def atualizar_usuario(self, id_usuario, nome, idade):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                if not nome.strip():
                    print("❌ Nome não pode ser vazio.")
                    return

                if idade <= 0:
                    print("❌ Idade inválida.")
                    return

                usuario.nome = nome
                usuario.idade = idade
                print("✏️ Usuário atualizado!")
                return

        print("❌ Usuário não encontrado.")

    def deletar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                self.usuarios.remove(usuario)
                print("🗑️ Usuário removido!")
                return

        print("❌ Usuário não encontrado.")
