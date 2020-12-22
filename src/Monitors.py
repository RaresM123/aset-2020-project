import nltk
import language_check

def Monitor_InputSentence(sentence):
    """
    Monitor Rules:
        1. Sentence null -> return the test sentence
        2. If there are words from another language -> delete those words
        3. If there are spelling mistakes -> rewrite the sentence
    """

    # GLOBALS #

    def Monitor_DeleteNonEnglishWords(sentence):
        # We will clean the sentence from non-english words
        words = set(nltk.corpus.words.words())
        sentence = " ".join(w for w in nltk.wordpunct_tokenize(sentence)
                            if w.lower() in words or not w.isalpha())
        return sentence

    def Monitor_SpellingCheck(sentence):
        # Spelling check : ex. A sentence with a error fort he Galaxy.
        # Correct : A sentence with an error for the Galaxy.
        tool = language_check.LanguageTool('en-US')
        matches = tool.check(sentence)
        sentence = language_check.correct(sentence, matches)
        return sentence

    TEST_SENTENCE = "I like eating bugs"

    # / GLOBALS #

    # IMPLEMENTATION #
    if sentence == None or sentence == "":
        return TEST_SENTENCE

    sentence = Monitor_DeleteNonEnglishWords(sentence)
    sentence = Monitor_SpellingCheck(sentence)
    return sentence

    # / IMPLEMENTATION #
