#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 zqhz
#
def get_multiple():
    l = [i for i in range(1000) if (i % 3 == 0 or i % 5 == 0)]
    return sum(l)

if __name__ == '__main__':
    print(get_multiple())
