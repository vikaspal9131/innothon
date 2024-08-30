import sys
import os
import unittest
from test_project_api import ProjectApiTestCase
from test_model_api import ModelApiTestCase
from test_ecg_api import ECGApiTestCase
from test_user_api import UserApiTestCase

# Add the parent directory to PYTHONPATH
sys.path.insert(0, os.path.abspath('E:/AAYUSH TECH/Projects/skitech-streamlit/backend'))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ProjectApiTestCase))
    suite.addTest(unittest.makeSuite(ModelApiTestCase))
    suite.addTest(unittest.makeSuite(ECGApiTestCase))
    suite.addTest(unittest.makeSuite(UserApiTestCase))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
