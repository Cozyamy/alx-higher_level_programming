#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    m_list = [0, 0, 0, 0]
    a = 0

    for number in tuple_a:
        if a < 2:
            m_list[a] = number
            a += 1

    a = 2
    for number in tuple_b:
        if a < 4:
            m_list[a] = number
            a += 1

    return (m_list[0] + m_list[2], m_list[1] + m_list[3])
