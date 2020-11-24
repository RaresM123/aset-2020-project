import string

# import en_core_web_sm
import spacy
import numpy as np
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from spacy.lang.en.stop_words import STOP_WORDS

import DataSetParser
from logger.logger import LOGGER


class StemmerImplementation(DataSetParser.Stemmer):
    def Stem(self, text):
        LOGGER.debug("text before Stem processing: {}".format(text))
        tokens = word_tokenize(text)
        porter = PorterStemmer()
        # vectorizing function to able to call on list of tokens
        stem_words = np.vectorize(porter.stem)
        self.corpus = stem_words(tokens)
        LOGGER.debug("text after Stem processing: {}".format(self.corpus))


class LemmatizerImplementationNLTK(DataSetParser.Lemmatizer):
    def Lemmatize(self):

        LOGGER.debug("text before Lemm processing: {}".format(self.corpus))

        wordnet_lemmatizer = WordNetLemmatizer()
        # vectorizing function to able to call on list of tokens
        lemmatize_words = np.vectorize(wordnet_lemmatizer.lemmatize)
        self.corpus = lemmatize_words(self.corpus)
        LOGGER.debug("text after Lemm processing: {}".format(self.corpus))


class LemmatizerImplementationSPACY(DataSetParser.Lemmatizer):
    def Lemmatize(self):
        """
        Spacy lemmatized much better than nltk,
        one of the examples risen -> rise, only spacy handled that.
        """
        LOGGER.debug("text before Lemm processing: {}".format(self.corpus))

        new_corpus = []
        nlp = spacy.load("en_core_web_sm")
        for el in self.corpus:
            new_corpus+=[nlp(str(el))]
        self.corpus = new_corpus.copy()
        LOGGER.debug("text after Lemm processing: {}".format(self.corpus))


class StopWordsImplementation(DataSetParser.StopWords):
    def _remove_punct(self):
        return [t for t in self.corpus if t.doc.text not in string.punctuation]

    def _remove_stop_words(self):
        return [t.doc.text for t in self.corpus if t.doc.text not in STOP_WORDS]

    def RemoveStopWords(self):
        LOGGER.debug("text before StopWords processing: {}".format(self.corpus))

        self.corpus = self._remove_punct()
        self.corpus = self._remove_stop_words()

        LOGGER.debug("text after StopWords processing: {}".format(self.corpus))

