from flask import Flask, jsonify
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.user import User, UserRegister, SearchUser, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DonTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

api = Api(app)
jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def check_if_token_revoked(_, jwt_payload):
    return jwt_payload["jti"] in BLACKLIST


@jwt.revoked_token_loader
def token_revogado(_, __):
    return jsonify({'message': 'You have been logged out'}), 401


# ROTAS DA API
api.add_resource(Hoteis, '/hoteis', '/hoteis/')
api.add_resource(Hotel, '/hoteis/<int:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(SearchUser, '/usuarios')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')


if __name__ == '__main__':
    from sql_alchemy import banco

    banco.init_app(app)

    with app.app_context():
        banco.create_all()

    app.run(debug=True)
