#!/usr/bin/python -tt
# Parse lshw output and collect hardware data.

'''
Sample output:

'''

from lxml import etree
from subprocess import Popen, PIPE

inventory = Popen(['lshw', '-xml', '-numeric'], stdout=PIPE).communicate()[0]
inventory = etree.XML(inventory)

# checking only for the disk here, subsequent checks for other hardware parts need to be done along.

find.disks = etree.xpath
