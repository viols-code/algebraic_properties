# PARALLEL ALGORITHM WITH MORE THAN 10 PROCESSES

import time
from multiprocessing import Manager, Pool
import numpy as np
from .utils import matrix_multiplication


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
    product_1 = matrix_multiplication(matrix_a, matrix_b)
    queue_product.put((matrix_a, matrix_b, product_1))


def check_algebraic_property(queue_product, idx):
    """
    Computation of second product and control of the equality
    :param queue_product: queue of first product
    :param idx: index of the matrices
    """
    (matrix_a, matrix_b, product_1) = queue_product.get(block=True, timeout=None)
    product_2 = matrix_multiplication(matrix_b, matrix_a)
    if np.array_equal(product_1, product_2):
        print("The hypothesis A{j}B{j} = B{j}A{j} is verified".format(j=idx+1))
    else:
        print("A{j}B{j} is not equal to B{j}A{j}".format(j=idx+1))


def parallel_strategy(n, c, num):
    start = time.time()
    process = 5

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
