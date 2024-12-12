from data.connection.Connection import Connection
from data.service.HealthService import HealthService
from data.service.NutritionService import NutritionService
from model.DailyStatus import DailyStatus


class DailyStatusService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.health_service = HealthService(connection)
        self.nutrition_servcie = NutritionService(connection)

    def get_daily_status(self, id_uuid_circle: str):
        health_reult = self.health_service.get_health_status_by_circle(id_uuid_circle)
        nutrition_result = self.nutrition_servcie.get_nutrition_status_by_circle(
            id_uuid_circle
        )

        daily_status_list: list[DailyStatus] = []
        daily_status_list.extend(health_reult)
        daily_status_list.extend(nutrition_result)
        return daily_status_list
