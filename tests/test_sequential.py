import io
import unittest
from unittest.mock import patch

from scripts.versions.sequential import sequential_strategy


class TestSequentialAlgorithm(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sequential_strategy(self, mock_stdout):
        num = 1
        c = 2
        n = 25
        idx = 0
        sequential_strategy(n, c, num)
        self.assertEqual(mock_stdout.getvalue()[:68], "The hypothesis A{j}B{j} = B{j}A{j} is verified\n"
                                                      "The sequential algorithm took".format(j=idx+1))


if __name__ == '__main__':
    unittest.main()
