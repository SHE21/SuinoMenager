from data.model import NutritionModel
from data.model import HealthModel
from data.connection.Connection import Connection


class DailyStatusService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.health_model = HealthModel.get_health_model(connection.get_db())
        self.nutrition_model = NutritionModel.get_nutrition_model(connection.get_db())
