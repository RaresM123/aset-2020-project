"""Decorator implemented for Authorizing the Requests made to Server"""
from flask import Flask, jsonify, request, render_template
import requests
import subprocess
from logger.logger import LOGGER
import traceback
import os
import numpy as np
import tensorflow as tf
import json
import model, sample, encoder

import DataSetParser
import TransformersImplementation
import Monitors
import config

AUTHORIZATION_TOKEN_EXPECTED = os.environ['AUTHENTICATION_TOKEN']

app = Flask(__name__)

PARAMS_DICT = {"model_name": None,
               "seed": None,
               "nsamples": None,
               "batch_size": None,
               "length": None,
               "temperature": None,
               "top_k": None,
               "top_p": None,
               "raw_text": None}


def authorize(_function):
    """These will be used for making a simple form of authentication when requests are made to server"""
    def wrapper(*args, **kwargs):
        authentication_token = request.form.get('AuthorizationToken')
        if authentication_token == AUTHORIZATION_TOKEN_EXPECTED:
            LOGGER.info("Successful auth")
            return _function(*args, **kwargs)
        else:
            LOGGER.error("Failed auth with token {}".format(authentication_token))
            return 'Wrong Token', requests.status_codes.codes['unauthorized']
    return wrapper


def processSentence(sentence):

    LOGGER.info("start processing sentence: {}".format(sentence))
    try:
        # output = subprocess.check_output('python3 src/interactive_conditional_samples.py --raw_text "{}"'.format(sentence),shell=True)
        # response = output.decode('utf-8').split("\n")[-2]
        # print(response)
        # return response
        PARAMS_DICT["model_name"] = 'beta2'
        PARAMS_DICT["seed"] = None
        PARAMS_DICT["nsamples"] = 1
        PARAMS_DICT["batch_size"] = 1
        PARAMS_DICT["length"] = None
        PARAMS_DICT["temperature"] = 1
        PARAMS_DICT["top_k"] = 40
        PARAMS_DICT["top_p"] = 0.0
        PARAMS_DICT["raw_text"] = sentence
        NEW_PARAMS_DICT = Monitors.monitor_parameters(PARAMS_DICT)

        assert NEW_PARAMS_DICT["nsamples"] % NEW_PARAMS_DICT["batch_size"] == 0

        enc = encoder.get_encoder(NEW_PARAMS_DICT["model_name"])
        hparams = model.default_hparams()
        with open(os.path.join('models', NEW_PARAMS_DICT["model_name"], 'hparams.json')) as f:
            hparams.override_from_dict(json.load(f))

        if NEW_PARAMS_DICT["length"] is None:
            NEW_PARAMS_DICT["length"] = hparams.n_ctx // 2
        elif NEW_PARAMS_DICT["length"] > hparams.n_ctx:
            raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

        with tf.Session(graph=tf.Graph()) as sess:
            context = tf.placeholder(tf.int32, [NEW_PARAMS_DICT["batch_size"], None])
            np.random.seed(NEW_PARAMS_DICT["seed"])
            tf.set_random_seed(NEW_PARAMS_DICT["seed"])
            output = sample.sample_sequence(
                hparams=hparams, length=NEW_PARAMS_DICT["length"],
                context=context,
                batch_size=NEW_PARAMS_DICT["batch_size"],
                temperature=NEW_PARAMS_DICT["temperature"], top_k=NEW_PARAMS_DICT["top_k"],
                top_p=NEW_PARAMS_DICT["top_p"]
            )

            saver = tf.train.Saver()
            ckpt = tf.train.latest_checkpoint(os.path.join('models', NEW_PARAMS_DICT["model_name"]))
            saver.restore(sess, ckpt)

            while True:
                context_tokens = enc.encode(NEW_PARAMS_DICT["raw_text"])
                generated = 0
                for _ in range(NEW_PARAMS_DICT["nsamples"] // NEW_PARAMS_DICT["batch_size"]):
                    out = sess.run(output, feed_dict={
                        context: [context_tokens for _ in range(NEW_PARAMS_DICT["batch_size"])]
                    })[:, len(context_tokens):]
                    for i in range(NEW_PARAMS_DICT["batch_size"]):
                        generated += 1
                        text = enc.decode(out[i])
                        return text.split('<|endoftext|>')[0]

    except:
        traceback.print_exc()
        exit()

"""this is where the authorization is made"""


@app.route('/check_statement', methods=['POST'])
@authorize
def SendStatement():


    sentence = request.form['sentence']
    response = {
        'success': True,
        'processedSentence': None
    }

    # try:
    #     body = request.get_json() or dict()
    # except:
    #     body = dict()
    # sentence = body.get('sentence')
    # if not sentence:
    #     response['success'] = False
    #     LOGGER.error("Wrong key provided")
    #     # return jsonify(response)
    #     return render_template("public/response_sentence.html", page_body=response)
    try:
        processed_sentence = Monitors.Monitor_InputSentence(sentence)
        processed_sentence = processSentence(processed_sentence)
    except Exception as e:
        print(e.stack)
        response['success'] = False
        LOGGER.error("Failed to process sentence")
        # return jsonify(response)
        return render_template("public/response_sentence.html", page_body=response)

    response['processedSentence'] = str(processed_sentence)
    LOGGER.info("request successfully processed")
    # return jsonify(response)
    print(response)
    return render_template("public/response_sentence.html",
                           page_body="Generated sentence is: {}".format(response['processedSentence']))


@app.route("/")
def index():
    return render_template("public/insert_sentence.html")


if __name__ == '__main__':
    app.run()
