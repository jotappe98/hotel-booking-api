from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required

path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str, location='args')
path_params.add_argument('avaliacao_min', type=float, location='args')
path_params.add_argument('avaliacao_max', type=float, location='args')
path_params.add_argument('diaria_min', type=float, location='args')
path_params.add_argument('diaria_max', type=float, location='args')
path_params.add_argument('limit', type=int, location='args')
path_params.add_argument('offset', type=int, location='args')
path_params.add_argument('wifi', type=bool, location='args')
path_params.add_argument('piscina', type=bool, location='args')
path_params.add_argument('estacionamento', type=bool, location='args')
path_params.add_argument('cafe_da_manha', type=bool, location='args')


def not_empty(valor):
    if not valor or valor.strip() == "":
        raise ValueError("This field cannot be empty")
    return valor


class Hoteis(Resource):
    
    def get(self):
        
        dados = path_params.parse_args()

        query = HotelModel.query

        if dados.get('cidade'):
            query = query.filter(HotelModel.cidade == dados['cidade'])

        if dados.get('avaliacao_min'):
            query = query.filter(HotelModel.avaliacao >= dados['avaliacao_min'])

        if dados.get('avaliacao_max'):
            query = query.filter(HotelModel.avaliacao <= dados['avaliacao_max'])

        if dados.get('diaria_min'):
            query = query.filter(HotelModel.diaria >= dados['diaria_min'])

        if dados.get('diaria_max'):
            query = query.filter(HotelModel.diaria <= dados['diaria_max'])

        if dados.get('wifi') is not None:
            query = query.filter(HotelModel.wifi == dados['wifi'])

        if dados.get('piscina') is not None:
            query = query.filter(HotelModel.piscina == dados['piscina'])

        if dados.get('estacionamento') is not None:
            query = query.filter(HotelModel.estacionamento == dados['estacionamento'])

        if dados.get('cafe_da_manha') is not None:
            query = query.filter(HotelModel.cafe_da_manha == dados['cafe_da_manha'])

        hoteis = [hotel.json() for hotel in query.all()]

        return {'hoteis': hoteis}, 200
   
   

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=not_empty, required=True, help="This field 'nome' cannot be left blank")
    argumentos.add_argument('avaliacao', type=float, required=True, help="This field 'avaliacao' cannot be left blank")
    argumentos.add_argument('diaria', type=float, required=True, help="This field 'diaria' cannot be left blank")
    argumentos.add_argument('cidade', type=not_empty, required=True, help="This field 'cidade' cannot be left blank")

    @staticmethod
    def find_hotel(hotel_id):
        try:
            return HotelModel.query.filter_by(hotel_id=hotel_id).first()
        except SQLAlchemyError:
            return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel.json(), 200
        return {'message': 'Hotel not found'}, 404

    @jwt_required() #Garante que esteja autenticado para usar o método
    def post(self, hotel_id):
        if Hotel.find_hotel(hotel_id):
            return {'message': f'Hotel id {hotel_id} already exists'}, 400

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)

        try:
            hotel.save_to_db()
        except SQLAlchemyError:
            return {'message': 'An internal error occurred trying to save hotel'}, 500

        return hotel.json(), 201
        

    @jwt_required()
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_encontrado = Hotel.find_hotel(hotel_id)

        if hotel_encontrado:
            hotel_encontrado.update_data(**dados)
            try:
                hotel_encontrado.save_to_db()
            except SQLAlchemyError:
                return {'message': 'An internal error occurred trying to update hotel'}, 500
            return hotel_encontrado.json(), 200

        novo_hotel = HotelModel(hotel_id, **dados)
        try:
            novo_hotel.save_to_db()
        except SQLAlchemyError:
            return {'message': 'An internal error occurred trying to save hotel'}, 500
        return novo_hotel.json(), 201

    @jwt_required()
    def delete(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_from_db()
            except SQLAlchemyError:
                return {'message': 'An internal error occurred trying to delete hotel'}, 500
            return {'message': 'Hotel deleted'}, 200
        return {'message': 'Hotel not found'}, 404