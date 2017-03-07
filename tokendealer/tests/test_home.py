import unittest
import os
from flask_webtest import TestApp as _TestApp

os.environ['TESTDIR'] = os.path.dirname(__file__)

from tokendealer.app import app         # NOQA


class TestSomething(unittest.TestCase):
    def setUp(self):
        self.app = _TestApp(app)
        self.headers = {'Content-Type': 'application/vnd.api+json'}

    def test_get_pub_key(self):
        resp = self.app.get('/')
        self.assertTrue('pub_key' in resp.json)

    def test_roundtrip(self):
        data = {'this': 'token'}
        resp = self.app.post_json('/create_token', params=data,
                                  headers=self.headers)
        resp = self.app.post_json('/verify_token', params=resp.json,
                                  headers=self.headers)
        self.assertTrue(resp.json['this'], 'token')

    def test_bad_tokens(self):
        resp = self.app.post_json('/verify_token', params={'token': 'd.A.D'},
                                  headers=self.headers, status=400)
        self.assertEqual(resp.json['description'], 'Invalid header padding')

        resp = self.app.post_json('/verify_token', params={},
                                  headers=self.headers, status=400)
        self.assertEqual(resp.json['description'], "'token'")
