#!/usr/bin/python3
def no_c(my_string):

    replace = ""

    for a in my_string:
        if a != 'C' and a != 'c':
            replace += a

    return (replace)
