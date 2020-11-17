import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import ModelLoader



def TestModelLoader(unittest.TestCase):
	def test_loading(self):
		model = ModelLoader.Model()
		model.getStateFromMemento()

		self.assertTrue(model is not None)
		self.assertTrue(model.saveStateToMemento())
