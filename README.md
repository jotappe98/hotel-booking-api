API REST desenvolvida com **Python** e **Flask** como projeto de estudo, com o objetivo de praticar conceitos de backend como autenticação, integração com banco de dados e arquitetura RESTful.

## Tecnologias

- Python
- Flask
- Flask-RESTful
- Flask-JWT-Extended
- Flask-SQLAlchemy
- SQLite

## Funcionalidades

- Registro e autenticação de usuários (JWT)
- CRUD de hotéis (Criar, Ler, Atualizar, Deletar)
- Rotas protegidas utilizando JWT
- Lista negra de tokens (logout)
- **Hotéis mock adicionados para testar filtros avançados** (por cidade, valor da diária e avaliação)

## Como rodar o projeto

```bash
# clone o repositório
git clone https://github.com/your-username/hotel-booking-api.git

# entre na pasta do projeto
cd hotel-booking-api

# crie um ambiente virtual
python -m venv venv

# ative o venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# instale as dependências
pip install -r requirements.txt

# rode a aplicação
python main.py

## Sobre o projeto
Este projeto foi desenvolvido como parte de um curso prático de APIs REST com Python e Flask, com o objetivo de consolidar conceitos como autenticação, CRUD, banco de dados e boas práticas de backend. O código foi implementado e testado por mim usando Postman, servindo como base para estudos e futuras melhorias.
```
