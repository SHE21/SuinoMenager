from datetime import date
from data.connection.Connection import Connection
from data.model import CircleModel
from data.model import HealthModel
from model.Circle import Circle


class CircleService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.circle_model = CircleModel.get_circle_model(connection.get_db())
        self.health_model = HealthModel.get_health_model(connection.get_db())

    def create_circle(
        self,
        id_uuid: str,
        id_uuid_suino: str,
        circle_name: str,
        start_date: date,
        end_date: date,
        observation: str,
        is_ended: bool,
        registration_date: date,
    ):
        try:
            result = self.circle_model.create(
                id_uuid=id_uuid,
                id_uuid_suino=id_uuid_suino,
                circle_name=circle_name,
                start_date=start_date,
                end_date=end_date,
                observation=observation,
                is_ended=is_ended,
                registration_date=registration_date,
            )
            return result

        except Exception as e:
            return None

    def get_circle_by_uuid(self, uuid: str) -> Circle:
        circle_result = self.circle_model.get(self.circle_model.id_uuid == uuid)
        return Circle(
            id=circle_result.id,
            id_uuid=circle_result.uuid,
            circle_name=circle_result.circle_name,
            start_date=circle_result.date_start,
            end_date=circle_result.end_date,
            observation=circle_result.observation,
            daily_status=[],
            is_ended=circle_result.is_ended,
            registration_date=circle_result.registration_date,
        )

    def get_circles_by_uuid_suino(self, id_uuid_suino: str) -> list[Circle]:
        circle_result = self.circle_model.select().where(
            self.circle_model.id_uuid_suino == id_uuid_suino
        )
        circle_list = []

        for circle in circle_result:
            circle_list.append(
                Circle(
                    id=circle.id,
                    id_uuid=circle.id_uuid,
                    id_uuid_suino=circle.id_uuid_suino,
                    circle_name=circle.circle_name,
                    start_date=circle.start_date,
                    end_date=circle.end_date,
                    observation=circle.observation,
                    daily_status=[],
                    is_ended=circle.is_ended,
                    registration_date=circle.registration_date,
                )
            )
        return circle_list
