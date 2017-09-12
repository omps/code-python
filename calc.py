#!/usr/bin/python
def add(a,b):
   '''
   >>> print(add(10,20))
   30
   '''
   return a + b

def sub(a,b):
   '''
   >>> print(sub(10,20))
   -10
   '''
   return a - b

def multi(a,b):
   '''
   >>> print(multi(10,20))
   200
   '''
   return a * b

def div(a,b):
   '''
   >>> print(div(10,20))
   0.5
   '''
   return a / b

def total(a,b):
   return a + b

import doctest
doctest.testmod()
