from datetime import date
from data.connection.Connection import Connection
from data.model import SuinoModel


class SuinoService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.suino_model = SuinoModel.get_suino_model(connection.get_db())

    def create_suino(self, id_tag: str, race: str, date_birth: date, gender: str, origin: str, destination: str):
        try:
            result = self.suino_model.create(
                id_tag=id_tag,
                race=race,
                date_birth=date_birth,
                gender=gender,
                origin=origin,
                destination=destination
            )
            return result

        
        except Exception as e:
            return None

    def get_suino_by_id_tag(self, id_tag: str):
        return self.suino_model.get_or_none(self.suino_model.id_tag == id_tag)

    @staticmethod
    def update_suino(suino_id, name):
        query = SuinoModel.update(name=name).where(SuinoModel.id == suino_id)
        return query.execute()

    @staticmethod
    def delete_suino(suino_id):
        query = SuinoModel.delete().where(SuinoModel.id == suino_id)
        return query.execute()
