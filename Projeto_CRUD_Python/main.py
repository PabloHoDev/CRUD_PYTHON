from service.usuario_service import UsuarioService


def menu():
    service = UsuarioService()

    while True:
        print("\n--- MENU CRUD ---")
        print("1 - Criar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("0 - Sair")

        opcao = input("Escolha: ")

        try:
            if opcao == "1":
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                service.criar_usuario(nome, idade)

            elif opcao == "2":
                service.listar_usuarios()

            elif opcao == "3":
                id_usuario = int(input("ID: "))
                nome = input("Novo nome: ")
                idade = int(input("Nova idade: "))
                service.atualizar_usuario(id_usuario, nome, idade)

            elif opcao == "4":
                id_usuario = int(input("ID: "))
                service.deletar_usuario(id_usuario)

            elif opcao == "0":
                print("👋 Saindo...")
                break

            else:
                print("⚠️ Opção inválida!")

        except ValueError:
            print("❌ Entrada inválida. Use números quando solicitado.")


menu()
