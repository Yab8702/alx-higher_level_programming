#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        space = ' '
        for i, col in zip(range(len(matrix[row])), matrix[row]):
            if i == len(matrix[row]) - 1:
                space = ''
            print("{:d}".format(col), end=space)
        print("")
