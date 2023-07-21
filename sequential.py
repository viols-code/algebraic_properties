# PROJECT 8
# Project name: Algebraic Properties
# Short description: Usually, given two square matrices A and B it is not true that AB = BA.
# However, if B=cA, where c is a scalar, then AB=BA.
# The goal is to implement an algorithm for testing experimentally such hypothesis.

# SEQUENTIAL ALGORITHM

from optparse import OptionParser
import numpy as np
import time
from matrix_multiplication import multiplication


if __name__ == '__main__':
    parser = OptionParser()
    """ Adding all the options that can be given as parameters """
    parser.add_option("-n", action="store", dest='n', type='int', help="Dimension of the matrices")
    parser.add_option("-c", action="store", dest='c', type='int', help="Scalar constant c")

    """ Reading the arguments """
    (options, args) = parser.parse_args()
    n = options.n
    c = options.c

    start = time.time()
    # Initializing the number of hypothesis to verify
    num = 10

    """ Verifying experimentally the hypothesis """
    for i in range(num):
        # Generate random matrix of size n * n
        matrix_a = np.random.randint(low=-100, high=100, size=(n, n), dtype=int)
        # Compute matrix b
        matrix_b = c * matrix_a
        # Compute matrix products
        product1 = multiplication(matrix_a, matrix_b)
        product2 = multiplication(matrix_b, matrix_a)
        # Compare matrix products
        if np.array_equal(product1, product2):
            print("The hypothesis A{j}B{j} = B{j}A{j} is verified".format(j=i+1))
        else:
            print("A{j}B{j} is not equal to B{j}A{j}".format(j=i+1))

    end = time.time()
    print(f"The sequential algorithm took {end-start} seconds")
