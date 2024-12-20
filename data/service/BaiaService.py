from data.model import BaiaModel
from data.connection.Connection import Connection


class BaiaService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.baia_model = BaiaModel.get_baia_model(connection.get_db())
        
    def create(self, baia: Baia):
