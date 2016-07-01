"""
Main Testing file.
"""
import unittest
import os
from bbcs_tools import bitbucket

ENV = {'CI_REPO_NAME':'user/repo',
       'CI_COMMIT_ID':'cafebabe',
       'CI_NAME':'codeship',
       'CI_BUILD_NUMBER':'42',
       'CI_BUILD_URL':'http://localhost/',
       'BB_USERNAME':'username',
       'BB_PASSWORD':'password'}

for _ in ENV.items():
    os.environ[_[0]] = _[1]


class RequestsMock():
    "Requests Mock"
    def __init__(self):
        self.status_code = 200
        self.data_json = None
        self.data_post = None
        self.data = dict()

    def post(self, *args, **kwargs):
        "POST"
        self.data['POST'] = [args, kwargs]
        return self

    def get(self, *args, **kwargs):
        "GET"
        self.data['GET'] = [args, kwargs]
        return self

    def raise_for_status(self):
        "Raise an error"
        if self.status_code >= 200 and self.status_code < 300:
            return False
        raise ValueError('raise for status')

    def json(self):
        "Return json data."
        return self.data_json


# pylint: disable=missing-docstring, protected-access
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        bitbucket.requests = RequestsMock()

    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()

    def setUp(self):
        pass

    def test_01_smoke_bitbucket(self):
        "Just a smoke test."
        bitbucket.build_started()
        bitbucket.build_stopped()
        self.assertRaises(SystemExit, bitbucket.build_failure)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_first']
    unittest.main()