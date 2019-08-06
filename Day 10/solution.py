#!/bin/python

import sys

n = int(input().strip())

result = 0
max_count = 0
while num > 0:
    if num % 2 == 1:
        result += 1
        if result > max_count:
            max_count = result
    else:
        result = 0
    num //= 2
print (max_count)
