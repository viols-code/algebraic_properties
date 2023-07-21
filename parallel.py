# PROJECT 8
# Project name: Algebraic Properties
# Short description: Usually, given two square matrices A and B it is not true that AB = BA.
# However, if B=cA, where c is a scalar, then AB=BA.
# The goal is to implement an algorithm for testing experimentally such hypotheses

# PARALLEL ALGORITHM WITH MORE THAN 10 PROCESSES

from optparse import OptionParser
import numpy as np
from multiprocessing import Manager, Pool
import time
from matrix_multiplication import multiplication


def generate_random_matrix(queue_A, constant, dimension):
    # generate random matrix of size dimension * dimension
    matrix_a = np.random.randint(low=-100, high=100, size=(dimension, dimension), dtype=int)
    matrix_b = constant * matrix_a
    queue_A.put((matrix_a, matrix_b))


def compute_first_product(queue_A, queue_B):
    (matrix_a, matrix_b) = queue_A.get(block=True, timeout=None)
    product_1 = multiplication(matrix_a, matrix_b)
    queue_B.put((matrix_a, matrix_b, product_1))


def check_algebraic_property(queue_B, idx):
    (matrix_a, matrix_b, product_1) = queue_B.get(block=True, timeout=None)
    product_2 = multiplication(matrix_b, matrix_a)
    if np.array_equal(product_1, product_2):
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
    # Initializing the number of hypothesis to verify
    num = 10
    process = 10
    m = Manager()

    matrices_a = m.Queue(maxsize=num)
    products_1 = m.Queue(maxsize=num)

    args1 = [(matrices_a, c, n) for _ in range(num)]
    args2 = [(matrices_a, products_1) for _ in range(num)]
    args3 = [(products_1, i) for i in range(num)]

    # Create pools
    p1 = Pool(process)
    p2 = Pool(process)
    p3 = Pool(process)

    p1.starmap(generate_random_matrix, args1)
    p2.starmap(compute_first_product, args2)
    p3.starmap(check_algebraic_property, args3)

    p1.close()
    p2.close()
    p3.close()
    p1.join()
    p2.join()
    p3.join()

    end = time.time()
    print(f"The parallel algorithm with more than 10 processes took {end - start} seconds")
