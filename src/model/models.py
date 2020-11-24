from peewee import *

psql_db = PostgresqlDatabase('aset2020', user='postgres', password='Rares1234_!')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db


class Sentences(BaseModel):
    sentence = TextField()


psql_db.connect()
psql_db.create_tables([Sentences])
