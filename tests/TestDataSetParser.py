import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import DataSetParser

class TestDataSetParser(unittest.TestCase):
	def test_parser(self):
		builder = DataSetParser.Builder()
		factory = DataSetParser.Factory()
		factory.setBuilder(builder)

		parser = factory.getParser()

		self.assertTrue(parser is not None)

		parser.ReadData("dataset_path")
		training_data = parser.GetTrainingData()
		testing_data = parser.GetTestingData()

		self.assertTrue(isValid(training_data))
		self.assertTrue(isValid(testing_data))