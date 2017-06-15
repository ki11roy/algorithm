#!/usr/bin/env python

import sys
import operator
from collections import defaultdict
from operator import itemgetter
from time import time

n, m = map(int, raw_input().strip().split(' '))

endpoints = []
for i in range(m):
    a, b, k = map(int, raw_input().strip().split(' '))
    endpoints.append((a, 0, k))
    endpoints.append((b, 1, k))

start = time()

max_sum = partial_sum = 0
got_best_interval = False
best_interval_start = best_interval_end = 0
for endpoint, is_start, weight in sorted(endpoints, key=itemgetter(0, 1)):
    print "{} w:{} {}".format(endpoint, weight, is_start)
    if not is_start:
        partial_sum += weight
        if partial_sum > max_sum:
            best_interval_start = endpoint
            got_best_interval = True
    else:
        if got_best_interval:
            max_sum = partial_sum
            best_interval_end = endpoint
            got_best_interval = False
        partial_sum -= weight

stop=time()

if got_best_interval:
    max_sum = partial_sum

print best_interval_start, best_interval_end, max_sum,
print 'time:', stop-start
