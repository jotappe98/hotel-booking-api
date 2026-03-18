# Hotel Booking API

API REST desenvolvida com **Python e Flask** como projeto de estudo para praticar conceitos de backend como autenticação, integração com banco de dados e arquitetura REST.

O projeto simula um sistema simples de hotéis, permitindo cadastro de usuários, autenticação com JWT e gerenciamento de hotéis.

## Tecnologias utilizadas

- Python
- Flask
- Flask-RESTful
- Flask-JWT-Extended
- Flask-SQLAlchemy
- SQLite
- Postman (testes da API)

## Funcionalidades

- Cadastro de usuários
- Login com autenticação JWT
- Logout com lista negra de tokens
- CRUD completo de hotéis
- Rotas protegidas que exigem autenticação
- Filtros de busca por:
  - cidade
  - hotel
  

Para facilitar os testes, foram adicionados **hotéis mockados** no banco de dados.

## Estrutura básica da API

Alguns exemplos de endpoints disponíveis:

POST /register
POST /login
POST /logout

GET /hoteis
GET /hoteis/<id>

POST /hoteis
PUT /hoteis/<id>
DELETE /hoteis/<id>


## Como executar o projeto

# 1. Clone o repositório
git clone <url-do-repo>

# 2. Acesse a pasta do backend
cd backend

# 3. Crie e ative o ambiente virtual 

python -m venv venv

# Windows (PowerShell)
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Execute a aplicação
python main.py

Vai estar disponível em:

http://127.0.0.1:5000

Testes
Os endpoints da API foram testados utilizando Postman, permitindo validar autenticação, criação de usuários e operações de CRUD.

Sobre o projeto

Este projeto foi desenvolvido como parte dos meus estudos em backend com Python, com o objetivo de praticar conceitos importantes como:

criação de APIs REST

autenticação com JWT

integração com banco de dados

organização básica de um projeto backend

Ele serve como base para aprendizado e para futuras melhorias.