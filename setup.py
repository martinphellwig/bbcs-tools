"""
PyPi Setup file.
"""
import os
# pylint: disable=no-name-in-module, import-error
from setuptools import setup

NAME = 'BBCS-Tools'
DESCRIPTION = 'Bitbucket Codeship integration tools'
VERSION = '0.0.0.1'
LICENSE = 'BSD'
AUTHOR = 'Martin P. Hellwig'
AUTHOR_EMAIL = 'martin.hellwig@gmail.com'
#
URL_MAIN = "https://bitbucket.org/hellwig/" + NAME + '/'
DOWNLOAD_ID = os.environ.get('CI_COMMIT_ID', VERSION)
URL_DOWNLOAD = URL_MAIN + 'get/' + DOWNLOAD_ID + '.zip'
#
PACKAGES = ['bbcs_tools']
PACKAGE_DATA  = {}
# SCRIPT = 'upload_coveralls_csbb='\
#          'coveralls_hg.coveralls_codeship:main'
SCRIPT = None
KEYWORDS = [
    'Coveralls',
    'Codeship',
    'BitBucket'
    ]
CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    ]
REQUIREMENTS = [
    'requests',
    'coverage',
    ]


################################################################################

KWARGS = {
    'name':NAME, 'packages':PACKAGES, 'version':VERSION,
    'description':DESCRIPTION, 'author':AUTHOR, 'author_email':AUTHOR_EMAIL,
    'url':URL_MAIN, 'download_url':URL_DOWNLOAD, 'keywords':KEYWORDS,
    'license':LICENSE, 'classifiers':CLASSIFIERS,
    'install_requires':REQUIREMENTS, 'package_data':PACKAGE_DATA,
    'entry_points':{'console_scripts':[SCRIPT]},}

setup(**KWARGS)
