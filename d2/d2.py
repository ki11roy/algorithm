#!/bin/python

import sys
import itertools
from itertools import islice, izip, chain, izip_longest, compress

selector = [
    1, 1, 1,
    0, 1, 0,
    1, 1, 1
]

def window(seq, n=3):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result    
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def build_matrix(x):
		w = []
		for y in x:
			r = []
			for v in window(y):
				r.append(v)
			w.append(r)

		return max(sum(compress(list(chain.from_iterable(g)), selector)) for g in izip(*w))

def traverse_with_window(arr):
	return max(build_matrix(x) for x in window(arr))


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)


print traverse_with_window(arr)
