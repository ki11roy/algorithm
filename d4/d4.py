#!/bin/python

import sys
from collections import deque

n, d = raw_input().strip().split(' ')
n, d = int(n), int(d)
arr = deque(map(int,raw_input().strip().split(' ')))

arr.rotate(-d)

for i in arr:
    print i,