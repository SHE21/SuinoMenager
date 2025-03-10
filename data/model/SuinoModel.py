from peewee import Model, AutoField, CharField, DateField, MySQLDatabase, BooleanField


def get_suino_model(db_connection: MySQLDatabase):
    class SuinoModel(Model):
        id = AutoField(primary_key=True)
        id_uuid = CharField(max_length=50)
        id_uuid_circle = CharField(max_length=50)
        id_tag = CharField(max_length=50)
        race = CharField(max_length=50)
        date_birth = DateField()
        gender = CharField(max_length=10)
        origin = CharField(max_length=100)
        is_active = BooleanField(default=True)
        registration_date = DateField()

        class Meta:
            database = db_connection  # Define o banco de dados para o modelo
            table_name = "suinos"  # Nome da tabela no banco de dados

    db_connection.create_tables([SuinoModel], safe=True)
    return SuinoModel
