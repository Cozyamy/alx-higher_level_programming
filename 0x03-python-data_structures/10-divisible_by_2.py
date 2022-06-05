#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    def iseven(n): return True if n % 2 == 0 else False
    new_list = [iseven(i) for i in my_list]

    return (new_list)
