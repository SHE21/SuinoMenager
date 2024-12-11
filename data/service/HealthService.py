from data.model import HealthModel
from data.connection.Connection import Connection
from model.Health import Health


class HealthService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.health_model = HealthModel.get_health_model(connection.get_db())

    def create_status_health(
        self,
        id_uuid,
        id_uuid_suino,
        id_uuid_circle,
        weight,
        registration_date,
        id_uui_health,
        medicine_name,
        medicine_type,
        adminitration_type,
        dosage,
        is_treatment,
        diagnosis,
        date_start,
        date_end,
        obervation,
    ):

        try:
            result = self.health_model.create(
                id_uuid=id_uuid,
                id_uuid_suino=id_uuid_suino,
                id_uuid_circle=id_uuid_circle,
                weight=weight,
                registration_date=registration_date,
                id_uui_health=id_uui_health,
                medicine_name=medicine_name,
                medicine_type=medicine_type,
                adminitration_type=adminitration_type,
                dosage=dosage,
                is_treatment=is_treatment,
                diagnosis=diagnosis,
                date_start=date_start,
                date_end=date_end,
                obervation=obervation,
            )
            return result

        except Exception as e:
            print(e)
            return None

    def get_health_status_by_circle(self, id_uuid_circle: str) -> list[Health]:
        health_model_result = self.health_model.select().where(
            self.health_model.id_uuid_circle == id_uuid_circle
        )
        health_list = []

        for health in health_model_result:
            health_list.append(
                Health(
                    id=health.id,
                    id_uuid=health.id_uuid,
                    id_uuid_suino=health.id_uuid_suino,
                    id_uuid_circle=health.id_uuid_circle,
                    weight=health.weight,
                    registration_date=health.registration_date,
                    id_uui_health=health.id_uui_health,
                    medicine_name=health.medicine_name,
                    medicine_type=health.medicine_type,
                    adminitration_type=health.adminitration_type,
                    dosage=health.dosage,
                    is_treatment=health.is_treatment,
                    diagnosis=health.diagnosis,
                    date_start=health.date_start,
                    date_end=health.date_end,
                    obervation=health.obervation,
                )
            )
        return health_list
