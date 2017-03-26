#!/usr/bin/python

import sys

totalHit = 0.0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    count = int(thisSale)

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", totalHit
        oldKey = thisKey;
        totalHit = 0

    oldKey = thisKey
    totalHit += count

if oldKey != None:
    print oldKey, "\t", totalHit