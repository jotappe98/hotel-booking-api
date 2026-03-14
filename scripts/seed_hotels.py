import json
from main import app
from sql_alchemy import banco
from models.hotel import HotelModel


with app.app_context():

    with open("data/hotels_seed.json", encoding="utf-8") as file:
        hoteis = json.load(file)

    for hotel in hoteis:
        novo_hotel = HotelModel(**hotel)
        banco.session.add(novo_hotel)

    banco.session.commit()

    print("Hotéis inseridos com sucesso!")
