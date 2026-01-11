from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required
import sqlite3

def normalize_path_params ( cidade = None,
                            avaliacao_min = 0,
                            avaliacao_max = 5,
                            diaria_min = 0,
                            diaria_max = 10000,
                            limit = 50,
                            offset = 0, **dados):
    if cidade:
        return {
            'avaliacao_min': avaliacao_min,
            'avaliacao_max': avaliacao_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'cidade': cidade,
            'limit': limit,
            'offset': offset
        }
    return {
        'avaliacao_min': avaliacao_min,
        'avaliacao_max': avaliacao_max,
        'diaria_min': diaria_min,
        'diaria_max': diaria_max,
        'limit': limit,
        'offset': offset
    }



path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type = str)
path_params.add_argument('avaliacao_min', type = float)
path_params.add_argument('avaliacao_max', type = float)
path_params.add_argument('diaria_min', type = float)
path_params.add_argument('diaria_max', type = float)
path_params.add_argument('limit', type = int)
path_params.add_argument('offset', type = int)

def not_empty(valor):
    if not valor or valor.strip() == "":
        raise ValueError("This field cannot be empty")
    return valor


class Hoteis(Resource):
    def get(self):
        connection = sqlite3.connect('instance/banco.db')
        cursor = connection.cursor()


        dados = path_params.parse_args()
        dados_validos = {chave: dados[chave] for chave in dados if dados[chave] is not None} #Recebe apenas os parâmetros que foram passados na requisição e são válidos
        parametros = normalize_path_params(**dados_validos)

        if not parametros.get('cidade'):
            consulta = "SELECT * FROM hoteis \
            WHERE (avaliacao > ?) AND (avaliacao < ?) \
            AND (diaria > ?) AND (diaria < ?) \
            LIMIT ? OFFSET ?"
            tupla = tuple([parametros [chave] for chave in parametros]) 
            resultado = cursor.execute(consulta, tupla)
        else:
            consulta = "SELECT * FROM hoteis \
            WHERE (avaliacao > ?) AND (avaliacao < ?) \
            AND (diaria > ?) AND (diaria < ?) \
            AND (cidade = ?) \
            LIMIT ? OFFSET ?"
            tupla = tuple([parametros [chave] for chave in parametros]) 
            resultado = cursor.execute(consulta, tupla)

        rows = resultado.fetchall() 
        
        hoteis = []
        for row in resultado:
            Hoteis.append({
                'hotel_id': row[0],
                'nome': row[1],
                'avaliacao': row[2],
                'diaria': row[3],
                'cidade': row[4]
            })


        connection.close()

        
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