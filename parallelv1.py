# PROJECT 8
# Project name: Algebraic Properties
# Short description: Usually, given two square matrices A and B it is not true that AB = BA.
# However, if B=cA, where c is a scalar, then AB=BA.
# The goal is to implement an algorithm for testing experimentally such hypothesis.

# PARALLEL ALGORITHM WITH 10 PROCESSES

from optparse import OptionParser
import numpy as np
from multiprocessing import Process
import time
from matrix_multiplication import multiplication


def control_algebraic_property(dimension, constant, idx):
    """
    Generation of random matrix
    :param dimension: dimension of the matrix to be generated
    :param constant: scalar constant for computing the second matrix
    :param idx: index of the matrices
    """
    # Generation of random matrix of size n * n
    matrix_a = np.random.randint(low=-100, high=100, size=(dimension, dimension), dtype=int)
    # Computation of matrix b
    matrix_b = constant * matrix_a
    # Computation of matrix products
    product1 = multiplication(matrix_a, matrix_b)
    product2 = multiplication(matrix_b, matrix_a)
    # Comparison between matrix products
    if np.array_equal(product1, product2):
        print("The hypothesis A{j}B{j} = B{j}A{j} is verified".format(j=idx+1))
    else:
        print("A{j}B{j} is not equal to B{j}A{j}".format(j=idx+1))


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
    # Initialize the number of hypothesis to verify
    num = 10

    # Create workers
    workers = [Process(target=control_algebraic_property, args=(n, c, i)) for i in range(num)]
    for worker in workers:
        worker.start()

    # Join workers
    for worker in workers:
        worker.join()

    end = time.time()
    print(f"The parallel algorithm with 10 processes took {end - start} seconds")
