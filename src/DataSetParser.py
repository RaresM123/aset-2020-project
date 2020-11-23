class Stemmer:
    corpus = []

    def Stem(self, text):
        pass

    def GetCorpus(self):
        return self.corpus

class Lemmatizer:
    def Lemmatize(self):
        pass

    def SetCorpus(self, corpus):
        self.corpus = corpus

    def GetCorpus(self):
        return self.corpus

class StopWords:
    def RemoveStopWords(self):
        pass

    def SetCorpus(self, corpus):
        self.corpus = corpus

    def GetCorpus(self):
        return self.corpus

class DataSetParser:
    corpus = []
    stemmer = None
    lemmatizer = None
    stop_words = None

    def SetStemmer(self, stemmer):
        self.stemmer = stemmer

    def SetLemmatizer(self, lemmatizer):
        self.lemmatizer = lemmatizer

    def SetStopWords(self, stop_words):
        self.stop_words = stop_words

    def ReadData(self):
        pass

    def GetTrainingData(self):
        pass

    def GetTestingData(self):
        pass

    def PreProcessData(self, data):
        self.stemmer.Stem(data)
        self.corpus = self.stemmer.GetCorpus()
        self.lemmatizer.SetCorpus(self.corpus)
        self.lemmatizer.Lemmatize()
        self.corpus = self.lemmatizer.GetCorpus()
        self.stop_words.SetCorpus(self.corpus)
        self.stop_words.RemoveStopWords()
        self.corpus = self.stop_words.GetCorpus()


class Builder:
    def getStemmer(self):
        pass

    def getLemmatizer(self):
        pass

    def getStopWord(self):
        pass

class DataSetParserBuilder(Builder):
    def getStemmer(self):
        pass

    def getLemmatizer(self):
        pass

    def getStopWord(self):
        pass

class Factory:
    __builder = None

    def setBuilder(self, builder):
        pass

    def getDataSetParser(self):
        pass
