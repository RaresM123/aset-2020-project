"""Decorator implemented for Authorizing the Requests made to Server"""
from flask import Flask, jsonify, request, render_template
import requests
import subprocess
import DataSetParser
import TransformersImplementation
from logger.logger import LOGGER
import traceback
import os
import numpy as np
import tensorflow as tf
import json
import model, sample, encoder
app = Flask(__name__)
AUTHORIZATION_TOKEN_EXPECTED = 'xy124zjw3'

def authorize(_function):
    """These will be used for making a simple form of authentication when requests are made to server"""
    def wrapper(*args, **kwargs):
        authentication_token = request.headers.get('AuthorizationToken')
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
        model_name = 'beta2'
        seed = None
        nsamples = 1
        batch_size = 1
        length = None
        temperature = 1
        top_k = 40
        top_p = 0.0
        raw_text = sentence

        if batch_size is None:
            batch_size = 1
        assert nsamples % batch_size == 0

        enc = encoder.get_encoder(model_name)
        hparams = model.default_hparams()
        with open(os.path.join('models', model_name, 'hparams.json')) as f:
            hparams.override_from_dict(json.load(f))

        if length is None:
            length = hparams.n_ctx // 2
        elif length > hparams.n_ctx:
            raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

        with tf.Session(graph=tf.Graph()) as sess:
            context = tf.placeholder(tf.int32, [batch_size, None])
            np.random.seed(seed)
            tf.set_random_seed(seed)
            output = sample.sample_sequence(
                hparams=hparams, length=length,
                context=context,
                batch_size=batch_size,
                temperature=temperature, top_k=top_k, top_p=top_p
            )

            saver = tf.train.Saver()
            ckpt = tf.train.latest_checkpoint(os.path.join('models', model_name))
            saver.restore(sess, ckpt)

            while True:
                context_tokens = enc.encode(raw_text)
                generated = 0
                for _ in range(nsamples // batch_size):
                    out = sess.run(output, feed_dict={
                        context: [context_tokens for _ in range(batch_size)]
                    })[:, len(context_tokens):]
                    for i in range(batch_size):
                        generated += 1
                        text = enc.decode(out[i])
                        return text.split('<|endoftext|>')[0]

    except:
        traceback.print_exc()
        exit()

"""this is where the authorization is made"""


@app.route('/check_statement', methods=['POST'])
# @authorize
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
    if not sentence:
        response['success'] = False
        LOGGER.error("Wrong key provided")
        # return jsonify(response)
        return render_template("public/response_sentence.html", page_body=response)
    try:
        processed_sentence = processSentence(sentence)
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
