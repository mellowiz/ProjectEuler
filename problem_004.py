#!/usr/bin/env python

from __future__ import division, print_function
import math, sys

minN = 900

def isPal(v):
  response = 1
  for i in range(len(str(v))):
    if str(v)[i] != str(v)[len(str(v)) - (i + 1)]:
      response = 0
      break
  return response

for i in range(999, minN, -1):
   for j in range(999, minN, -1):
     value = i * j
     print("%d x %d = %d" % (i, j, value))
     if isPal(value):
       print("***")
       sys.exit()
