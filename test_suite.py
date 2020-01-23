import unittest

def allTests():
    from test_case_4 import TestCase4
    from test_case_5 import TestCase5
    from test_case_6 import TestCase6
    from test_case_7 import TestCase7
    from test_case_8 import TestCase8
    """
     Launch all test cases
    :return:
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCase4))
    suite.addTest(unittest.makeSuite(TestCase5))
    suite.addTest(unittest.makeSuite(TestCase6))
    suite.addTest(unittest.makeSuite(TestCase7))
    suite.addTest(unittest.makeSuite(TestCase8))

    return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(allTests())

