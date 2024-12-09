from peewee import Model, AutoField, CharField, DateField, MySQLDatabase, BooleanField

def get_circle_model(db_connection: MySQLDatabase):
    class CircleModel(Model):
        id = AutoField(primary_key=True)
        id_uuid = CharField(max_length=50)
        circle_name = CharField(max_length=50)
        start_date = DateField()
        end_date = DateField()
        is_ended = BooleanField(default=False)

        class Meta:
                database = db_connection # Define o banco de dados para o modelo
                table_name = 'suino'  # Nome da tabela no banco de dados

    db_connection.create_tables([CircleModel], safe=True)
    return CircleModel


