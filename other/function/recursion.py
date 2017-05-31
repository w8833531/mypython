#!/usr/bin/env python
# -*- coding=utf-8 -*-
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(1)
print fact(5)
print fact(30)
print fact(100)
print fact(500)
