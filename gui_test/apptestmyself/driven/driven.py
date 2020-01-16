import unittest
from gui_test.apptestmyself.testcase.calculator_test import Cacl

def start1():
    suite=unittest.TestSuite()
    suite.addTest(Cacl('test_add'))
    run=unittest.TextTestRunner(verbosity=2)
    run.run(suite)
if __name__=='__main__':
    start1()