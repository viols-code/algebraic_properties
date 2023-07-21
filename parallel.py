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


def generate_random_matrix(queue, constant, dimension):
    """
    Generation of random matrix
    :param queue: queue of generated matrices
    :param constant: scalar constant for computing the second matrix
    :param dimension: dimension of the matrix to be generated
    """
    # generate random matrix of size dimension * dimension
    matrix_a = np.random.randint(low=-100, high=100, size=(dimension, dimension), dtype=int)
    matrix_b = constant * matrix_a
    queue.put((matrix_a, matrix_b))


def compute_first_product(queue, queue_product):
    """
    Computation of first product
    :param queue: queue of generated matrices
    :param queue_product: queue of first product
    """
    (matrix_a, matrix_b) = queue.get(block=True, timeout=None)
    product_1 = multiplication(matrix_a, matrix_b)
    queue_product.put((matrix_a, matrix_b, product_1))


def check_algebraic_property(queue_product, idx):
    """
    Computation of second product and control of the equality
    :param queue_product: queue of first product
    :param idx: index of the matrices
    """
    (matrix_a, matrix_b, product_1) = queue_product.get(block=True, timeout=None)
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
    # Initializing the number of processes for each pool
    process = 4

    # Initializing queues
    m = Manager()
    matrices_a = m.Queue(maxsize=num)
    products_1 = m.Queue(maxsize=num)

    # Initializing arguments
    args1 = [(matrices_a, c, n) for _ in range(num)]
    args2 = [(matrices_a, products_1) for _ in range(num)]
    args3 = [(products_1, i) for i in range(num)]

    # Creating pools
    p1 = Pool(process)
    p2 = Pool(process)
    p3 = Pool(process)

    # Assigning functions to pools
    p1.starmap(generate_random_matrix, args1)
    p2.starmap(compute_first_product, args2)
    p3.starmap(check_algebraic_property, args3)

    # Closing and Joining pools
    p1.close()
    p2.close()
    p3.close()
    p1.join()
    p2.join()
    p3.join()

    end = time.time()
    print(f"The parallel algorithm with more than 10 processes took {end - start} seconds")
