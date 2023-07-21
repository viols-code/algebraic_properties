import numpy as np


def multiplication(matrix_1, matrix_2):
    """
    Multiplication between two two-dimensional matrices
    :param matrix_1: first matrix
    :param matrix_2: second matrix
    :return: multiplication between the two matrices
    """
    # Controls if shape of the matrices is compatible with multiplication
    if matrix_1.shape[1] != matrix_2.shape[0]:
        print("Error: the two matrices cannot be multiplied")
        return
    # Computing the multiplication
    new_matrix = np.zeros((matrix_1.shape[0], matrix_2.shape[1]))
    for i in range(matrix_1.shape[0]):
        for j in range(matrix_2.shape[1]):
            for k in range(matrix_1.shape[1]):
                new_matrix[i, j] += matrix_1[i, k] * matrix_2[k, j]
    return new_matrix
