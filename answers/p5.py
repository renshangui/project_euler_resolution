#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
numbers = [i for i in range(1, 21)]


def get_gcb(a, b):
    if a < b:
        temp = a
        a = b
        b = temp

    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def get_multiple(l):
    if len(l) == 2:
        return l[0] * l[1] / get_gcb(l[0], l[1])
    multiple = get_multiple(l[1:])
    return l[0] * multiple / get_gcb(l[0], multiple)


print(get_multiple(numbers))