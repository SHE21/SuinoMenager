from data.model import NutritionModel
from data.connection.Connection import Connection


class NutritionService():
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
            supplementation
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
                supplementation=supplementation
            )
            return result
        
        except Exception as e:
            return None

    """
     id_uuid_nutrition = CharField(max_length=50)
        daily_feed_intake = FloatField()
        feed_composition = CharField(max_length=200)
        weight_gain_daily = FloatField()
        water_intake = FloatField()
        supplementation = CharField()
    """

