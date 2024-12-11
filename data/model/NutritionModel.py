from data.model.DailyStatusModel import DailyStatusModel
from peewee import CharField, FloatField, MySQLDatabase


def get_nutrition_model(db_connection: MySQLDatabase):
    class NutritionModel(DailyStatusModel):
        id_uuid_nutrition = CharField(max_length=50)
        daily_feed_intake = FloatField()
        feed_composition = CharField(max_length=200)
        weight_gain_daily = FloatField()
        water_intake = FloatField()
        supplementation = CharField()

        class Meta:
            database = db_connection # Define o banco de dados para o modelo
            table_name = 'nutrition'  # Nome da tabela no banco de dados

    db_connection.create_tables([NutritionModel], safe=True)
    return NutritionModel