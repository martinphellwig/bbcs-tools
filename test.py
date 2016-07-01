"""
Main Testing file.
"""
import unittest

class RequestsMock():
    "Requests Mock"
    def __init__(self):
        self.status_code = 200
        self.data_json = None
        self.data_post = None
        self.data = dict()

    def post(self, url, files):
        "POST"
        self.data['POST'] = [url, files]
        return self

    def get(self, url):
        "GET"
        self.data['GET'] = url
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

    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()

    def setUp(self):
        pass

    def test_01_smoke(self):
        "Just a smoke test."
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_first']
    unittest.main()