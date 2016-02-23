#!/usr/bin/env python

from __future__ import division, print_function

maxRange = raw_input('Enter upper range limit: ')
maxRangeN = int(maxRange)

L = []						# initialize empty list
for i in range(1,maxRangeN):
  if (i // 3 == i / 3) or (i // 5 == i / 5):	# only add to L multiples of 3 or 5
    L.append(i)

print("List of numbers between 1 and %d:" % maxRangeN)
print(L)

Sum = 0
for j in L:
  Sum += j

print("Sum is", Sum)
