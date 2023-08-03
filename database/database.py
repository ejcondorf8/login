
from peewee import *
from decouple import config
import datetime
database=MySQLDatabase(
    'users1',
    user='root',
    password=config('clave'),
    port=3306
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