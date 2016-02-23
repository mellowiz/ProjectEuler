#!/usr/bin/env python

from __future__ import division, print_function
import math

MaxN = 600851475143

def divisors(n):
  L= []
  for i in range(2, int(math.floor(math.sqrt(n)))):
    if n % i == 0:
      L.append(i)
  return L

print("Finding maximum prime divisor for", MaxN)
L1 = divisors(MaxN)
print("All divisors:", L1)

for j in reversed(L1):
  if divisors(j) == []:
    print("Largest prime factor is", j)
    break
