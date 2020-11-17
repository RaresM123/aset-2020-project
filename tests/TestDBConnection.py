import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import DBConnection

def TestDBConnection(unittest.TestCase):
	def test_connection(self):
		with DBConnection.InitiateDBConnection() as singleton:
			# enter -  creates a new connection

			databaseManager = DBConnection.DBConnection(DRIVER, SERVER, DATABASE, UID, PWD)

			connection = databaseManager.get_connection(singleton)
			self.assertTrue(connection is not None)

			obj1 = databaseManager.get_connection(singleton)
			obj2 = databaseManager.get_connection(singleton)
			self.assertTrue(obj1 == obj2)

			obj1 = databaseManager.get_connection(singleton)
			obj2 = databaseManager.get_connection(singleton,True) # force reinitialization of the db connection
			obj3 = databaseManager.get_connection(singleton)

			self.assertTrue(obj1 != obj2 and obj2 == obj3)

			# exit - the connection is closed