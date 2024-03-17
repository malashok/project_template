import unittest
import os
import pandas as pd
from app.io.input import input_from_file, input_from_file_pd


class TestInputFunctions(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test.txt'
        with open(self.test_file, 'w') as file:
            file.write('test')

    def tearDown(self):
        os.remove(self.test_file)

    def test_input_from_file(self):
        expected_out = 'test'
        output = input_from_file(self.test_file)
        self.assertEqual(output, expected_out)

    def test_input_from_file_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            input_from_file('notexist.txt')

    def test_input_from_file_empty(self):
        with open(self.test_file, 'w') as file:
            file.write('')
        output = input_from_file(self.test_file)
        self.assertEqual(output, '')


class TestInputFromFilePd(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test.txt'
        with open(self.test_file, 'w') as file:
            file.write('test\ntest2')

    def tearDown(self):
        os.remove(self.test_file)

    def test_input_from_file_pd(self):
        import pandas as pd
        expected_output = pd.DataFrame({'test': ['test2']})
        output = input_from_file_pd(self.test_file)
        pd.testing.assert_frame_equal(output, expected_output)

    def test_input_from_file_pd_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            input_from_file_pd('notexist.txt')

    def test_input_from_file_pd_empty_file_header_only(self):
        with open(self.test_file, 'w') as file:
            file.write('column1,column2\n')
        output = input_from_file_pd(self.test_file)
        pd.testing.assert_frame_equal(output, pd.DataFrame(columns=['column1', 'column2']))


if __name__ == '__main__':
    unittest.main()
