#!/usr/bin/env python -tt

# Project euler, Question 1. Multiple of 3 and 5.
# if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Author: Om Prakash Singh
# Email: omps@omps.in


# find the no. between 1 to 10
count = 0
s = 0
a = range(1000)
a.pop(0)

for i in a:
    if i % 3 == 0 or i % 5 == 0:
        #print i
        s = s + i
        count = count + 1
print s
print count
