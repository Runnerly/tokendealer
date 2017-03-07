import unittest
import os
from flask_webtest import TestApp as _TestApp

os.environ['TESTDIR'] = os.path.dirname(__file__)

from tokendealer.app import app


class TestSomething(unittest.TestCase):
    def setUp(self):
        self.app = _TestApp(app)

    def test_create(self):
        headers = {'Content-Type': 'application/vnd.api+json'}
        data = {'this': 'token'}
        resp = self.app.post_json('/create_token', params=data,
                                  headers=headers)
        token = resp.json['token']

        resp = self.app.post_json('/verify_token', params=resp.json,
                                  headers=headers)
        self.assertTrue(resp.json['this'], 'token')
