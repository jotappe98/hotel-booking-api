from sql_alchemy import banco
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(banco.Model):
    __tablename__ = 'usuarios'

    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40), unique=True, nullable=False)
    senha = banco.Column(banco.String(200), nullable=False)  # hash mais longo

    def __init__(self, login, senha):
        self.login = login
        self.senha = generate_password_hash(senha) #converte a senha em um hash seguro antes de salvar no banco.

    def verify_password(self, senha_plain):
        return check_password_hash(self.senha, senha_plain) #compara a senha digitada com o hash armazenado sem revelar a senha real.

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login
        }

    @classmethod
    def find_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()

    @classmethod
    def find_by_login(cls, login):
        return cls.query.filter_by(login=login).first()

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()

    @classmethod #Buscar todos os usuários
    def find_all_users(cls):
        return cls.query.all()