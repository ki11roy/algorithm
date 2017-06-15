#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

if n <= 0:
    exit(255)

if n < len(arr): 
    del arr[n:]

for i in reversed(arr):
    print i,