from data.model import InstalationModel
from data.connection.Connection import Connection
from model.Instalation import Instalation


class InstalationService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.instalation_model = InstalationModel.get_instalation_model(
            connection.get_db()
        )

    def create(self, instalation: Instalation):
        try:
            return self.instalation_model.create(
                id_uuid=instalation.id_uuid,
                geo_location=instalation.geo_location,
                address=instalation.address,
                name=instalation.name,
                area=instalation.area,
                infra=instalation.infra,
                registration_date=instalation.registration_date,
            )

        except Exception as e:
            return None

    def get_instalation_list(self):
        try:
            result = self.instalation_model.select()

            instalation_list = []

            for instalation in result:
                instalation_list.append(
                    Instalation(
                        id=id,
                        id_uuid=instalation.id_uuid,
                        geo_location=instalation.geo_location,
                        address=instalation.address,
                        name=instalation.name,
                        area=instalation.area,
                        infra=instalation.infra,
                        registration_date=instalation.registration_date,
                    )
                )

            return instalation_list

        except Exception as e:
            return None
