#!/usr/bin/python

import sys

totalHit = 0
oldKey = None

maxHit = 0
maxHitKey = ""

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    count = int(thisSale)

    if oldKey and oldKey != thisKey:
        if totalHit > maxHit:
            maxHit = totalHit
            maxHitKey = oldKey
        oldKey = thisKey;
        totalHit = 0

    oldKey = thisKey
    totalHit += count

if oldKey != None:
    if totalHit > maxHit:
        maxHit = totalHit
        maxHitKey = oldKey

print maxHitKey, "\t", maxHit