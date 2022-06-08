#!/usr/bin/python3
def roman_to_int(roman_string):
    """This converts a Roman numeral to an integer"""

    dic_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    no = 0
    current = dic_num.get(roman_string[0], 0)

    for i in roman_string[1:]:
        next_n = dic_num.get(i, 0)

        if (current == 0 or next_n == 0):
            return (0)

        if current < next_n:
            no += current * -1
        else:
            no += current
        current = next_n

    no += current
    return (no)
