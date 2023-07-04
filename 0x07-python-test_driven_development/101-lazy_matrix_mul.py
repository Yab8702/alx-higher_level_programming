#!/usr/bin/python3
"""import numpy and define the module of lazy_matrix_mul"""
import numpy as nmp


def lazy_matrix_mul(mtrx_a, mtrx_b):
    """
    Multiply 2 matrix with numpy
    """
    return nmp.matmul(mtrx_a, mtrx_b)
