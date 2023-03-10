#!/usr/bin/python3
# 3-print_reserved_list_integer


def print_reversed_list_integer(my_list=[]):
    """print a list in reverse"""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
