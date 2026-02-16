📌 Projeto CRUD em Python – (AINDA SOFRERÁ ATUALIZAÇÕES)

📖 Descrição

Este projeto é uma API REST de CRUD (Create, Read, Update e Delete) desenvolvida em Python utilizando:

FastAPI

SQLAlchemy

SQLite

O projeto foi estruturado seguindo boas práticas de organização de código, separando responsabilidades em:

🗂 Estrutura do Projeto

Projeto_CRUD_Python/
│
├── modelos/
│   └── usuario.py
│
├── repositorios/
│   └── usuario_repositorio.py
│
├── servicos/
│   └── usuario_servico.py
│
├── rotas/
│   └── usuario_rotas.py
│
├── configuracoes/
│   └── banco.py
│
├── main.py
├── requirements.txt
└── README.md

🧠 Arquitetura
📁 modelos

Define as tabelas do banco de dados.

📁 repositorios

Responsável pelo acesso direto ao banco de dados.

📁 servicos

Contém as regras de negócio.

📁 rotas

Define os endpoints da API.

📁 configuracoes

Configuração da conexão com o banco de dados.

🚀 Tecnologias Utilizadas

Python 3.10+

FastAPI

SQLAlchemy

SQLite

Uvicorn

🎯 Objetivo do Projeto

Este projeto tem como objetivo:

Aplicar boas práticas de organização

Separar responsabilidades

Criar base escalável

Servir como base para evolução para níveis mais avançados

🚀 Próximas Melhorias (Planejamento)

 Adicionar atualização (PUT)

 Implementar validação com Pydantic

 Adicionar autenticação JWT

 Implementar paginação

 Criar testes automatizados

 Dockerizar aplicação

 👨‍💻 Autor

Projeto desenvolvido para fins de estudo e evolução em arquitetura de APIs REST com Python.