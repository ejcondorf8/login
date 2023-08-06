
from peewee import *
from decouple import config
import datetime
from controlador import log
class Conexion:
    USER='fl0user'
    PASSWORD='clave1'
    PORT=5432
    HOST='ep-late-haze-49514607.ap-southeast-1.aws.neon.tech'
    DB='users1'
    @classmethod
    def obtenerConexion(cls):
        database=PostgresqlDatabase(
            cls.DB,
            user=cls.USER,
            password=config(cls.PASSWORD),
            port=cls.PORT,
            host=cls.HOST
        )
        log.debug('CONEXION EXITOSA')
        return database



class User(Model):
    email=TextField()
    password=TextField()
    CREATE_TIME=DateField(default=datetime.datetime.now)


    class Meta:
        database=Conexion.obtenerConexion()
        db_table='users'


prueba=Conexion.obtenerConexion().create_tables([User])