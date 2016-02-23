#!/usr/bin/env python

from __future__ import division, print_function

def fib(n):
  a, b = 1, 2
  for i in range(n):
    a, b = b, a + b
  return a

Sum = 0

for j in range(30):
  if int(str(fib(j))[len(str(fib(j)))-1:len(str(fib(j)))]) % 2 != 0:
    Sum += fib(j)

print(Sum)
