# iterator to pipe the contents of dataset into the word embedders

class iterator:
	def __init__(self):
		...
	
	def hasNext(self):
		...
	
	def getNext(self):
		...

class data:
	# the data read from disk that is supposed to be piped to the word embedder

	def __init__(self):
		...

	def getIterator(self):
		...
