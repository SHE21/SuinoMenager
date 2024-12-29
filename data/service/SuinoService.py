from datetime import date
from data.connection.Connection import Connection
from data.model import SuinoModel
from model.Circle import Circle
from model.Suino import Suino


class SuinoService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.suino_model = SuinoModel.get_suino_model(connection.get_db())

    def create_suino(
        self,
        id_tag: str,
        id_uuid: str,
        id_uuid_circle: str,
        race: str,
        date_birth: date,
        gender: str,
        origin: str,
        is_active: bool,
        registration_date: date,
    ):
        try:
            result = self.suino_model.create(
                id_tag=id_tag,
                id_uuid=id_uuid,
                id_uuid_circle=id_uuid_circle,
                race=race,
                date_birth=date_birth,
                gender=gender,
                origin=origin,
                is_active=is_active,
                registration_date=registration_date,
            )
            return result

        except Exception as e:
            return None

    def get_suino_by_uuid(self, circle: Circle) -> list[Suino]:
        suino_result = self.suino_model.select().where(
            self.suino_model.id_uuid_circle == circle.id_uuid
        )

        suino_list = []
        for suino in suino_result:
            suino_list.append(
                Suino(
                    id=suino.id,
                    id_uuid=suino.id_uuid,
                    id_uuid_circle=suino.id_uuid_circle,
                    id_tag=suino.id_tag,
                    race=suino.race,
                    date_birth=suino.date_birth,
                    gender=suino.gender,
                    origin=suino.origin,
                    is_active=suino.is_active,
                    registration_date=suino.registration_date,
                )
            )
        return suino_list

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
                    suino.origin,
                    suino.registration_date,
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
