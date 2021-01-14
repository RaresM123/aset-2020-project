from unittest import TestCase
import unittest
import ServerConnectionAuthorizer
import multiprocessing
import time
import socket
def is_connected():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(('localhost', 5000))
	if result == 0:
		return True
	else:
		return False


class Test(TestCase):
	def test_connection(self):
		proc = multiprocessing.Process(target=ServerConnectionAuthorizer.app.run)
		proc.start()
		time.sleep(5)
		self.assertTrue(is_connected())
		proc.terminate()


if __name__ == '__main__':
	unittest.main()