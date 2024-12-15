from data.ServiceInterface import ServiceInterface
from data.model import NutritionModel
from data.connection.Connection import Connection
from model.Circle import Circle
from model.DailyStatus import DailyStatus
from model.Nutrition import Nutrition


class NutritionService(ServiceInterface):
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.nutrition_model = NutritionModel.get_nutrition_model(connection.get_db())

    def create(self, daily_status: DailyStatus):
        try:
            return self.nutrition_model.create(
                id_uuid=daily_status.id_uuid,
                id_uuid_suino=daily_status.id_uuid_suino,
                id_uuid_circle=daily_status.id_uuid_circle,
                weight=daily_status.weight,
                registration_date=daily_status.registration_date,
                id_uuid_nutrition=daily_status.id_uuid_nutrition,
                daily_feed_intake=daily_status.daily_feed_intake,
                feed_composition=daily_status.feed_composition,
                weight_gain_daily=daily_status.weight_gain_daily,
                water_intake=daily_status.water_intake,
                supplementation=daily_status.supplementation,
            )

        except Exception as e:
            return None

    def get_daily_status_by_circle(self, circle: Circle) -> list[DailyStatus]:
        nutrition_model_result = self.nutrition_model.select().where(
            self.nutrition_model.id_uuid_circle == circle.id_uuid
        )
        nutrition_list = []

        for nutrition in nutrition_model_result:
            nutrition_list.append(
                Nutrition(
                    id=nutrition.id,
                    id_uuid=nutrition.id_uuid,
                    id_uuid_suino=nutrition.id_uuid_suino,
                    id_uuid_circle=nutrition.id_uuid_circle,
                    weight=nutrition.weight,
                    registration_date=nutrition.registration_date,
                    id_uuid_nutrition=nutrition.id_uuid_nutrition,
                    daily_feed_intake=nutrition.daily_feed_intake,
                    feed_composition=nutrition.feed_composition,
                    weight_gain_daily=nutrition.weight_gain_daily,
                    water_intake=nutrition.water_intake,
                    supplementation=nutrition.supplementation,
                )
            )
        return nutrition_list
