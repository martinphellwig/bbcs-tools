"""
Main Testing file.
"""
import unittest
import tempfile
import shutil
import os
from bbcs_tools import bitbucket
from bbcs_tools import pypi

ENV = {'CI_REPO_NAME':'user/repo',
       'CI_COMMIT_ID':'cafebabe',
       'CI_NAME':'codeship',
       'CI_BUILD_NUMBER':'42',
       'CI_BUILD_URL':'http://localhost/',
       'BB_USERNAME':'username',
       'BB_PASSWORD':'password',
       'PYPI_USERNAME':'pypi_username',
       'PYPI_PASSWORD':'pypi_password'}

for _ in ENV.items():
    os.environ[_[0]] = _[1]

class PopenMock(): # pylint: disable=too-few-public-methods
    "Mock the popen object"
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def wait(self):
        "Actually don't wait."
        pass


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

def call_setup_mock(*args, **kwargs): # pylint: disable=unused-argument
    "Just mock the call argument, we don't really want to call it."
    pass


# pylint: disable=missing-docstring, protected-access
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        bitbucket.requests = RequestsMock()
        pypi.requests = RequestsMock()
        pypi.Popen = PopenMock

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

    def test_02_smoke_pypi(self):
        "The pypi smoke test"
        pypi.requests.data_json = {'releases':dict()}
        self.assertTrue(pypi.upload())

    def test_03_pypy_valid_version(self):
        "Does valid version work?"
        data = {'version':'1', 'name':'test'}
        info = {'releases':{'0':None, '1':None, '2':None}}
        self.assertFalse(pypi._valid_version(data, info))

    def test_04_pypi_rc(self):
        "Does the rc file get generated?"
        tempdir = tempfile.mkdtemp()
        path = os.path.join(tempdir, 'dot.pypirc')
        rc_status = pypi._create_pypirc(path)
        self.assertTrue(rc_status[0])
        subsequent_rc = pypi._create_pypirc(path)
        self.assertFalse(subsequent_rc[0])
        self.assertTrue(os.path.exists(path))
        pypi._clean_up_rc(rc_status)
        self.assertFalse(os.path.exists(path))
        shutil.rmtree(tempdir)




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_first']
    unittest.main()