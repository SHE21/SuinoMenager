from data.model.DailyStatusModel import DailyStatusModel
from peewee import CharField, DateField, FloatField, BooleanField, MySQLDatabase


def get_health_model(db_connection: MySQLDatabase):
    class HealthModel(DailyStatusModel):
        id_uui_health = CharField(max_length=50)
        medicine_name = CharField(max_length=100)
        medicine_type = CharField(max_length=100)
        adminitration_type = CharField(max_length=100)
        dosage: float = FloatField()
        is_treatment = BooleanField(default=False)
        diagnosis = CharField(max_length=100)
        date_start = DateField()
        date_end = DateField()
        obervation = CharField(max_length=200)

        class Meta:
            database = db_connection  # Define o banco de dados para o modelo
            table_name = "health"  # Nome da tabela no banco de dados

    db_connection.create_tables([HealthModel], safe=True)
    return HealthModel
