#!/usr/bin/python

import sys

countTotal = 0
oldKey = None

#same drill we will be reading line by line
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) !=2 :
        # contingency check
        continue

    thisKey,thiscount = data_mapped #the variables speak for themselves 
          
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", countTotal
        oldKey = thisKey;
        countTotal = 0

    oldKey = thisKey
    countTotal += float(thiscount)
    

if oldKey != None:

   print oldKey, "\t", countTotal,"\t" 
