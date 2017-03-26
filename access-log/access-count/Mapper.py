#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys


def getFirstWord(data, splitter, checkOn, strip_char=None):
    data = data.split(splitter, 1)
    if checkOn and len(data) != 2:
        return None
    elif checkOn is False:
        return data[0], None

    word, data = data
    if strip_char is None:
        strip_char = ' '
    word = word.strip(strip_char)
    return word, data


for line in sys.stdin:
    data = line.strip()
    ip, data = getFirstWord(data, ' ', True)
    identity, data = getFirstWord(data, ' ', True)
    username, data = getFirstWord(data, ' ', True)
    date, data = getFirstWord(data, "] ", True, "[")
    url, data = getFirstWord(data, "\" ", True, "\"")
    response_code, data = getFirstWord(data, ' ', True)
    response_size, data = getFirstWord(data, ' ', False)
    request = url.split(' ')
    request_url = request[1]
    print request_url, "\t", 1
    # print ip, "|", identity, "|", username, "|", date, "|", url, "|", response_code, "|", response_size

