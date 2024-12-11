from data.model import DailyStatusModel
from peewee import CharField, FloatField, MySQLDatabase


def get_nutrition_model(db_connection: MySQLDatabase):
    class NutritionModel(DailyStatusModel):
        def __init__(self):
            self.id_uuid_nutrition = CharField(max_length=50)
            self.daily_feed_intake = FloatField()
            self.feed_composition = CharField(max_length=200)
            self.weight_gain_daily = FloatField()
            self.water_intake = FloatField()
            self.supplementation = CharField()

        class Meta:
            class Meta:
                    database = db_connection # Define o banco de dados para o modelo
                    table_name = 'nutrition'  # Nome da tabela no banco de dados

    db_connection.create_tables([NutritionModel], safe=True)
    return NutritionModel