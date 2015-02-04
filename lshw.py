#!/usr/bin/python -tt
# Parse lshw output and collect hardware data.

# Code is taken from https://gist.github.com/amitsaha/4554484
# I need to modify and pick various other part such as cpu, memory.


from lxml import etree
from subprocess import Popen,PIPE
inventory = Popen(['lshw', '-xml', '-numeric'], stdout=PIPE).communicate()[0]
inventory = etree.XML(inventory)
 
find_disks = etree.XPath(".//node[@class='disk']")
 
numdisks = 0
diskspace = 0
for disk in find_disks(inventory):
    # has to be a hard-disk
    if disk.find('size') is not None:
        numdisks = numdisks + 1
        diskspace = diskspace + int(disk.find('size').text)
        print disk.find('description').text, disk.find('product').text, disk.find('logicalname').text
        print 'Disk Space: ', disk.find('size').text
        print 'Sector size: ',disk.find('configuration/setting/[@id="sectorsize"]').get('value')
        print 
 
print 'Num disks', numdisks
print 'Total disk space', diskspace/(1024**2)

'''
Sample output:

'''

from lxml import etree
from subprocess import Popen, PIPE

inventory = Popen(['lshw', '-xml', '-numeric'], stdout=PIPE).communicate()[0]
inventory = etree.XML(inventory)

# checking only for the disk here, subsequent checks for other hardware parts need to be done along.

find_disks = etree.Xpath(".//node[@class='disk']")


numdisk = 0
diskspace = 0

for disk in find_disks(inventory):
    #check if this is hard disk or something else
    if disk.find('size') is not None:
        numdisk = numdisk + 1
        diskspace = diskspace + int(disk.find('size').text)
        print disk.find('description').text, disk.find('product').text, disk.find('logicalname').text
        print 'Disk Space: ', disk.find('size').text)
        print 'Sector Size: ', disk.find('configuration/setting/[@id="sectorsize"]').get('value')
        print

    print 'Num Disks: ', numdisk
    print 'Total Disk Space', diskspace/(1024*2)

=======
#/usr/bin/python -tt



import sys, commands
from xml.dom.minidom import parse, parseString

try:
    # lshw_xml = commands.getoutput('/usr/bin/lshw -xml')
    # print lshw_xml
    infile = sys.argv[1]
    
    if infile:
        lshw_dom = parse(infile)
    else:
        lshw_xml = parseString(lshw_xml)

    nodes = lshw_dom.childNodes
    for node in nodes:
    
        if node.nodeType == node.COMMENT_NODE:
            print "Comment: ", node.nodeValue
            
        if node.nodeType == node.ELEMENT_NODE:
            print node, node.childNodes

        if node.attributes:
            node_attrs = node.attributes
            for i in range(0, node_attrs.length):
                attr = node_attrs.item(i)
                print attr.name, attr.value

except:
    print "Unexpected error:", sys.exc_info()
