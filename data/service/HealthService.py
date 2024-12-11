from data.model import HealthModel
from data.connection.Connection import Connection

class HealthService():
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
            obervation
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
                obervation=obervation
            )
            return result
        
        except Exception as e:
            return None
