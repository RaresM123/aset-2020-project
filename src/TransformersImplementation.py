import string

import en_core_web_sm
import numpy as np
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

import DataSetParser

class StemmerImplementation(DataSetParser.Stemmer):
    def Stem(self, text):
        tokens = word_tokenize(text)
        porter = PorterStemmer()
        # vectorizing function to able to call on list of tokens
        stem_words = np.vectorize(porter.stem)
        self.corpus = stem_words(tokens)

class LemmatizerImplementationNLTK(DataSetParser.Lemmatizer):
    def Lemmatize(self):
        wordnet_lemmatizer = WordNetLemmatizer()
        # vectorizing function to able to call on list of tokens
        lemmatize_words = np.vectorize(wordnet_lemmatizer.lemmatize)
        self.corpus = lemmatize_words(self.corpus)

class LemmatizerImplementationSPACY(DataSetParser.Lemmatizer):
    def Lemmatize(self):
        """
        Spacy lemmatized much better than nltk,
        one of the examples risen -> rise, only spacy handled that.
        """
        nlp = en_core_web_sm.load()
        lemmatize_words = np.vectorize(nlp)
        self.corpus = [t.lemma_ for t in lemmatize_words(self.corpus)]

class StopWordsImplementation(DataSetParser.StopWords):
    def _remove_punct(self, doc):
        return [t for t in doc if t.text not in string.punctuation]

    def _remove_stop_words(self, doc):
        return [t for t in doc if not t.is_stop]

    def RemoveStopWords(self):
        nlp = en_core_web_sm.load()
        doc = np.vectorize(nlp)
        self.corpus = self._remove_punct(doc)
        self.corpus = self._remove_stop_words(doc)


