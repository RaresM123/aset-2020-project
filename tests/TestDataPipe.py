import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import DataPipe

class TestDataPipe(unittest.TestCase):
	def test_loading(self):
		data = DataPipe.data("dataset_path")
		self.assertTrue(data is not None)

		iterator = data.getIterator()
		self.assertTrue(iterator is not None)

		while(iterator.hasNext()):
			content = iterator.getNext()
			self.assertTrue(isValid(content))