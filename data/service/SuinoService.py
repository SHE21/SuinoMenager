from datetime import date
import uuid
from data.connection.Connection import Connection
from data.model import SuinoModel
from model.Suino import Suino


class SuinoService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.suino_model = SuinoModel.get_suino_model(connection.get_db())

    def create_suino(self, id_tag: str, id_uuid: str, race: str, date_birth: date, gender: str, origin: str):
        try:
            result = self.suino_model.create(
                id_tag=id_tag,
                id_uuid=id_uuid,
                race=race,
                date_birth=date_birth,
                gender=gender,
                origin=origin
            )
            return result

        
        except Exception as e:
            return None

    def get_suino_by_uuid(self, id_uuid: str) -> Suino:
        suino_result = self.suino_model.get(self.suino_model.id_uuid == id_uuid)
        return Suino(
            id=suino_result.id,
            id_uuid=suino_result.id_uuid,
            id_tag=suino_result.id_tag,
            race=suino_result.race,
            date_birth=suino_result.date_birth,
            gender=suino_result.gender,
            origin=suino_result.origin
        )
    
    def get_suinos(self) -> list[Suino]:
        suino_list_db = self.suino_model.select()
        suino_list_result = []

        for suino in suino_list_db:
            suino_list_result.append(
                Suino(
                    suino.id,
                    suino.id_uuid,
                    suino.id_tag,
                    suino.race,
                    suino.date_birth,
                    suino.gender,
                    suino.origin
                )
            )
        return suino_list_result
    
    @staticmethod
    def update_suino(suino_id, name):
        query = SuinoModel.update(name=name).where(SuinoModel.id == suino_id)
        return query.execute()

    @staticmethod
    def delete_suino(suino_id):
        query = SuinoModel.delete().where(SuinoModel.id == suino_id)
        return query.execute()
