#!/usr/bin/python2.7

import sys

def Hello(name):
  if name == 'Alice' or name == 'Nick':
    print 'Alert: Alice Mode'
    name = name + '???'
  else:
    print 'Else'
 name = name + '!!!!'
 print 'Hello', name
