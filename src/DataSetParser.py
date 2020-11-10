class Stemmer:
    corpus = []

    def Stem():
        pass

    def GetCorpus():
        pass

class Lemmatizer:
    def Lemmatize(self):
        pass

    def SetCorpus(self, corpus):
        pass

    def GetCorpus(self):
        pass

class StopWords:
    def RemoveStopWords(self):
        pass

    def SetCorpus(self, corpus):
        pass

    def GetCorpus(self):
        pass

class DataSetParser:
    corpus = []
    stemmer = None
    lemmatizer = None
    stop_words = None

    def SetStemmer(stemmer):
        pass

    def SetLemmatizer(lemmatizer):
        pass

    def SetStopWords(stop_words):
        pass

    def ReadData(self):
        pass

    def GetTrainingData(self):
        pass

    def GetTestingData(self):
        pass

class Builder:
    def getStemmer():
        pass
    
    def getLemmatizer():
        pass

    def getStopWord():
        pass

class DataSetParserBuilder(Builder):
    def getStemmer():
        pass
    
    def getLemmatizer():
        pass

    def getStopWord():
        pass

class Factory:
    __builder = None

    def setBuilder(self, builder):
        pass

    def getDataSetParser(self):
        pass
