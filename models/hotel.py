from sql_alchemy import banco

class HotelModel(banco.Model):
    __tablename__ = 'hoteis'

    hotel_id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80), nullable=False)
    cidade = banco.Column(banco.String(80), nullable=False)
    avaliacao = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))

    wifi = banco.Column(banco.Boolean, default=False)
    piscina = banco.Column(banco.Boolean, default=False)
    estacionamento = banco.Column(banco.Boolean, default=False)
    cafe_da_manha = banco.Column(banco.Boolean, default=False)
    descricao = banco.Column(banco.String(500))
    imagem_url = banco.Column(banco.String(200))

    def __init__(self, hotel_id, nome, cidade, avaliacao, diaria,
                 wifi=False, piscina=False, estacionamento=False, cafe_da_manha=False):
        self.hotel_id = hotel_id
        self.nome = nome
        self.cidade = cidade
        self.avaliacao = avaliacao
        self.diaria = diaria
        self.wifi = wifi
        self.piscina = piscina
        self.estacionamento = estacionamento
        self.cafe_da_manha = cafe_da_manha

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'cidade': self.cidade,
            'avaliacao': self.avaliacao,
            'diaria': self.diaria,
            'wifi': self.wifi,
            'piscina': self.piscina,
            'estacionamento': self.estacionamento,
            'cafe_da_manha': self.cafe_da_manha
        }

    @classmethod
    def find_hotel(cls, hotel_id):
        return cls.query.filter_by(hotel_id=hotel_id).first()

    def save_to_db(self):
        banco.session.add(self)
        banco.session.commit()

    def update_data(self, **dados):
        for key, value in dados.items():
            setattr(self, key, value)

    def delete_from_db(self):
        banco.session.delete(self)
        banco.session.commit()