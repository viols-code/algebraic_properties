import io
import unittest
from unittest.mock import patch
from scripts.versions.parallel_ten_processes import control_algebraic_property


class TestParallelAlgorithm(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_control_algebraic_property(self, mock_stdout):
        dimension = 10
        constant = 11
        idx = 1
        control_algebraic_property(dimension, constant, idx)
        self.assertEqual(mock_stdout.getvalue(), "The hypothesis A{j}B{j} = B{j}A{j} is verified\n".format(j=idx+1))


if __name__ == '__main__':
    unittest.main()
