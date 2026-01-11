from flask import Flask, jsonify
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.user import User,UserRegister,SearchUser, UserLogin,UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DonTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
api = Api(app)
jwt= JWTManager(app)


@jwt.token_in_blocklist_loader
def check_if_token_revoked(_, jwt_payload):
    return jwt_payload["jti"] in BLACKLIST

@jwt.revoked_token_loader
def token_revogado(_, __):
    return jsonify({'message': 'You have been logged out'}), 401



api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<int:hotel_id>')

api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(SearchUser, '/usuarios')
api.add_resource(UserLogin,'/login')
api.add_resource(UserLogout,'/logout')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    with app.app_context():
        banco.create_all()


        from models.hotel import HotelModel

        if HotelModel.query.count() < 20:
            
            hoteis_iniciais = [
                HotelModel(hotel_id=1, nome='Hotel Laghetto', avaliacao=4.8, diaria=530.10, cidade='Porto Alegre'),
                HotelModel(hotel_id=2, nome='Majestic Palace Hotel', avaliacao=4.9, diaria=1531.00,
                           cidade='Florianópolis'),
                HotelModel(hotel_id=3, nome='Nooma Hotel', avaliacao=4.7, diaria=939.00, cidade='Curitiba'),
                HotelModel(hotel_id=4, nome='Hotel Fasano', avaliacao=4.8, diaria=1250.00, cidade='São Paulo'),
                HotelModel(hotel_id=5, nome='Copacabana Palace', avaliacao=4.9, diaria=1800.00, cidade='Rio de Janeiro'),
                HotelModel(hotel_id=6, nome='Ibis Styles', avaliacao=4.2, diaria=300.00, cidade='Curitiba'),
                HotelModel(hotel_id=7, nome='Sheraton Grand', avaliacao=4.7, diaria=950.00, cidade='Salvador'),
                HotelModel(hotel_id=8, nome='Pestana Rio Atlântica', avaliacao=4.6, diaria=950.00, cidade='Rio de Janeiro'),
                HotelModel(hotel_id=9, nome='Maksoud Plaza Hotel', avaliacao=4.5, diaria=760.00, cidade='São Paulo'),
                HotelModel(hotel_id=10, nome='Hotel Unique', avaliacao=4.8, diaria=1200.00, cidade='São Paulo'),
                HotelModel(hotel_id=11, nome='Grand Hyatt Rio de Janeiro', avaliacao=4.7, diaria=1250.00, cidade='Rio de Janeiro'),
                HotelModel(hotel_id=12, nome='Mercure Recife Navegantes', avaliacao=4.3, diaria=400.00, cidade='Recife'),
                HotelModel(hotel_id=13, nome='Windsor Barra Hotel', avaliacao=4.5, diaria=850.00, cidade='Rio de Janeiro'),
                HotelModel(hotel_id=14, nome='Royal Tulip Brasília', avaliacao=4.6, diaria=750.00, cidade='Brasília'),
                HotelModel(hotel_id=15, nome='Radisson Blu São Paulo', avaliacao=4.5, diaria=700.00, cidade='São Paulo'),
                HotelModel(hotel_id=16, nome='Blue Tree Premium Faria Lima', avaliacao=4.4, diaria=650.00, cidade='São Paulo'),
                HotelModel(hotel_id=17, nome='Hotel Do Canal', avaliacao=4.3, diaria=300.00, cidade='Salvador'),
                HotelModel(hotel_id=18, nome='Ritz-Carlton Rio de Janeiro', avaliacao=4.9, diaria=2500.00, cidade='Rio de Janeiro'),
                HotelModel(hotel_id=19, nome='Nacional Inn Recife', avaliacao=4.2, diaria=350.00, cidade='Recife'),
                HotelModel(hotel_id=20, nome='Hotel PortoBay Rio Internacional', avaliacao=4.6, diaria=1100.00, cidade='Rio de Janeiro')
            ]

            for hotel in hoteis_iniciais:
                banco.session.add(hotel)

            banco.session.commit()
            print("Banco populado com dados iniciais!")
    app.run(debug=True)