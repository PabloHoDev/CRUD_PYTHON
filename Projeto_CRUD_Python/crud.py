usuarios = []
proximo_id = 1

def criar_usuario():
    global proximo_id

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    usuario = {
        'id': proximo_id,
        'nome': nome,
        'idade': idade
    }

    usuarios.append(usuario)
    proximo_id += 1

    print("✅ Usuário criado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("⚠️ Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print(f"ID: {usuario['id']} | Nome: {usuario['nome']} | Idade: {usuario['idade']}")

def atualizar_usuario():
    id_usuario = int(input("Digite o ID do usuário: "))

    for usuario in usuarios:
        if usuario['id'] == id_usuario:
            usuario['nome'] = input("Novo nome: ")
            usuario['idade'] = int(input("Nova idade: "))
            print("✏️ Usuário atualizado!")
            return

    print("❌ Usuário não encontrado.")

def deletar_usuario():
    id_usuario = int(input("Digite o ID do usuário: "))

    for usuario in usuarios:
        if usuario['id'] == id_usuario:
            usuarios.remove(usuario)
            print("🗑️ Usuário removido!")
            return

    print("❌ Usuário não encontrado.")

def menu():
    while True:
        print("\n--- MENU CRUD ---")
        print("1 - Criar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "0":
            print("👋 Saindo...")
            break
        else:
            print("⚠️ Opção inválida!")

menu()
