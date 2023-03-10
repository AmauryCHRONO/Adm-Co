#!/usr/bin/env python
# coding: utf-8
"""
author : Amaury CHRONOWSKI

"""


def add(num_1, num_2):
    """Cette fonction additionn 2 nombres"""
    res = num_1 + num_2
    print("add() executed under the scope: ", __name__)
    return res


if __name__ == "__main__":
    num_1 = input("Enter the first number to add: ")
    num_2 = input("Enter the secode number to add: ")
    res = add(int(num_1), int(num_2))
    print(num_1, "+", num_2, "=", res)
    print("Code executed under the scope: ", __name__)
