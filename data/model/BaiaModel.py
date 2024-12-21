from peewee import (
    Model,
    AutoField,
    CharField,
    DateField,
    FloatField,
    BooleanField,
    MySQLDatabase,
)


def get_baia_model(db_connection: MySQLDatabase):
    class BaiaModel(Model):
        id = AutoField(primary_key=True)
        id_uuid = CharField(max_length=50)
        id_uuid_instalation = CharField(max_length=50)
        label = CharField(max_length=50)
        dimen_with = FloatField()
        dimen_height = FloatField()
        type_occupation = CharField(max_length=50)
        status = BooleanField(default=True)
        registration_date = DateField()

        class Meta:
            database = db_connection  # Define o banco de dados para o modelo
            table_name = "baias"  # Nome da tabela no banco de dados

    db_connection.create_tables([BaiaModel], safe=True)
    return BaiaModel
