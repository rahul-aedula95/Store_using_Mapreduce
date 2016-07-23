#!/usr/bin/python


import sys

for line in sys.stdin:
    #reading line by line 
    data = line.strip().split("\t")
   #assign a feild for every data instance 
    if len(data) == 6:
           date, time, store, item, cost, payment = data
           #display in streaming for input for hadoop streaming
           print "{0}\t{1}".format(store,cost)

