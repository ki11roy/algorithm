#!/usr/bin/env python

import sys
from collections import defaultdict

n = int(raw_input().strip())

MAX_LENGTH = 20

source = defaultdict(int)
for i in range(n):
	source[raw_input().strip()[:MAX_LENGTH]] += 1

print source		
m = int(raw_input().strip())
for i in range(m):
	print source[raw_input().strip()[:MAX_LENGTH]]


