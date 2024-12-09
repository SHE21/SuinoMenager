from datetime import date
from data.connection.Connection import Connection
from data.model import CircleModel


class CircleService():
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.circle_model = CircleModel.get_circle_model(connection.get_db())

    def create_circle(self,
            id_uuid: str,
            circle_name: str,
            start_date: date,
            end_date: date,
            observation: str,
            is_ended: bool):
        try:
            result = self.circle_model.create(
                id_uuid= id_uuid,
                circle_name=circle_name,
                start_date=start_date,
                end_date=end_date,
                observation=observation,
                is_ended=is_ended
            )
            return result

        except Exception as e:
            return None