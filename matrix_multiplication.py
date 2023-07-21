import numpy as np


def multiplication(matrix_1, matrix_2):
    if matrix_1.shape[1] != matrix_2.shape[0]:
        print("Error: the two matrices cannot be multiplied")
        return
    new_matrix = np.zeros((matrix_1.shape[0], matrix_2.shape[1]))
    for i in range(matrix_1.shape[0]):
        for j in range(matrix_2.shape[1]):
            for k in range(matrix_1.shape[1]):
                new_matrix[i, j] += matrix_1[i, k] * matrix_2[k, j]
    return new_matrix
