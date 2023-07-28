import io
import unittest
from multiprocessing import Queue
from unittest.mock import patch

import numpy as np

from scripts.versions.parallel import generate_random_matrix, compute_first_product, check_algebraic_property, \
    parallel_strategy


class TestParallelAlgorithm(unittest.TestCase):

    def test_generate_random_matrix(self):
        queue = Queue()
        generate_random_matrix(queue, 2, 10)
        (matrix_a, matrix_b) = queue.get(block=True, timeout=None)
        self.assertEqual(matrix_a.shape, (10, 10))
        self.assertEqual(matrix_b.shape, (10, 10))
        np.testing.assert_array_equal(2 * matrix_a, matrix_b)

    def test_compute_first_product(self):
        queue = Queue()
        queue_product = Queue()
        generate_random_matrix(queue, 7, 20)
        compute_first_product(queue, queue_product)
        (matrix_a, matrix_b, product_1) = queue_product.get(block=True, timeout=None)
        self.assertEqual(matrix_a.shape, (20, 20))
        self.assertEqual(matrix_b.shape, (20, 20))
        np.testing.assert_array_equal(7 * matrix_a, matrix_b)
        np.testing.assert_array_equal(product_1, np.matmul(matrix_a, matrix_b))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_algebraic_property_true(self, mock_stdout):
        queue_product = Queue()
        dimension = 20
        constant = 9
        idx = 0
        matrix_a = np.random.randint(low=-100, high=100, size=(dimension, dimension), dtype=int)
        matrix_b = constant * matrix_a
        product = np.matmul(matrix_a, matrix_b)
        queue_product.put((matrix_a, matrix_b, product))
        check_algebraic_property(queue_product, idx)
        self.assertEqual(mock_stdout.getvalue(), "The hypothesis A{j}B{j} = B{j}A{j} is verified\n".format(j=idx + 1))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_algebraic_property_false(self, mock_stdout):
        queue_product = Queue()
        dimension = 30
        constant = 7
        idx = 2
        matrix_a = np.random.randint(low=-100, high=100, size=(dimension, dimension), dtype=int)
        matrix_b = constant * matrix_a
        matrix_2 = np.random.randint(low=-100, high=100, size=(dimension, dimension), dtype=int)
        product = np.matmul(matrix_a, matrix_2)
        queue_product.put((matrix_a, matrix_b, product))
        check_algebraic_property(queue_product, idx)
        self.assertEqual(mock_stdout.getvalue(), "A{j}B{j} is not equal to B{j}A{j}\n".format(j=idx + 1))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_parallel_strategy(self, mock_stdout):
        num = 1
        c = 2
        n = 25
        parallel_strategy(n, c, num)
        self.assertEqual(mock_stdout.getvalue()[:55], "The parallel algorithm with more than 10 processes took")


if __name__ == '__main__':
    unittest.main()
