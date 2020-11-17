import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import DBConnection

def TestDBConnection(unittest.TestCase):
	def test_connection(self):
		singeleton = DBConnection.DBConnection()

		obj1 = singleton.get_connection()
		obj2 = singelton.get_connection()
		self.assertFalse(obj1 != obj2) 

		connection = obj1.get_connection()
		self.assertTrue(connection is not None)