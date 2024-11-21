import unittest
import mainFile


class TestMain(unittest.TestCase):

    def test_sumfive(self):
        ''' Testing for success'''
        test_param = 10
        result = mainFile.sumFive(test_param)
        self.assertEqual(result, 15, 'Success Test')

    def test_sumfive_for_failure(self):
        test_param = 10
        result = mainFile.sumFive(test_param)
        self.assertNotEqual(result, 20, 'The Failure test is successful')

    def test_for_valueError(self):
        test_param = 'jlkjlkj'
        result = mainFile.sumFive(test_param)
        self.assertTrue(isinstance(result, TypeError))

    def testing_for_none(self):
        test_param = None
        result = mainFile.sumFive(test_param)
        self.assertTrue(result, 'Please enter the number')

    def testing_for_empty(self):
        test_param = ''
        result = mainFile.sumFive(test_param)
        self.assertTrue(result, 'Please enter the number')


if __name__ == '__main__':
    unittest.main()
