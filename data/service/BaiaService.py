from data.model import BaiaModel
from data.connection.Connection import Connection
from model.Baia import Baia


class BaiaService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.baia_model = BaiaModel.get_baia_model(connection.get_db())

    def create(self, baia: Baia):
        try:
            return self.baia_model.create(
                id=baia.id,
                id_uuid=baia.id_uuid,
                id_uuid_instalation=baia.id_uuid_instalation,
                label=baia.label,
                dimen_with=baia.dimen_with,
                dimen_height=baia.dimen_height,
                type_occupation=baia.type_occupation,
                status=baia.status,
                registration_date=baia.registration_date,
            )

        except Exception as e:
            return None

    def get_baias_by_instalation(self, id_uuid_instalation: str) -> list[Baia]:
        try:
            baias_result = self.baia_model.select().where(
                self.baia_model.id_uuid_instalation == id_uuid_instalation
            )
            baia_list = []

            for baia in baias_result:
                baia_list.append(self.create_baia_object(baia))
            return baia_list

        except Exception as e:
            return baia_list

    def create_baia_object(self, baia) -> Baia:
        return Baia(
            id=baia.id,
            id_uuid=baia.id_uuid,
            id_uuid_instalation=baia.id_uuid_instalation,
            label=baia.label,
            dimen_with=baia.dimen_with,
            dimen_height=baia.dimen_height,
            type_occupation=baia.type_occupation,
            status=baia.status,
            registration_date=baia.registration_date,
        )
