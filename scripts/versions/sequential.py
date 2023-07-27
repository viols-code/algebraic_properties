# SEQUENTIAL ALGORITHM

import numpy as np
import time
from .utils import matrix_multiplication


def sequential_strategy(n, c, num):
    start = time.time()

    """ Verifying experimentally the hypothesis """
    for i in range(num):
        # Generate random matrix of size n * n
        matrix_a = np.random.randint(low=-100, high=100, size=(n, n), dtype=int)
        # Compute matrix b
        matrix_b = c * matrix_a
        # Compute matrix products
        product1 = matrix_multiplication(matrix_a, matrix_b)
        product2 = matrix_multiplication(matrix_b, matrix_a)
        # Compare matrix products
        if np.array_equal(product1, product2):
            print("The hypothesis A{j}B{j} = B{j}A{j} is verified".format(j=i+1))
        else:
            print("A{j}B{j} is not equal to B{j}A{j}".format(j=i+1))

    end = time.time()
    print(f"The sequential algorithm took {end-start} seconds")
