import pyodbc
import psycopg2
from logger.logger import LOGGER

"""Singleton Design Pattern Implementation"""


class InitiateDBConnection(object):
    def __init__(self, database, host, port, user, password):
        self.database = database
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbconn = None

    # creats new connection
    def create_connection(self):
        try:
            return psycopg2.connect(user = self.user,
                                password = self.password,
                              database = self.database,
                              host = self.host, port = self.port)
        except(Exception, psycopg2.Error) as error:

            LOGGER.error("Error while connecting to PostgreSQL with error: {}".format(str(error)))
            return None

    # For explicitly opening database connection
    def __enter__(self):
        self.dbconn = self.create_connection()
        return self.dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbconn.close()


class DBConnection(object):
    connection = None

    @classmethod
    def get_connection(cls, new=False):
        """Call InitiateDBConnection class to initiate a new Singleton database connection"""
        if new or not cls.connection:
            cls.connection = InitiateDBConnection(database='aset2020',host = '127.0.0.1',port='5432', user='postgres', password='Rares1234_!').create_connection()
        return cls.connection

    @classmethod
    def execute_query(cls, query):
        """execute query on the singleton db connection"""
        connection = cls.get_connection()
        try:
            cursor = connection.cursor()
        except pyodbc.ProgrammingError:
            connection = cls.get_connection(new=True)  # Create a new connection
            cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

