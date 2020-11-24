"""Decorator implemented for Authorizing the Requests made to Server"""
from flask import Flask, jsonify, request
import requests

import DataSetParser
import TransformersImplementation

app = Flask(__name__)

AUTHORIZATION_TOKEN_EXPECTED = 'xy124zjw3'


def authorize(_function):
    """These will be used for making a simple form of authentication when requests are made to server"""
    def wrapper(*args, **kwargs):
        authentication_token = request.headers.get('AuthorizationToken')
        if authentication_token == AUTHORIZATION_TOKEN_EXPECTED:
            return _function(*args, **kwargs)
        else:
            return 'Wrong Token', requests.status_codes.codes['unauthorized']
    return wrapper


def processSentence(sentence):

    stemmer = TransformersImplementation.StemmerImplementation()
    lemmer = TransformersImplementation.LemmatizerImplementationSPACY()
    stop_words = TransformersImplementation.StopWordsImplementation()

    dataSetParser = DataSetParser.DataSetParser()
    dataSetParser.SetLemmatizer(lemmer)
    dataSetParser.SetStemmer(stemmer)
    dataSetParser.SetStopWords(stop_words)

    dataSetParser.PreProcessData(sentence)
    return dataSetParser.corpus


"""this is where the authorization is made"""


@app.route('/check_statement', methods=['POST'])
@authorize
def SendStatement():

    response = {
        'success': True,
        'processedSentence': None
    }

    try:
        body = request.get_json() or dict()
    except:
        body = dict()
    sentence = body.get('sentence')
    if not sentence:
        response['success'] = False
        return jsonify(response)

    try:
        processed_sentence = processSentence(sentence)
    except Exception as e:
        response['success'] = False
        return jsonify(response)

    response['processedSentence'] = processed_sentence
    return jsonify(response)


if __name__ == '__main__':
    app.run()