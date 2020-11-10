"""Singleton Design Pattern Implementation"""

class InitiateDBConnection(object):
    def __init__(self, driver, server, database, user, password):
        self.driver = driver
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.dbconn = None

    # creats new connection
    def create_connection(self):
        return pyodbc.connect("DRIVER={};".format(self.driver) + \
                              "SERVER={};".format(self.server) + \
                              "DATABASE={};".format(self.database) + \
                              "UID={};".format(self.user) + \
                              "PWD={};".format(self.password) + \
                              "CHARSET=UTF8",
                              ansi=True)

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
            cls.connection = InitiateDBConnection().create_connection()
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

