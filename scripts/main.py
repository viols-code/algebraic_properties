# Course: Scientific Programming
# Project name: Algebraic Properties
# Author: Viola Renne
# Short description: Usually, given two square matrices A and B it is not true that AB = BA.
# However, if B=cA, where c is a scalar, then AB=BA.
# The goal is to implement an algorithm for testing experimentally such hypothesis.

from optparse import OptionParser
from versions.parallel_ten_processes import parallel_ten_processes_strategy
from versions.sequential import sequential_strategy
from versions.parallel import parallel_strategy


if __name__ == '__main__':
    parser = OptionParser()
    """ Adding all the options that can be given as parameters """
    parser.add_option("-n", action="store", dest='n', type='int', help="Dimension of the matrices")
    parser.add_option("-c", action="store", dest='c', type='int', help="Scalar constant c")
    parser.add_option("-a", action="store", dest='algorithm', type='string',
                      help="Algorithm selected.\n"
                           "Type sequential for the sequential algorithm.\n"
                           "Type parallel for the parallel algorithm with more than 10 processes.\n"
                           "Type parallelv1 for parallel with 10 processes.")

    """ Reading the arguments """
    (options, args) = parser.parse_args()
    n = options.n
    c = options.c
    algorithm = options.algorithm

    # Initializing the number of hypothesis to verify
    num = 10
    print(algorithm)
    if algorithm == 'sequential':
        sequential_strategy(n, c, num)
    elif algorithm == 'parallel':
        parallel_strategy(n, c, num)
    elif algorithm == 'parallelv1':
        parallel_ten_processes_strategy(n, c, num)
    else:
        print("Inserted a wrong algorithm.")
