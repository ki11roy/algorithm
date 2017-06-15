#!/usr/bin/env python

import sys

def print_seq_list(seq_list):
	for seq in seq_list:
		print seq,
	print

n, q = map(int, raw_input().strip().split(' '))
queries = []
for i in xrange(0, q):
	t, x, y = map(int, raw_input().strip().split(' '))
	queries.append((t, x, y))
 
#print n, q

seq_list = []
for i in xrange(0, n):
	seq_list.append([])

last_ans = 0
for t, x, y in queries:
	ind = (x ^ last_ans) % n
	if t == 1:
		seq_list[ind].append(y)	
	elif t == 2:
		seq = seq_list[ind]
		last_ans = seq[y % len(seq)]	
		print last_ans

	#print t, x ,y
	#print_seq_list(seq_list)



