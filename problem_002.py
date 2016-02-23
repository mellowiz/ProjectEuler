#!/usr/bin/env python

from __future__ import division, print_function

MaxN = 4000000
Sum = 0
a, b = 1, 2
i = 0

while True:
  print("iteration: %d, value A = %d, value B = %d, Sum = %d" % (i, a, b, Sum))
  a, b = b, a + b			# fib(n) = fib(n-1) + fib(n-2)
  if a >= MaxN: break
  if a % 2 == 0:			# only add even numbers
    Sum += a
  i += 1

print(Sum)
