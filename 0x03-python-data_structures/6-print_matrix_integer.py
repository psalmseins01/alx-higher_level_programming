#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, elem in enumerate(i):
            if j == len(i) - 1:
                print('{}'.format(elem), end=' ')
            else:
                print('{}'.format(elem), end=' ')
        print()
