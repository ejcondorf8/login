
from peewee import *
from decouple import config
import datetime
database=PostgresqlDatabase(
    'users1',
    user='fl0user',
    password=config('clave1'),
    port=5432,
    host='ep-late-haze-49514607.ap-southeast-1.aws.neon.tech'
)
print(database)


class User(Model):
    email=TextField()
    password=TextField()
    CREATE_TIME=DateField(default=datetime.datetime.now)


    class Meta:
        database=database
        db_table='users'


database.create_tables([User])