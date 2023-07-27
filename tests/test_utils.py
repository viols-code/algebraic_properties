import unittest
import numpy as np
from scripts.versions.utils import matrix_multiplication


class TestMatrixMultiplication(unittest.TestCase):

    def test_simple_multiplication(self):
        matrix_1 = np.array([[1, 2], [3, 4]])
        matrix_2 = np.array([[1, 2, 3], [4, 5, 6]])
        product = matrix_multiplication(matrix_1, matrix_2)
        np.testing.assert_array_equal(product, np.array([[9, 12, 15], [19, 26, 33]]))

    def test_zero_multiplication(self):
        matrix_1 = np.zeros((3, 2))
        matrix_2 = np.zeros((2, 3))
        product = matrix_multiplication(matrix_1, matrix_2)
        np.testing.assert_array_equal(product, np.zeros((3, 3)))

    def test_size_multiplication(self):
        matrix_1 = np.ones((3, 2))
        matrix_2 = np.zeros((3, 3))
        with self.assertRaises(Exception):
            matrix_multiplication(matrix_1, matrix_2)

    def test_matrix_multiplication(self):
        dimension = 10
        for i in range(10):
            matrix_1 = np.random.randint(low=-100, high=100, size=(dimension, dimension), dtype=int)
            matrix_2 = np.random.randint(low=-100, high=100, size=(dimension, dimension), dtype=int)
            product = matrix_multiplication(matrix_1, matrix_2)
            np.testing.assert_array_equal(product, np.matmul(matrix_1, matrix_2))


if __name__ == '__main__':
    unittest.main()
