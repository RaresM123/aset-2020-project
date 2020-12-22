import nltk
import language_check
from pattern.text.en import singularize

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
        nltk.download('words')
        words = set(nltk.corpus.words.words())

        sentence = " ".join(w for w in nltk.wordpunct_tokenize(sentence)
                            if singularize(w).lower() in words or not w.isalpha())
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

    sentence = Monitor_SpellingCheck(sentence)
    sentence = Monitor_DeleteNonEnglishWords(sentence)

    return sentence

    # / IMPLEMENTATION #


def monitor_parameters(param_dict):

    """
    This function verify each parameter to have the values in acceptable and correct ranges
    :param param_dict: dictionary of parameters
    :return: a new formed dictionary of paramters after monitorizing
    """
    new_param_dict = {}
    new_param_dict["model_name"] = "beta2" if param_dict["model_name"] is None else param_dict["model_name"]
    new_param_dict["seed"] = None if (param_dict["seed"] > 100 or param_dict["seed"] < -100) else param_dict["seed"]
    new_param_dict["nsamples"] = 1 if (param_dict["nsamples"] < 0 or param_dict["nsamples"] is None) else param_dict["nsamples"]
    new_param_dict["batch_size"] = 1 if (param_dict["batch_size"] < 0 or param_dict["batch_size"] is None) else param_dict["batch_size"]
    new_param_dict["length"] = None if param_dict["length"] < 0 else param_dict["length"]
    new_param_dict["temperature"] = 1 if (param_dict["temperature"] < 0 or param_dict["temperature"] is None) else param_dict["temperature"]
    new_param_dict["top_k"] = 40 if (param_dict["top_k"] < 0 or param_dict["top_k"] is None) else param_dict["top_k"]
    new_param_dict["top_p"] = 0.0 if (param_dict["top_p"] < 0 or param_dict["top_p"] is None) else param_dict["top_p"]
    new_param_dict["raw_sentence"] = param_dict["raw_sentence"]
    return new_param_dict
