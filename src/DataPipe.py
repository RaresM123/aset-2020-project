# iterator to pipe the contents of dataset into the word embedders
import tarfile
from DBConnection import DBConnection, InitiateDBConnection
import TransformersImplementation
import DataSetParser

TAR_URL = r"dataset\CBTest.tgz"
EXTRACT_PATH = r"dataset"
TRAIN_DATA_PATH = r"dataset\CBTest\data\cbt_train.txt"

def extract_dataset(tar_url, extract_path):
	tar = tarfile.open(tar_url, 'r')
	for item in tar:
		tar.extract(item, extract_path)


def read_in_chunks(file_object, chunk_size=4096):
	"""Lazy function (generator) to read a file piece by piece.
	Default chunk size: 4k."""
	while True:
		data = file_object.read(chunk_size)
		if not data:
			break
		yield data


def process_data(text):

	return text.split("\n")[2:]


def process_train_data():

	with open(TRAIN_DATA_PATH, "r") as f:
		data = f.read()
	sentences = process_data(data)

	return sentences


def insert_sentences(sentences):
	print(sentences[0])
	sql = """INSERT INTO sentences(sentence) VALUES(%s) RETURNING id;"""
	obj = DBConnection()
	conn = obj.get_connection()
	cursor = conn.cursor()
	for sentence in sentences:
		cursor.execute(sql, (sentence,))
	conn.commit()


class iterator:
	def __init__(self):
		...
	
	def hasNext(self):
		...
	
	def getNext(self):
		...


class data:
	# the data read from disk that is supposed to be piped to the word embedder

	def __init__(self,path):
		...

	def getIterator(self):
		...
	
	def isValid(self, content):
		...


def main():
	# extract_dataset(TAR_URL, EXTRACT_PATH)
	sentences = process_train_data()
	# insert_sentences(sentences)
	stemmer = TransformersImplementation.StemmerImplementation()
	lemmer = TransformersImplementation.LemmatizerImplementationSPACY()
	stop_words = TransformersImplementation.StopWordsImplementation()

	dataSetParser = DataSetParser.DataSetParser()
	dataSetParser.SetLemmatizer(lemmer)
	dataSetParser.SetStemmer(stemmer)
	dataSetParser.SetStopWords(stop_words)

	dataSetParser.PreProcessData(sentences[0])
	print(dataSetParser.corpus)


if __name__ == '__main__':
	main()
