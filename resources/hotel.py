from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required



def not_empty(valor):
    if not valor or valor.strip() == "":
        raise ValueError("This field cannot be empty")
    return valor


class Hoteis(Resource):
    def get(self):
        try:
            hoteis = [hotel.json() for hotel in HotelModel.query.all()]
            return {'hoteis': hoteis}, 200
        except SQLAlchemyError:
            return {'message': 'An internal error occurred while fetching hotels'}, 500


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