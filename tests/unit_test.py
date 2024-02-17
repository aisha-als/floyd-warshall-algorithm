import sys
import unittest
import test_data
from floydwarshall.floyd_warshall import floyd_recursive

NO_PATH = sys.maxsize

class TestDatasets(unittest.TestCase):

    def test_original(self):
        self.assertEqual(floyd_recursive(test_data.original_graph), test_data.original_expected)

    def test_a(self):
        self.assertEqual(floyd_recursive(test_data.test_a), test_data.a_expected)

    def test_b(self):
        self.assertEqual(floyd_recursive(test_data.test_b), test_data.b_expected)

    def test_c(self):
        self.assertEqual(floyd_recursive(test_data.test_c), test_data.c_expected)

    def test_d(self):
        self.assertRaises(IndexError, floyd_recursive,test_data.test_d)

    def test_e(self):
        self.assertEqual(floyd_recursive(test_data.test_e), test_data.e_expected)

#class TestDatasetsResults(unittest.TestResult):

if __name__ == '__main__':
    unittest.main()