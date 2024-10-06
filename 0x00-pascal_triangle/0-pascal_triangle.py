#!/usr/bin/python3
"""
Print Pascal's Triangle
"""


def pascal_triangle(n):
    """returns Pascal's triangle in a list of list"""
    my_list = []
    if (n <= 0):
        return my_list
    my_list.append([1])
    for i in range(n - 1):
        my_list.append([1] + [my_list[i][a] + my_list[i][a + 1]
                              for a in range(len(my_list[i]) - 1)] + [1])
    return my_list
