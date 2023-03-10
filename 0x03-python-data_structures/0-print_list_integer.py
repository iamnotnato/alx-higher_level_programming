#!/usr/bin/python3
# 0-print_list_integer.py


def print_list_integer(my_list=[]):
    """print integer in a list"""
    for elem in range(len(my_list)):
        print("{:d}".format(my_list[elem]))
