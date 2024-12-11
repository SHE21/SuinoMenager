from peewee import Model, AutoField, CharField, DateField, FloatField

class DailyStatus(Model):
    def __init__(self):
        id = AutoField(primary_key=True)
        id_uuid = CharField(max_length=50)
        id_uuid_suino = CharField(max_length=50)
        id_uuid_circle = CharField(max_length=50)
        weight = FloatField()
        registration_date = DateField()

    class Meta:
        abstract = True