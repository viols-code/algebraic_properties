import io
import unittest
from unittest.mock import patch
from scripts.versions.parallel_ten_processes import control_algebraic_property, parallel_ten_processes_strategy


class TestParallelTenProcessesAlgorithm(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_control_algebraic_property(self, mock_stdout):
        dimension = 10
        constant = 11
        idx = 1
        control_algebraic_property(dimension, constant, idx)
        self.assertEqual(mock_stdout.getvalue(), "The hypothesis A{j}B{j} = B{j}A{j} is verified\n".format(j=idx+1))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_parallel_ten_processes_strategy(self, mock_stdout):
        num = 1
        c = 2
        n = 25
        parallel_ten_processes_strategy(n, c, num)
        self.assertEqual(mock_stdout.getvalue()[:45], "The parallel algorithm with 10 processes took")


if __name__ == '__main__':
    unittest.main()
