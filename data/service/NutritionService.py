from data.model import NutritionModel
from data.connection.Connection import Connection
from model.Nutrition import Nutrition


class NutritionService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
        self.nutrition_model = NutritionModel.get_nutrition_model(connection.get_db())

    def create_status_nutrition(
        self,
        id_uuid,
        id_uuid_suino,
        id_uuid_circle,
        weight,
        registration_date,
        id_uuid_nutrition,
        daily_feed_intake,
        feed_composition,
        weight_gain_daily,
        water_intake,
        supplementation,
    ):

        try:
            result = self.nutrition_model.create(
                id_uuid=id_uuid,
                id_uuid_suino=id_uuid_suino,
                id_uuid_circle=id_uuid_circle,
                weight=weight,
                registration_date=registration_date,
                id_uuid_nutrition=id_uuid_nutrition,
                daily_feed_intake=daily_feed_intake,
                feed_composition=feed_composition,
                weight_gain_daily=weight_gain_daily,
                water_intake=water_intake,
                supplementation=supplementation,
            )
            return result

        except Exception as e:
            return None

    def get_nutriotion_status_by_circle(self, id_uuid_circle: str) -> list[Nutrition]:
        nutrition_model_result = self.nutrition_model.select().where(
            self.nutrition_model.id_uuid_circle == id_uuid_circle
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
