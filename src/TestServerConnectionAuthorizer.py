from unittest import TestCase

import requests


class Test(TestCase):
    def test_authorize(self):
        """
        1. Testing if authorization token is correct, the status of the response to be 200(OK)
        2. Testing if authorization token is wrong, the status of the response to be 401(forbidden)
        """
        URL = r'http://127.0.0.1:5000/check_statement'

        response = requests.post(URL, data={"sentence": "Ana are mere", 'AuthorizationToken': 'xy124zjw3'})
        self.assertEqual(response.status_code, 200)

        response = requests.post(URL, data={"sentence": "Ana are mere", 'AuthorizationToken': 'xy124z3'})
        self.assertEqual(response.status_code, 401)
