# Algebraic Properties

## :bookmark_tabs: Menu
* [Overview](#overview)
* [Description](#description)
* [Implementation](#implementation)
* [Usage](#usage)

## Overview
This is a project proposed by the Scientific Programming course by Politecnico di Milano

## Description
**Project name:** Algebraic Properties  
**Programming language:** Python  
**Short description:** Usually, given two square matrices A and B it is not true that AB = BA.
However, if B = cA, where c is a scalar, then AB=BA.
The goal is to implement an algorithm for testing experimentally such hypotheses  
**Expected outcome:** Implement an algorithm for testing experimentally such hypotheses. It is
required to:
1. Take as input an integer N and a scalar c
2. Generate 10 random matrices N*N: A1, A2, …, A10
3. Generate 10 matrices as: B1=cA1, B2=cA2, ..., B10=cA10
4. Test the equality that AiBi = BiAi for i = 1, 2, 3, …, 10
5. Considering a number of threads T > 10, design a second version of the algorithm that uses
multiprocessing to speed up the execution.
6. NB: as the number of threads is > 10, assigning each pair of matrices to a single process is
not a valid solution, as some processes will be unused.

## Implementation
Three different algorithms were implemented:
- a sequential algorithm (sequential.py);
- a parallel algorithm that uses ten processes (parallelv1.py);
- a parallel algorithm that uses three pools of ten processes each (parallel.py).

A matrix multiplication function was also implemented, since the numpy.dot() function is already parallelized.
Using an implementation of the matrix multiplication helps better understand the difference in the execution time 
between the three algorithms. Since creating processes costs time, to see an improvement in the execution time using 
multiprocessing, it is necessary that N is large enough.

A test program was implemented, in order to visualize the differences between the three algorithms.

## Usage

1. **Install the requirements.**  
    In order to install the requirements, use:  
    ```bash
    pip install -r requirements.txt
    ```
   
2. **Add options.**  
In order see the possible options, open a terminal, cd into project directory and type:
   ```bash
   python name_algorithm --help 
   ```
For example:
   ```bash
   python sequential.py --help
   ```

3. **Standard benchmark simulation.**  
By default, main.py runs a vascular network which represents the Circle of Willis.
Open a terminal cd into project directory and type:
   ```bash
   python name_algorithm -n N -c c
   ```
For example:
   ```bash
   python sequential.py -n 100 -c 12
   ```