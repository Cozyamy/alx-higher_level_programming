#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        end = ""
        for column in row:
            print("{}{:d}".format(end, column), end="")
            end = " "
        print("")
