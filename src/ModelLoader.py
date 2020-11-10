# memento for storing the models

class Memento:
	def __init__(self):
		...

	def getState(self):
		...

class Model:
# the generative model (GPT-2)
# is the originator in memento design pattern
	def __init__(self):
		...

	def saveStateToMemento(self):
		...

	def getStateFromMemento(self):
		...

class CareTaker:
	def __init__(self):
		...

	def add(self,state):
		...

	def get(self,index):
		...