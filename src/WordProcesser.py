#adapter for word processing


#target for lemmatizer
class LemmatizerInterface:

    def __init__(self):
        pass

#target for stemmer
class StemmerInterface:

    def __init__(self):
        pass


#target for stop words
class stopWordsInterface:

    def __init__(self):
        pass


class concreteLemmatizer:

    def __init__(self):
        pass


class concreteStemmer:

    def __init__(self):
        pass


class concreteStopWords:

    def __init__(self):
        pass


class AdapterLemmatizer(LemmatizerInterface):

    def __init__(self):
        super().__init__()


class AdapterStemmer(StemmerInterface):

    def __init__(self):
        super().__init__()


class AdapterStopWords(stopWordsInterface):

    def __init__(self):
        super().__init__()



