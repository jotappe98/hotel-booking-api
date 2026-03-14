import json
import sys
import os

# adiciona a raiz do projeto ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from sql_alchemy import banco
from models.hotel import HotelModel


banco.init_app(app)

with app.app_context():

    banco.create_all()

    with open("data/hotels_seed.json", encoding="utf-8") as file:
        hoteis = json.load(file)

    for hotel in hoteis:
        novo_hotel = HotelModel(**hotel)
        banco.session.add(novo_hotel)

    banco.session.commit()

    print("Hotéis inseridos com sucesso!")
