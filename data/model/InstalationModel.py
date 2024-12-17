from peewee import (
    Model,
    AutoField,
    CharField,
    DateField,
    MySQLDatabase,
    FloatField,
)


def get_instalation_model(db_connection: MySQLDatabase):
    class InstalationModel(Model):
        id = AutoField(primary_key=True)
        id_uuid = CharField(max_length=50)
        geo_location = CharField(max_length=50)
        address = CharField(max_length=100)
        name = CharField(max_length=100)
        area = FloatField()
        infra = CharField(max_length=200)
        registration_date = DateField()

        class Meta:
            database = db_connection  # Define o banco de dados para o modelo
            table_name = "instalation"  # Nome da tabela no banco de dados

    db_connection.create_tables([InstalationModel], safe=True)
    return InstalationModel
