#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    no1 = 0
    no2 = 0

    for tup in my_list:
        no1 += tup[0] * tup[1]
        no2 += tup[1]

    return (no1 / no2)
