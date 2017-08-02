#!/usr/bin/python
import numpy as np
import sys

infile = sys.argv[1]

a = np.load(infile)

for i in range(a.size/26):
    print "%s %s %s" %(a[i][1], a[i][2], a[i][11])#B
    #print "%s %s" %(a[i][3], a[i][13])#J
    #print "%s %s" %(a[i][3], a[i][15])#H
