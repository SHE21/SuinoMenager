from data.connection.Connection import Connection
from data.service.HealthService import HealthService
from data.service.NutritionService import NutritionService
from model.Circle import Circle
from model.DailyStatus import DailyStatus


class DailyStatusService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.health_service = HealthService(connection)
        self.nutrition_servcie = NutritionService(connection)

    def get_daily_status(self, circle: Circle):
        health_reult = self.health_service.get_health_status_by_circle(circle.id_uuid)
        nutrition_result = self.nutrition_servcie.get_daily_status_by_circle(
            circle=circle
        )

        daily_status_list: list[DailyStatus] = []
        daily_status_list.extend(health_reult)
        daily_status_list.extend(nutrition_result)
        return daily_status_list
